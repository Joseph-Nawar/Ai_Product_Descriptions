import { api } from "./client";
import { BatchResponse, BatchGenerationRequest } from "../types";
import { mockDownload, mockGenerate } from "./mock";

const USE_MOCK = (import.meta as any).env.VITE_USE_MOCK === "true";

export async function generateDescriptionsFromCsv(file: File, audience: string, languageCode: string = "en"): Promise<BatchResponse> {
  if (USE_MOCK) {
    // For mock, parse the CSV and use the existing mock generation
    const Papa = await import("papaparse");
    const csvText = await file.text();
    const parsed = Papa.parse(csvText, { header: true, skipEmptyLines: true });
    const products = parsed.data.map((row: any, index: number) => ({
      id: String(row.id || `row_${index}`).trim(),
      product_name: String(row.product_name || row.title || row.name || "").trim(),
      category: String(row.category || row.type || "").trim(),
      features: String(row.features || "").trim(),
      audience: audience.trim(),
      keywords: row.keywords ? String(row.keywords).trim() : undefined,
      languageCode: languageCode
    })).filter((r: any) => r.product_name);
    
    return mockGenerate(products);
  }
  
  const formData = new FormData();
  formData.append("file", file);
  formData.append("audience", audience);
  formData.append("languageCode", languageCode);
  
  const res = await api.post<BatchResponse>("/api/generate-batch-csv", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
  return res.data;
}

export async function generateDescriptions(payload: BatchGenerationRequest): Promise<BatchResponse> {
  if (USE_MOCK) {
    const products = payload.products;
    return mockGenerate(products);
  }
  
  const res = await api.post<BatchResponse>("/api/generate-batch", payload, {
    headers: { "Content-Type": "application/json" }
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