import axios, { AxiosError } from "axios";
function trimTrailingSlash(s: string) { return s.endsWith("/") ? s.slice(0, -1) : s; }
const env = (import.meta as any).env || {};
const base = env.VITE_API_BASE_URL || env.VITE_API_BASE || "http://localhost:8000";
export const API_BASE = trimTrailingSlash(String(base));
export const api = axios.create({ baseURL: API_BASE, timeout: 30000, headers: { "Content-Type": "application/json" } });

// Enhanced error handling for rate limits
export function handleApiError(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const axiosError = error as AxiosError;
    
    if (axiosError.response?.status === 429) {
      const retryAfter = axiosError.response.headers['retry-after'];
      const seconds = retryAfter ? parseInt(retryAfter) : 60;
      return `Rate limit exceeded. Please wait ${seconds} seconds before trying again.`;
    }
    
    if (axiosError.response?.status === 400) {
      return "Invalid request. Please check your input and try again.";
    }
    
    if (axiosError.response?.status === 500) {
      return "Server error. Please try again later.";
    }
    
    if (axiosError.code === 'ECONNABORTED') {
      return "Request timed out. Please try again.";
    }
  }
  
  return error instanceof Error ? error.message : "An unexpected error occurred.";
}
