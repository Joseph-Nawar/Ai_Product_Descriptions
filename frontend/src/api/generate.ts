import { api } from "./client";
import { BatchResponse, BatchGenerationRequest } from "../types";
import { mockDownload, mockGenerate } from "./mock";

const USE_MOCK = (import.meta as any).env.VITE_USE_MOCK === "true";

export async function generateDescriptions(payload: BatchGenerationRequest | FormData): Promise<BatchResponse> {
  if (USE_MOCK) {
    const batchRequest = Array.isArray(payload) ? payload : JSON.parse(String((payload as any).get("json") || "[]"));
    // For mock, we'll use the products array directly
    const products = 'products' in batchRequest ? batchRequest.products : batchRequest;
    return mockGenerate(products);
  }
  
  // Accept both BatchGenerationRequest and CSV form-data (backend should handle both)
  const isFormData = typeof FormData !== "undefined" && payload instanceof FormData;
  const res = await api.post<BatchResponse>("/api/generate-batch", payload, {
    headers: isFormData ? { "Content-Type": "multipart/form-data" } : { "Content-Type": "application/json" }
  });
  return res.data;
}

export async function fetchBatch(batchId: string): Promise<BatchResponse> {
  if (USE_MOCK) {
    // In mock mode we don't persist batches; surface a clear error.
    throw new Error("Batch lookup not available in mock mode");
  }
  const res = await api.get<BatchResponse>(`/batch/${batchId}`);
  return res.data;
}

export async function downloadBatch(batchId: string): Promise<Blob> {
  if (USE_MOCK) return mockDownload(batchId);
  const res = await api.get(`/download/${batchId}`, { responseType: "blob" });
  return res.data;
}

export async function regenerateDescription(item: any): Promise<any> {
  if (USE_MOCK) {
    // Mock regeneration - return the same item with a new description
    return {
      ...item,
      description: `Regenerated description for ${item.product_name}: This is a mock regenerated description that showcases the product's key features and benefits.`,
      regenerating: false
    };
  }
  const res = await api.post(`/api/regenerate`, item);
  return res.data;
}