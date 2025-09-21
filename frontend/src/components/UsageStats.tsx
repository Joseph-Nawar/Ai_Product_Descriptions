import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { UsageStats as UsageStatsType } from '../types';

interface UsageStatsProps {
  onRefresh?: () => void;
  className?: string;
  showCharts?: boolean;
}

export function UsageStats({ onRefresh, className = "", showCharts = true }: UsageStatsProps) {
  const [stats, setStats] = useState<UsageStatsType | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      setLoading(true);
      setError(null);
      // TODO: Endpoint not yet implemented. Commented out to prevent 404s and rate limiting.
      // const statsData = await paymentApi.getUsageStats();
      // setStats(statsData);
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
    }
  };

  const handleRefresh = async () => {
    try {
      setRefreshing(true);
      await loadStats();
      if (onRefresh) {
        onRefresh();
      }
    } finally {
      setRefreshing(false);
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

  const getUsageTrend = () => {
    if (!stats) return 'stable';
    const avg = stats.average_generations_per_day;
    if (avg > 10) return 'high';
    if (avg > 5) return 'moderate';
    return 'low';
  };

  const getTrendColor = () => {
    const trend = getUsageTrend();
    switch (trend) {
      case 'high': return 'text-emerald-400';
      case 'moderate': return 'text-yellow-400';
      case 'low': return 'text-blue-400';
      default: return 'text-gray-400';
    }
  };

  const getTrendIcon = () => {
    const trend = getUsageTrend();
    switch (trend) {
      case 'high': return '📈';
      case 'moderate': return '📊';
      case 'low': return '📉';
      default: return '📊';
    }
  };

  // Simple chart component for usage visualization
  const UsageChart = ({ data, title }: { data: number; title: string }) => {
    const maxValue = Math.max(data, 10); // Minimum scale
    const percentage = (data / maxValue) * 100;
    
    return (
      <div className="bg-white/5 rounded-lg p-4">
        <div className="text-sm text-gray-400 mb-2">{title}</div>
        <div className="text-2xl font-bold text-white mb-2">{data.toLocaleString()}</div>
        <div className="w-full bg-gray-700 rounded-full h-2">
          <div
            className="h-2 bg-gradient-to-r from-primary to-secondary rounded-full transition-all duration-500"
            style={{ width: `${Math.min(percentage, 100)}%` }}
          />
        </div>
      </div>
    );
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

  if (!stats) {
    return (
      <div className={className}>
        <Banner type="error">Unable to load usage statistics</Banner>
      </div>
    );
  }

  return (
    <div className={`space-y-6 ${className}`}>
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-bold text-white">Usage Statistics</h3>
        <Button
          onClick={handleRefresh}
          disabled={refreshing}
          variant="tertiary"
          size="sm"
        >
          {refreshing ? <Spinner size="sm" /> : 'Refresh'}
        </Button>
      </div>

      {/* Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="text-sm text-gray-400 mb-1">Total Generations</div>
          <div className="text-2xl font-bold text-white">{stats.total_generations.toLocaleString()}</div>
          <div className="text-xs text-gray-500 mt-1">All time</div>
        </div>

        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="text-sm text-gray-400 mb-1">Today's Usage</div>
          <div className="text-2xl font-bold text-white">{stats.credits_used_today.toLocaleString()}</div>
          <div className="text-xs text-gray-500 mt-1">Credits used</div>
        </div>

        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="text-sm text-gray-400 mb-1">This Month</div>
          <div className="text-2xl font-bold text-white">{stats.credits_used_this_month.toLocaleString()}</div>
          <div className="text-xs text-gray-500 mt-1">Credits used</div>
        </div>

        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="text-sm text-gray-400 mb-1">Daily Average</div>
          <div className="text-2xl font-bold text-white">{stats.average_generations_per_day.toFixed(1)}</div>
          <div className="text-xs text-gray-500 mt-1">Generations/day</div>
        </div>
      </div>

      {/* Usage Trend */}
      <div className="bg-white/5 rounded-lg border border-glass-border p-6">
        <div className="flex items-center justify-between mb-4">
          <h4 className="text-lg font-semibold text-white">Usage Trend</h4>
          <div className={`flex items-center text-sm ${getTrendColor()}`}>
            <span className="mr-2">{getTrendIcon()}</span>
            {getUsageTrend().charAt(0).toUpperCase() + getUsageTrend().slice(1)} Activity
          </div>
        </div>
        
        <div className="text-gray-400 text-sm">
          You're averaging <span className="text-white font-semibold">{stats.average_generations_per_day.toFixed(1)}</span> generations per day.
          {stats.average_generations_per_day > 10 && (
            <span className="text-emerald-400 ml-2">Great usage! 🚀</span>
          )}
        </div>
      </div>

      {/* Charts Section */}
      {showCharts && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <UsageChart 
            data={stats.total_generations} 
            title="Total Generations" 
          />
          <UsageChart 
            data={stats.credits_used_this_month} 
            title="Monthly Usage" 
          />
        </div>
      )}

      {/* Last Activity */}
      {stats.last_generation_date && (
        <div className="bg-white/5 rounded-lg border border-glass-border p-4">
          <div className="text-sm text-gray-400 mb-1">Last Generation</div>
          <div className="text-white font-medium">
            {formatDate(stats.last_generation_date)}
          </div>
        </div>
      )}

      {/* Usage Insights */}
      <div className="bg-gradient-to-r from-primary/10 to-secondary/10 rounded-lg border border-primary/30 p-6">
        <h4 className="text-lg font-semibold text-white mb-3">Usage Insights</h4>
        <div className="space-y-2 text-sm text-gray-300">
          {stats.average_generations_per_day > 10 && (
            <div className="flex items-center">
              <span className="text-emerald-400 mr-2">✓</span>
              You're a power user! Consider upgrading to a higher plan for better value.
            </div>
          )}
          {stats.credits_used_today > 50 && (
            <div className="flex items-center">
              <span className="text-yellow-400 mr-2">⚠</span>
              High usage today. Monitor your credit balance.
            </div>
          )}
          {stats.average_generations_per_day < 2 && (
            <div className="flex items-center">
              <span className="text-blue-400 mr-2">💡</span>
              You have room to explore more features and generate more content.
            </div>
          )}
          <div className="flex items-center">
            <span className="text-primary mr-2">📊</span>
            Your usage pattern shows consistent engagement with the platform.
          </div>
        </div>
      </div>
    </div>
  );
}



