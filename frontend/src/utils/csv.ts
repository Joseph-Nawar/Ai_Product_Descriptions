import Papa from "papaparse";
import { GeneratedItem, ProductInput } from "../types";

export function parseProductsCsv(file: File): Promise<ProductInput[]> {
  return new Promise((resolve, reject) => {
    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: (results: any) => {
        // Define synonyms for automatic mapping
        const productNameSynonyms = ['title', 'name', 'product', 'productname', 'item', 'model'];
        const categorySynonyms = ['category', 'type', 'department', 'group', 'collection'];
        
        // Blocklist for columns that shouldn't be used as features
        const featureBlocklist = ['id', 'sku', 'price', 'cost', 'url', 'image', 'images'];
        
        const findColumn = (columns: string[], synonyms: string[]): string | null => {
          const normalizedColumns: { [key: string]: string } = {};
          for (const col of columns) {
            const normalized = col.toLowerCase().replace(/[\s\-_]/g, '');
            normalizedColumns[normalized] = col;
          }
          
          for (const synonym of synonyms) {
            const normalizedSynonym = synonym.toLowerCase().replace(/[\s\-_]/g, '');
            if (normalizedSynonym in normalizedColumns) {
              return normalizedColumns[normalizedSynonym];
            }
          }
          return null;
        };
        
        const columns = results.meta.fields || [];
        const productNameCol = findColumn(columns, productNameSynonyms) || columns[0] || 'Unknown';
        const categoryCol = findColumn(columns, categorySynonyms) || 'General';
        
        // Generate features from all other columns
        const cleaned = (results.data as any[]).map((row, index) => {
          const productName = String(row[productNameCol] || "").trim();
          const category = String(row[categoryCol] || "").trim() || "General";
          
          // Build features from other columns
          const featureParts: string[] = [];
          for (const col of columns) {
            if (col !== productNameCol && col !== categoryCol && 
                !featureBlocklist.includes(col.toLowerCase())) {
              const value = String(row[col] || "").trim();
              if (value) {
                featureParts.push(`${col}: ${value}`);
              }
            }
          }
          const features = featureParts.join('. ');
          
          return {
            id: String(row.id || `row_${index}`).trim(),
            product_name: productName,
            category: category.toLowerCase(),
            features: features,
            audience: String(row.audience || "").trim(), // Will be overridden by parent component
            keywords: row.keywords ? String(row.keywords).trim() : undefined
          };
        }).filter(r => r.product_name); // Only filter out rows with no product name
        
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
