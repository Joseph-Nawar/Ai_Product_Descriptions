import Papa from "papaparse";
import { GeneratedItem, ProductInput } from "../types";

export function parseProductsCsv(file: File): Promise<ProductInput[]> {
  return new Promise((resolve, reject) => {
    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: (results: any) => {
        const cleaned = (results.data as any[]).map(row => ({
          product_name: String(row.product_name || row.title || "").trim(),
          category: String(row.category || "").trim(),
          features: String(row.features || "").trim(),
          audience: String(row.audience || "").trim(),
          keywords: row.keywords ? String(row.keywords).trim() : undefined
        })).filter(r => r.product_name && r.category && r.features && r.audience);
        resolve(cleaned);
      },
      error: (err: any) => reject(err)
    });
  });
}

export function toCsv(items: GeneratedItem[]): string {
  return Papa.unparse(items);
}

export function download(filename: string, blob: Blob) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}
