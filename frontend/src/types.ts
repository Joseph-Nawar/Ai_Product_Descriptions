export type ProductInput = {
  id?: string;
  product_name: string;
  category: string;
  features: string;   // comma or newline separated
  audience: string;
  keywords?: string;  // optional SEO keywords
};

export type GeneratedItem = {
  id: string;
  product_name: string;
  category: string;
  audience: string;
  description: string;
  keywords?: string;
};

export type BatchResponse = {
  batch_id: string;
  items: GeneratedItem[];
};

export type ApiError = { message: string; status?: number };
