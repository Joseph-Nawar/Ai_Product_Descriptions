import { usePaymentStore } from '../store/paymentStore';

interface OfflineAction {
  id: string;
  type: string;
  payload: any;
  timestamp: number;
  retryCount: number;
  maxRetries: number;
}

interface SyncResult {
  success: boolean;
  error?: string;
  actionId: string;
}

class OfflineSyncService {
  private pendingActions: Map<string, OfflineAction> = new Map();
  private syncInProgress = false;
  private syncInterval: NodeJS.Timeout | null = null;
  private readonly STORAGE_KEY = 'offline_payment_actions';
  private readonly SYNC_INTERVAL = 30000; // 30 seconds
  private readonly MAX_RETRIES = 3;

  constructor() {
    this.loadPendingActions();
    this.startSyncInterval();
    this.setupOnlineListener();
  }

  /**
   * Add an action to be synced when online
   */
  addAction(type: string, payload: any): string {
    const actionId = this.generateActionId();
    const action: OfflineAction = {
      id: actionId,
      type,
      payload,
      timestamp: Date.now(),
      retryCount: 0,
      maxRetries: this.MAX_RETRIES
    };

    this.pendingActions.set(actionId, action);
    this.savePendingActions();
    
    // Also add to payment store for immediate UI updates
    usePaymentStore.getState().addPendingAction({
      type,
      payload
    });

    return actionId;
  }

  /**
   * Remove a completed action
   */
  removeAction(actionId: string): void {
    this.pendingActions.delete(actionId);
    this.savePendingActions();
  }

  /**
   * Get all pending actions
   */
  getPendingActions(): OfflineAction[] {
    return Array.from(this.pendingActions.values());
  }

  /**
   * Sync all pending actions
   */
  async syncAll(): Promise<SyncResult[]> {
    if (this.syncInProgress) {
      return [];
    }

    this.syncInProgress = true;
    const results: SyncResult[] = [];

    try {
      const actions = Array.from(this.pendingActions.values());
      
      for (const action of actions) {
        try {
          const result = await this.syncAction(action);
          results.push(result);
          
          if (result.success) {
            this.removeAction(action.id);
          } else {
            // Increment retry count
            action.retryCount++;
            if (action.retryCount >= action.maxRetries) {
              // Remove action after max retries
              this.removeAction(action.id);
              console.warn(`Action ${action.id} exceeded max retries and was removed`);
            } else {
              this.pendingActions.set(action.id, action);
            }
          }
        } catch (error) {
          console.error(`Failed to sync action ${action.id}:`, error);
          results.push({
            success: false,
            error: error instanceof Error ? error.message : 'Unknown error',
            actionId: action.id
          });
        }
      }

      this.savePendingActions();
    } finally {
      this.syncInProgress = false;
    }

    return results;
  }

  /**
   * Sync a single action
   */
  private async syncAction(action: OfflineAction): Promise<SyncResult> {
    try {
      switch (action.type) {
        case 'consume_credits':
          await this.syncConsumeCredits(action.payload);
          break;
        
        case 'update_subscription':
          await this.syncUpdateSubscription(action.payload);
          break;
        
        case 'cancel_subscription':
          await this.syncCancelSubscription(action.payload);
          break;
        
        case 'reactivate_subscription':
          await this.syncReactivateSubscription(action.payload);
          break;
        
        case 'purchase_credits':
          await this.syncPurchaseCredits(action.payload);
          break;
        
        default:
          throw new Error(`Unknown action type: ${action.type}`);
      }

      return {
        success: true,
        actionId: action.id
      };
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error',
        actionId: action.id
      };
    }
  }

  /**
   * Sync credit consumption
   */
  private async syncConsumeCredits(payload: { amount: number; description?: string }): Promise<void> {
    // This would typically make an API call to log the credit usage
    // For now, we'll just validate that the action was valid
    if (payload.amount <= 0) {
      throw new Error('Invalid credit amount');
    }
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  /**
   * Sync subscription update
   */
  private async syncUpdateSubscription(payload: { subscriptionId: string; variantId: string }): Promise<void> {
    const { paymentApi } = await import('../api/client');
    await paymentApi.updateSubscription(payload.subscriptionId, payload.variantId);
  }

  /**
   * Sync subscription cancellation
   */
  private async syncCancelSubscription(payload: { subscriptionId: string }): Promise<void> {
    const { paymentApi } = await import('../api/client');
    await paymentApi.cancelSubscription(payload.subscriptionId);
  }

  /**
   * Sync subscription reactivation
   */
  private async syncReactivateSubscription(payload: { subscriptionId: string }): Promise<void> {
    const { paymentApi } = await import('../api/client');
    await paymentApi.reactivateSubscription(payload.subscriptionId);
  }

  /**
   * Sync credit purchase
   */
  private async syncPurchaseCredits(payload: { amount: number; variantId?: string }): Promise<void> {
    const { paymentApi } = await import('../api/client');
    if (!payload.variantId) {
      throw new Error('Variant ID is required for credit purchase');
    }
    await paymentApi.createCheckoutSession(payload.variantId);
  }

  /**
   * Start automatic sync interval
   */
  private startSyncInterval(): void {
    this.syncInterval = setInterval(() => {
      if (navigator.onLine && this.pendingActions.size > 0) {
        this.syncAll();
      }
    }, this.SYNC_INTERVAL);
  }

  /**
   * Setup online/offline listeners
   */
  private setupOnlineListener(): void {
    window.addEventListener('online', () => {
      this.syncAll();
    });
  }

  /**
   * Load pending actions from localStorage
   */
  private loadPendingActions(): void {
    try {
      const stored = localStorage.getItem(this.STORAGE_KEY);
      if (stored) {
        const actions: OfflineAction[] = JSON.parse(stored);
        
        // Filter out old actions (older than 24 hours)
        const now = Date.now();
        const validActions = actions.filter(action => 
          now - action.timestamp < 24 * 60 * 60 * 1000
        );
        
        validActions.forEach(action => {
          this.pendingActions.set(action.id, action);
        });
      }
    } catch (error) {
      console.error('Failed to load pending actions:', error);
    }
  }

  /**
   * Save pending actions to localStorage
   */
  private savePendingActions(): void {
    try {
      const actions = Array.from(this.pendingActions.values());
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(actions));
    } catch (error) {
      console.error('Failed to save pending actions:', error);
    }
  }

  /**
   * Generate unique action ID
   */
  private generateActionId(): string {
    return `action_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  /**
   * Clear all pending actions
   */
  clearAll(): void {
    this.pendingActions.clear();
    this.savePendingActions();
  }

  /**
   * Get sync status
   */
  getStatus(): {
    pendingCount: number;
    syncInProgress: boolean;
    isOnline: boolean;
  } {
    return {
      pendingCount: this.pendingActions.size,
      syncInProgress: this.syncInProgress,
      isOnline: navigator.onLine
    };
  }

  /**
   * Cleanup
   */
  destroy(): void {
    if (this.syncInterval) {
      clearInterval(this.syncInterval);
      this.syncInterval = null;
    }
    
    window.removeEventListener('online', () => {
      this.syncAll();
    });
  }
}

// Create singleton instance
export const offlineSyncService = new OfflineSyncService();

// Export the class for testing
export { OfflineSyncService };

// Export types
export type { OfflineAction, SyncResult };



