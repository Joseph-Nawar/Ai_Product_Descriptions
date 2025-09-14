import React from "react";

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "tertiary";
  glowing?: boolean;
};

export function Button({ variant = "primary", glowing = false, className = "", children, ...rest }: ButtonProps) {
  const baseStyles = "relative rounded-xl px-5 py-2.5 font-semibold transition-all duration-300 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed transform disabled:transform-none focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900";

  const variantStyles = {
    primary: `text-white shadow-lg hover:shadow-xl bg-[length:200%_auto] bg-gradient-to-r from-primary via-secondary to-primary
              hover:from-primary-dark hover:via-secondary-dark hover:to-primary-dark hover:-translate-y-0.5
              animate-shimmer`,
    secondary: "bg-white/10 text-gray-100 border border-glass-border hover:bg-white/20 backdrop-blur-sm",
    tertiary: "bg-transparent text-gray-400 hover:bg-white/10 hover:text-white",
  };
  
  const glowStyle = glowing ? "shadow-glow-primary" : "";

  return <button {...rest} className={`${baseStyles} ${variantStyles[variant]} ${glowStyle} ${className}`}>{children}</button>;
}

export function Input(props: React.InputHTMLAttributes<HTMLInputElement>) {
  const { className = "", ...rest } = props;
  return (
    <input
      {...rest}
      className={
        "w-full rounded-lg border-2 border-glass-border bg-white/5 px-4 py-2.5 text-gray-100 placeholder-gray-400 " + 
        "focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-primary focus:border-transparent " +
        "transition-all duration-200 shadow-sm " + className
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
        "w-full min-h-[96px] rounded-lg border-2 border-glass-border bg-white/5 px-4 py-2.5 text-gray-100 placeholder-gray-400 " +
        "focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-primary focus:border-transparent " +
        "transition-all duration-200 shadow-sm resize-none " + className
      }
    />
  );
}

export function Banner({ type = "info", children }: { type?: "info" | "success" | "error"; children: React.ReactNode }) {
  const styles = {
    info: "bg-blue-500/10 text-blue-300 border-blue-500/30",
    success: "bg-emerald-500/10 text-emerald-300 border-emerald-500/30",
    error: "bg-red-500/10 text-red-300 border-red-500/30",
  }[type];
  return <div className={`border rounded-lg p-4 text-center font-medium shadow-lg backdrop-blur-sm ${styles}`}>{children}</div>;
}

export function Spinner({ size = "md" }: { size?: "sm" | "md" | "lg" }) {
  const sizes = {
    sm: "h-4 w-4",
    md: "h-5 w-5",
    lg: "h-8 w-8",
  };
  return (
    <div className={`${sizes[size]} rounded-full border-2 border-white/30 border-t-white animate-spin`}></div>
  );
}

export function StatusAnnouncer({ message }: { message: string }) {
  return <div aria-live="polite" aria-atomic="true" className="sr-only">{message}</div>;
}

export function Tooltip({ text, children }: { text: string; children: React.ReactNode }) {
  return (
    <div className="relative flex items-center group">
      {children}
      <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-max max-w-xs px-3 py-1.5 bg-gray-800 border border-glass-border text-white text-xs rounded-md shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-10">
        {text}
      </div>
    </div>
  );
}