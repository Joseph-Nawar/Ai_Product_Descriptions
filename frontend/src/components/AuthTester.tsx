import React from 'react';
import { useAuth } from '../auth/AuthProvider';

export function AuthTester() {
  const { user, loading, signOutUser } = useAuth();

  if (loading) {
    return (
      <div className="bg-gray-900 rounded-2xl border border-glass-border p-6">
        <h3 className="text-lg font-semibold text-gray-100 mb-4">Auth Status</h3>
        <div className="text-gray-400">Loading...</div>
      </div>
    );
  }

  return (
    <div className="bg-gray-900 rounded-2xl border border-glass-border p-6">
      <h3 className="text-lg font-semibold text-gray-100 mb-4">Auth Status (Development)</h3>
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-gray-300">User:</span>
          <span className="text-gray-400">
            {user ? `${user.email} (${user.uid})` : 'Not signed in'}
          </span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-gray-300">Status:</span>
          <span className={`px-2 py-1 rounded text-xs font-medium ${
            user ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'
          }`}>
            {user ? 'Authenticated' : 'Not authenticated'}
          </span>
        </div>
        {user && (
          <button
            onClick={signOutUser}
            className="w-full mt-4 px-4 py-2 bg-red-500/20 text-red-400 rounded-lg hover:bg-red-500/30 transition-colors"
          >
            Sign Out
          </button>
        )}
      </div>
    </div>
  );
}
