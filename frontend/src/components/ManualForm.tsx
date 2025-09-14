import React, { useState } from "react";
import { Input, Textarea, Button, Tooltip } from "./UI";
import { ProductInput } from "../types";

type Props = { onAdd: (row: ProductInput) => void };

const initialFormState: ProductInput = {
  product_name: "", category: "", features: "", audience: "", keywords: ""
};

export default function ManualForm({ onAdd }: Props) {
  const [form, setForm] = useState<ProductInput>(initialFormState);

  const update = <K extends keyof ProductInput>(k: K, v: ProductInput[K]) => setForm(p => ({ ...p, [k]: v }));

  const handleAdd = () => {
    onAdd(form);
    setForm(initialFormState);
  };

  return (
    <div className="grid gap-4">
      <Input placeholder="Product Name*" value={form.product_name} onChange={e => update("product_name", e.target.value)} />
      <Input placeholder="Category*" value={form.category} onChange={e => update("category", e.target.value)} />
      <Textarea placeholder="Key Features (e.g., Waterproof, 12-hour battery, Bluetooth 5.0)*" value={form.features} onChange={e => update("features", e.target.value)} />
      <Input placeholder="Target Audience (e.g., Tech Enthusiasts, Hikers, Students)*" value={form.audience} onChange={e => update("audience", e.target.value)} />
      <div className="flex items-center gap-2">
        <Input placeholder="SEO Keywords (optional, comma-separated)" value={form.keywords || ""} onChange={e => update("keywords", e.target.value)} />
        <Tooltip text="Keywords help the AI focus on specific terms for SEO.">
          <span className="text-gray-400 cursor-help">?</span>
        </Tooltip>
      </div>
      <Button onClick={handleAdd} disabled={!form.product_name || !form.category || !form.features || !form.audience}>
        Add to Batch
      </Button>
    </div>
  );
}