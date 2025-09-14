import { BatchResponse, ProductInput } from "../types";

const wait = (ms: number) => new Promise(res => setTimeout(res, ms));

// Simple mock generator for dev
export async function mockGenerate(inputs: ProductInput[]): Promise<BatchResponse> {
  await wait(800);
  const batch_id = crypto.randomUUID();
  const items = inputs.map((p, i) => ({
    id: `${batch_id}-${i + 1}`,
    product_name: p.product_name,
    category: p.category,
    audience: p.audience,
    keywords: p.keywords,
    features: p.features,
    tone: "professional", // Default for mock
    style_variation: "amazon", // Default for mock
    description: `Introducing ${p.product_name}: a ${p.category} perfect for ${p.audience}. Key features: ${p.features}. SEO-optimized and ready to boost your store.`
  }));
  return { batch_id, items };
}

export async function mockDownload(_batchId: string): Promise<Blob> {
  await wait(400);
  return new Blob([JSON.stringify({ ok: true })], { type: "application/json" });
}
