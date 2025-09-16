import React from 'react';

interface ProductGenieLogoProps {
  size?: 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

export default function ProductGenieLogo({ size = 'md', className = '' }: ProductGenieLogoProps) {
  const sizeClasses = {
    sm: 'w-8 h-8',
    md: 'w-10 h-10',
    lg: 'w-16 h-16',
    xl: 'w-32 h-32'
  };

  // Calculate actual pixel sizes for srcset
  const pixelSizes = {
    sm: 32,
    md: 40,
    lg: 64,
    xl: 128
  };

  const currentSize = pixelSizes[size];

  return (
    <img 
      src="/productgenie-logo.png" 
      alt="ProductGenie Logo" 
      className={`${sizeClasses[size]} ${className}`}
      width={currentSize}
      height={currentSize}
      loading="eager"
      fetchpriority="high"
      decoding="async"
      // Responsive image attributes for better performance
      sizes={`${currentSize}px`}
    />
  );
}
