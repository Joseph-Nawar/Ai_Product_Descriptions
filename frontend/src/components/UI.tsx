import React from "react";

export function Button(props: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  const { className = "", ...rest } = props;
  return (
    <button
      {...rest}
      className={
        "relative rounded-xl px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold hover:from-blue-700 hover:to-purple-700 transition-all duration-200 shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-105 disabled:hover:scale-100 " + className
      }
    />
  );
}

export function Input(props: React.InputHTMLAttributes<HTMLInputElement>) {
  const { className = "", ...rest } = props;
  return (
    <input
      {...rest}
      className={
        "w-full rounded-xl border-2 border-gray-200 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-white shadow-sm hover:border-gray-300 " + className
      }
    />
  );
}

export function Textarea(props: React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
  const { className = "", ...rest } = props;
  return (
    <textarea
      {...rest}
      className={
        "w-full min-h-[96px] rounded-xl border-2 border-gray-200 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-white shadow-sm hover:border-gray-300 resize-none " + className
      }
    />
  );
}

export function Banner({ type = "info", children }: { type?: "info" | "success" | "error"; children: React.ReactNode }) {
  const styles = {
    info: "bg-gradient-to-r from-blue-50 to-blue-100 text-blue-900 border-blue-200 shadow-sm",
    success: "bg-gradient-to-r from-green-50 to-green-100 text-green-900 border-green-200 shadow-sm",
    error: "bg-gradient-to-r from-red-50 to-red-100 text-red-900 border-red-200 shadow-sm"
  }[type];
  return <div className={`border-2 rounded-xl p-4 ${styles}`}>{children}</div>;
}

export function Spinner() {
  return (
    <div className="flex items-center justify-center">
      <div className="h-6 w-6 rounded-full border-3 border-blue-200 border-t-blue-600 animate-spin"></div>
    </div>
  );
}

export function StatusAnnouncer({ message }: { message: string }) {
  return (
    <div 
      aria-live="polite" 
      aria-atomic="true" 
      className="sr-only"
    >
      {message}
    </div>
  );
}