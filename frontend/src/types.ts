export type ProductInput = {
  id?: string;
  product_name: string;
  category: string;
  features: string;
  audience: string;
  keywords?: string;
};

export type GeneratedItem = {
  id: string;
  product_name: string;
  category: string;
  audience: string;
  description: string;
  keywords?: string;
  features: string; // Add original features for regeneration
  tone: string; // Add original tone for regeneration
  style_variation: string; // Add original style variation for regeneration
  regenerating?: boolean; // New: For UI loading state on a single row
};

export type BatchGenerationRequest = {
  products: ProductInput[];
  batchTone: string;
  batchStyle: string;
};

export type BatchResponse = {
  batch_id: string;
  items: GeneratedItem[];
};

export type ApiError = { message: string; status?: number };