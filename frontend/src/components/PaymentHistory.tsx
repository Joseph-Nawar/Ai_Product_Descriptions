import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { PaymentTransaction } from '../types';

interface PaymentHistoryProps {
  onRefresh?: () => void;
  className?: string;
  itemsPerPage?: number;
}

export function PaymentHistory({ 
  onRefresh, 
  className = "", 
  itemsPerPage = 10 
}: PaymentHistoryProps) {
  const [transactions, setTransactions] = useState<PaymentTransaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);

  useEffect(() => {
    loadTransactions();
  }, []);

  const loadTransactions = async (page = 1, append = false) => {
    try {
      if (page === 1) {
        setLoading(true);
      } else {
        setLoadingMore(true);
      }
      setError(null);

      const response = await paymentApi.getPaymentHistory(page, itemsPerPage);
      const newTransactions = response.data || response;
      
      if (append) {
        setTransactions(prev => [...prev, ...newTransactions]);
      } else {
        setTransactions(newTransactions);
      }
      
      setHasMore(newTransactions.length === itemsPerPage);
      setCurrentPage(page);
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
      setLoadingMore(false);
    }
  };

  const handleRefresh = async () => {
    try {
      setRefreshing(true);
      await loadTransactions(1, false);
      if (onRefresh) {
        onRefresh();
      }
    } finally {
      setRefreshing(false);
    }
  };

  const handleLoadMore = () => {
    if (!loadingMore && hasMore) {
      loadTransactions(currentPage + 1, true);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const formatAmount = (amount: number, currency: string) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency.toUpperCase(),
    }).format(amount);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed': return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30';
      case 'pending': return 'text-yellow-400 bg-yellow-500/10 border-yellow-500/30';
      case 'failed': return 'text-red-400 bg-red-500/10 border-red-500/30';
      case 'refunded': return 'text-blue-400 bg-blue-500/10 border-blue-500/30';
      default: return 'text-gray-400 bg-gray-500/10 border-gray-500/30';
    }
  };

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'subscription': return '🔄';
      case 'credit_purchase': return '💳';
      case 'refund': return '↩️';
      default: return '💰';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed': return '✓';
      case 'pending': return '⏳';
      case 'failed': return '✗';
      case 'refunded': return '↩️';
      default: return '?';
    }
  };

  if (loading) {
    return (
      <div className={`flex justify-center items-center py-12 ${className}`}>
        <Spinner size="lg" />
      </div>
    );
  }

  if (error) {
    return (
      <div className={className}>
        <Banner type="error">{error}</Banner>
        <div className="mt-4 text-center">
          <Button onClick={handleRefresh} variant="secondary">
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className={`space-y-6 ${className}`}>
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-bold text-white">Payment History</h3>
        <Button
          onClick={handleRefresh}
          disabled={refreshing}
          variant="tertiary"
          size="sm"
        >
          {refreshing ? <Spinner size="sm" /> : 'Refresh'}
        </Button>
      </div>

      {/* Transactions List */}
      {transactions.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">💳</div>
          <h4 className="text-lg font-semibold text-white mb-2">No Transactions Yet</h4>
          <p className="text-gray-400 mb-6">
            Your payment history will appear here once you make your first purchase.
          </p>
          <Button
            onClick={() => window.location.href = '/pricing'}
            variant="primary"
          >
            View Pricing Plans
          </Button>
        </div>
      ) : (
        <div className="space-y-4">
          {transactions.map((transaction) => (
            <div
              key={transaction.id}
              className="bg-white/5 rounded-lg border border-glass-border p-4 hover:bg-white/10 transition-all duration-200"
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <div className="text-2xl">
                    {getTypeIcon(transaction.type)}
                  </div>
                  
                  <div>
                    <div className="text-white font-semibold">
                      {transaction.description}
                    </div>
                    <div className="text-sm text-gray-400">
                      {formatDate(transaction.created_at)}
                    </div>
                    {transaction.lemon_squeezy_order_id && (
                      <div className="text-xs text-gray-500 mt-1">
                        Order: {transaction.lemon_squeezy_order_id}
                      </div>
                    )}
                  </div>
                </div>

                <div className="text-right">
                  <div className={`text-lg font-bold ${
                    transaction.type === 'refund' ? 'text-red-400' : 'text-white'
                  }`}>
                    {transaction.type === 'refund' ? '-' : ''}
                    {formatAmount(transaction.amount, transaction.currency)}
                  </div>
                  
                  <div className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium border ${getStatusColor(transaction.status)}`}>
                    <span className="mr-1">{getStatusIcon(transaction.status)}</span>
                    {transaction.status.charAt(0).toUpperCase() + transaction.status.slice(1)}
                  </div>
                </div>
              </div>
            </div>
          ))}

          {/* Load More Button */}
          {hasMore && (
            <div className="text-center pt-4">
              <Button
                onClick={handleLoadMore}
                disabled={loadingMore}
                variant="secondary"
              >
                {loadingMore ? (
                  <>
                    <Spinner size="sm" className="mr-2" />
                    Loading...
                  </>
                ) : (
                  'Load More'
                )}
              </Button>
            </div>
          )}
        </div>
      )}

      {/* Summary */}
      {transactions.length > 0 && (
        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div>
              <div className="text-2xl font-bold text-emerald-400">
                {transactions.filter(t => t.status === 'completed').length}
              </div>
              <div className="text-sm text-gray-400">Completed</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-yellow-400">
                {transactions.filter(t => t.status === 'pending').length}
              </div>
              <div className="text-sm text-gray-400">Pending</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-red-400">
                {transactions.filter(t => t.status === 'failed').length}
              </div>
              <div className="text-sm text-gray-400">Failed</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-blue-400">
                {transactions.filter(t => t.status === 'refunded').length}
              </div>
              <div className="text-sm text-gray-400">Refunded</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
