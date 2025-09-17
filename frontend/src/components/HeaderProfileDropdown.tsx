import React, { useState, useRef, useEffect } from "react";
import { useAuth } from "../auth/AuthProvider";
import { Link } from "react-router-dom";

export const HeaderProfileDropdown: React.FC = () => {
  const { user, signOutUser, loading } = useAuth();
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Handle outside clicks to close dropdown
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsDropdownOpen(false);
      }
    }

    if (isDropdownOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isDropdownOpen]);

  if (loading) {
    return (
      <div className="flex items-center space-x-2">
        <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-white"></div>
      </div>
    );
  }

  if (!user) {
    return (
      <Link 
        to="/login" 
        className="flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium text-gray-100 hover:bg-gray-700/50 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200"
      >
        <div className="w-8 h-8 bg-gradient-to-r from-gray-500 to-gray-600 rounded-full flex items-center justify-center text-white text-sm font-bold shadow-lg">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
        </div>
        <span className="hidden md:block">Sign In</span>
      </Link>
    );
  }

  const handleSignOut = async () => {
    try {
      await signOutUser();
      setIsDropdownOpen(false);
    } catch (error) {
      console.error("Sign out error:", error);
    }
  };

  const userDisplayName = user.displayName || user.email || "User";
  const userInitials = userDisplayName
    .split(" ")
    .map(name => name[0])
    .join("")
    .toUpperCase()
    .slice(0, 2);

  return (
    <div className="relative" ref={dropdownRef}>
      <button
        onClick={() => setIsDropdownOpen(!isDropdownOpen)}
        className="flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium text-gray-100 hover:bg-gray-700/50 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200"
        aria-haspopup="true"
        aria-expanded={isDropdownOpen}
        aria-label="User profile menu"
      >
        <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white text-sm font-bold shadow-lg">
          {user.photoURL ? (
            <img
              src={user.photoURL}
              alt={userDisplayName}
              className="w-8 h-8 rounded-full object-cover"
            />
          ) : (
            userInitials
          )}
        </div>
        <span className="hidden md:block max-w-32 truncate">{userDisplayName}</span>
        <svg
          className={`w-4 h-4 transition-transform duration-200 ${isDropdownOpen ? "rotate-180" : ""}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {isDropdownOpen && (
        <div className="absolute right-0 mt-2 w-64 bg-white/95 backdrop-blur-lg rounded-xl shadow-2xl border border-gray-200/50 z-[99999] overflow-hidden">
          {/* User Info Section */}
          <div className="px-4 py-3 border-b border-gray-200/50 bg-gradient-to-r from-gray-50 to-gray-100/50">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white text-sm font-bold shadow-lg">
                {user.photoURL ? (
                  <img
                    src={user.photoURL}
                    alt={userDisplayName}
                    className="w-10 h-10 rounded-full object-cover"
                  />
                ) : (
                  userInitials
                )}
              </div>
              <div className="flex-1 min-w-0">
                <div className="font-semibold text-gray-900 truncate">{userDisplayName}</div>
                <div className="text-sm text-gray-600 truncate">{user.email}</div>
              </div>
            </div>
          </div>
          
          {/* Menu Items */}
          <div className="py-1">
            <button
              onClick={handleSignOut}
              className="flex items-center w-full px-4 py-3 text-sm text-gray-700 hover:bg-red-50 hover:text-red-700 focus:outline-none focus:bg-red-50 transition-colors duration-200"
              aria-label="Sign out"
            >
              <svg className="w-4 h-4 mr-3 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              <span className="font-medium">Sign out</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
