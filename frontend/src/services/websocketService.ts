import { usePaymentStore } from '../store/paymentStore';

interface WebSocketMessage {
  type: string;
  data: any;
  timestamp: number;
}

interface WebSocketService {
  connect: () => void;
  disconnect: () => void;
  send: (message: any) => void;
  isConnected: () => boolean;
  reconnect: () => void;
}

class PaymentWebSocketService implements WebSocketService {
  private ws: WebSocket | null = null;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;
  private reconnectDelay = 5000;
  private reconnectTimer: NodeJS.Timeout | null = null;
  private heartbeatInterval: NodeJS.Timeout | null = null;
  private heartbeatDelay = 30000; // 30 seconds

  constructor() {
    this.handleOnlineStatus = this.handleOnlineStatus.bind(this);
    this.handleOfflineStatus = this.handleOfflineStatus.bind(this);
    
    // Listen for online/offline status
    if (typeof window !== 'undefined') {
      window.addEventListener('online', this.handleOnlineStatus);
      window.addEventListener('offline', this.handleOfflineStatus);
    }
  }

  connect(): void {
    // WebSocket endpoint not implemented on backend yet
    // Disable WebSocket connection to prevent page crashes
    console.log('WebSocket connection disabled - endpoint not implemented on backend');
    return;
    
    if (this.ws?.readyState === WebSocket.OPEN) {
      return;
    }

    try {
      const wsUrl = import.meta.env.VITE_WS_URL || `ws://localhost:8000/ws/payments`;
      this.ws = new WebSocket(wsUrl);

      if (this.ws) {
        this.ws!.onopen = this.handleOpen.bind(this);
        this.ws!.onmessage = this.handleMessage.bind(this);
        this.ws!.onclose = this.handleClose.bind(this);
        this.ws!.onerror = this.handleError.bind(this);
      }

    } catch (error) {
      console.error('Failed to create WebSocket connection:', error);
      this.scheduleReconnect();
    }
  }

  disconnect(): void {
    if (this.reconnectTimer) {
      clearTimeout(this.reconnectTimer);
      this.reconnectTimer = null;
    }

    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      this.heartbeatInterval = null;
    }

    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }

    this.reconnectAttempts = 0;
    
    // Update store state
    usePaymentStore.getState().disconnectWebSocket();
  }

  send(message: any): void {
    if (this.ws?.readyState === WebSocket.OPEN) {
      const wsMessage: WebSocketMessage = {
        type: message.type || 'message',
        data: message,
        timestamp: Date.now()
      };
      
      this.ws.send(JSON.stringify(wsMessage));
    } else {
      console.warn('WebSocket is not connected. Cannot send message:', message);
    }
  }

  isConnected(): boolean {
    return this.ws?.readyState === WebSocket.OPEN;
  }

  reconnect(): void {
    this.disconnect();
    this.connect();
  }

  private handleOpen(): void {
    console.log('WebSocket connected');
    this.reconnectAttempts = 0;
    
    // Update store state
    usePaymentStore.setState(state => ({
      wsState: {
        ...state.wsState,
        connected: true,
        reconnecting: false,
        reconnectAttempts: 0
      }
    }));

    // Start heartbeat
    this.startHeartbeat();

    // Send authentication message if user is logged in
    this.sendAuthentication();
  }

  private handleMessage(event: MessageEvent): void {
    try {
      const message = JSON.parse(event.data);
      
      // Update last message in store
      usePaymentStore.setState(state => ({
        wsState: {
          ...state.wsState,
          lastMessage: event.data
        }
      }));

      // Handle different message types
      this.handleWebSocketMessage(message);

    } catch (error) {
      console.error('Failed to parse WebSocket message:', error);
    }
  }

  private handleClose(event: CloseEvent): void {
    console.log('WebSocket disconnected:', event.code, event.reason);
    
    // Update store state
    usePaymentStore.setState(state => ({
      wsState: {
        ...state.wsState,
        connected: false,
        reconnecting: false
      }
    }));

    this.stopHeartbeat();

    // Attempt to reconnect if not a clean close
    if (event.code !== 1000 && this.reconnectAttempts < this.maxReconnectAttempts) {
      this.scheduleReconnect();
    }
  }

  private handleError(error: Event): void {
    console.error('WebSocket error:', error);
    
    // Update store state
    usePaymentStore.setState(state => ({
      wsState: {
        ...state.wsState,
        connected: false,
        reconnecting: false
      }
    }));
  }

  private scheduleReconnect(): void {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      console.log('Max reconnection attempts reached');
      return;
    }

    this.reconnectAttempts++;
    const delay = this.reconnectDelay * Math.pow(2, this.reconnectAttempts - 1); // Exponential backoff

    console.log(`Scheduling reconnection attempt ${this.reconnectAttempts} in ${delay}ms`);

    // Update store state
    usePaymentStore.setState(state => ({
      wsState: {
        ...state.wsState,
        reconnecting: true,
        reconnectAttempts: this.reconnectAttempts
      }
    }));

    this.reconnectTimer = setTimeout(() => {
      this.connect();
    }, delay);
  }

  private startHeartbeat(): void {
    this.heartbeatInterval = setInterval(() => {
      if (this.ws?.readyState === WebSocket.OPEN) {
        this.send({ type: 'ping' });
      }
    }, this.heartbeatDelay);
  }

  private stopHeartbeat(): void {
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      this.heartbeatInterval = null;
    }
  }

  private sendAuthentication(): void {
    // Get current user token and send authentication message
    import('../auth/token').then(({ getIdToken }) => {
      getIdToken().then(token => {
        if (token) {
          this.send({
            type: 'auth',
            token: token
          });
        }
      }).catch(error => {
        console.error('Failed to get auth token for WebSocket:', error);
      });
    });
  }

  private handleWebSocketMessage(message: WebSocketMessage): void {
    const { type, data } = message;

    switch (type) {
      case 'pong':
        // Heartbeat response - no action needed
        break;

      case 'credit_update':
        // Update credit balance
        usePaymentStore.getState().updateCredits(data.amount, 'set');
        break;

      case 'subscription_update':
        // Refresh subscription data
        usePaymentStore.getState().fetchCurrentSubscription();
        break;

      case 'payment_completed':
        // Payment completed - refresh all data
        usePaymentStore.getState().refreshAll();
        break;

      case 'usage_update':
        // Usage statistics updated
        usePaymentStore.getState().fetchUsageStats();
        break;

      case 'subscription_cancelled':
        // Subscription was cancelled
        usePaymentStore.getState().fetchCurrentSubscription();
        break;

      case 'subscription_reactivated':
        // Subscription was reactivated
        usePaymentStore.getState().fetchCurrentSubscription();
        break;

      case 'credit_warning':
        // Low credit warning
        usePaymentStore.getState().setShowCreditWarning(true);
        break;

      case 'error':
        console.error('WebSocket server error:', data);
        break;

      default:
        console.log('Unknown WebSocket message type:', type, data);
    }
  }

  private handleOnlineStatus(): void {
    console.log('Network is online - attempting to reconnect WebSocket');
    this.connect();
  }

  private handleOfflineStatus(): void {
    console.log('Network is offline - disconnecting WebSocket');
    this.disconnect();
  }

  // Cleanup method
  destroy(): void {
    this.disconnect();
    
    if (typeof window !== 'undefined') {
      window.removeEventListener('online', this.handleOnlineStatus);
      window.removeEventListener('offline', this.handleOfflineStatus);
    }
  }
}

// Create singleton instance
export const websocketService = new PaymentWebSocketService();

// Export the class for testing
export { PaymentWebSocketService };

// Export types
export type { WebSocketMessage, WebSocketService };



