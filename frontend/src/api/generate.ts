import { api } from "./client";
import { BatchResponse, ProductInput } from "../types";
import { mockDownload, mockGenerate } from "./mock";

const USE_MOCK = (import.meta as any).env.VITE_USE_MOCK === "true";

export async function generateDescriptions(payload: ProductInput[] | FormData): Promise<BatchResponse> {
  if (USE_MOCK) {
    const list = Array.isArray(payload) ? payload : JSON.parse(String((payload as any).get("json") || "[]"));
    return mockGenerate(list);
  }
  // Accept both JSON array and CSV form-data (backend should handle both)
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
