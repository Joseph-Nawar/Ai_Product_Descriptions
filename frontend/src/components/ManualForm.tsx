import { useState } from "react";
import { Input, Textarea, Button } from "./UI";
import { ProductInput } from "../types";

type Props = { onAdd: (row: ProductInput) => void };

export default function ManualForm({ onAdd }: Props) {
  const [form, setForm] = useState<ProductInput>({
    product_name: "",
    category: "",
    features: "",
    audience: "",
    keywords: ""
  });

  function update<K extends keyof ProductInput>(k: K, v: ProductInput[K]) {
    setForm(prev => ({ ...prev, [k]: v }));
  }

  return (
    <div className="grid gap-3">
      <Input placeholder="Product name" value={form.product_name} onChange={e => update("product_name", e.target.value)} />
      <Input placeholder="Category" value={form.category} onChange={e => update("category", e.target.value)} />
      <Textarea placeholder="Features (comma or newline separated)" value={form.features} onChange={e => update("features", e.target.value)} />
      <Input placeholder="Target audience" value={form.audience} onChange={e => update("audience", e.target.value)} />
      <Input placeholder="Keywords (optional)" value={form.keywords || ""} onChange={e => update("keywords", e.target.value)} />
      <div><Button onClick={() => onAdd(form)} disabled={!form.product_name || !form.category || !form.features || !form.audience}>Add to Batch</Button></div>
    </div>
  );
}
