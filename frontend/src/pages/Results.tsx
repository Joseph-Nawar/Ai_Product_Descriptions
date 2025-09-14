import React, { useState, useEffect } from "react";
import { useLocation, useNavigate, useSearchParams } from "react-router-dom";
import EditableTable from "../components/EditableTable";
import ExportButtons from "../components/ExportButtons";
import AnalysisPanel from "../components/AnalysisPanel";
import { Banner, Button } from "../components/UI";
import { BatchResponse, GeneratedItem } from "../types";
import { fetchBatch, regenerateDescription } from "../api/generate";
import { handleApiError } from "../api/client";

export default function Results() {
  const navigate = useNavigate();
  const location = useLocation();
  const [search] = useSearchParams();
  const batchIdFromUrl = search.get("batch_id") || undefined;
  const state = (location.state || {}) as Partial<BatchResponse & { errors?: any[] }>;
  
  const [items, setItems] = useState<GeneratedItem[]>(state.items || []);
  const [error, setError] = useState<string | null>(null);
  const [selectedItem, setSelectedItem] = useState<GeneratedItem | null>(null);

  useEffect(() => {
    // Select the first item by default when data loads
    if (items.length > 0 && !selectedItem) {
      setSelectedItem(items[0]);
    }
  }, [items, selectedItem]);
  
  const handleRegenerate = async (itemToRegenerate: GeneratedItem) => {
    // Set loading state for the specific item
    setItems((currentItems: GeneratedItem[]) => currentItems.map(item => 
      item.id === itemToRegenerate.id ? { ...item, regenerating: true } : item
    ));

    try {
      const regeneratedItem = await regenerateDescription(itemToRegenerate); // Mocked API call
      // Update the specific item with new data and remove loading state
      setItems((currentItems: GeneratedItem[]) => currentItems.map(item => 
        item.id === itemToRegenerate.id ? { ...regeneratedItem, regenerating: false } : item
      ));
      // If the regenerated item was the selected one, update the panel too
      if (selectedItem?.id === itemToRegenerate.id) {
        setSelectedItem(regeneratedItem);
      }
    } catch (e) {
      setError(handleApiError(e));
      // Remove loading state on error
       setItems((currentItems: GeneratedItem[]) => currentItems.map(item => 
        item.id === itemToRegenerate.id ? { ...item, regenerating: false } : item
      ));
    }
  };

  useEffect(() => {
    async function ensureData() {
      if (location.state) {
        setItems(state.items || []);
        if (state.errors && state.errors.length > 0) {
          setError(`Generation completed with some errors.`);
        }
        return;
      }

      if (batchIdFromUrl) {
        try {
          const res = await fetchBatch(batchIdFromUrl);
          setItems(res.items);
          setError(null);
        } catch (e: any) {
          setError(handleApiError(e));
        }
      } else if (!items.length) {
        setError("No generation data found. Please start a new batch.");
      }
    }
    ensureData();
  }, [state, batchIdFromUrl, location.state, items.length]);

  return (
    <div className="mx-auto max-w-screen-2xl p-4 space-y-8 animate-fade-in">
      <div className="bg-gray-900 rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="space-y-1">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-accent-emerald to-accent-cyan bg-clip-text text-transparent">
              Your AI Descriptions are Ready
            </h1>
            <p className="text-gray-400">
              {items.length} descriptions generated. Edit below and export your results.
            </p>
          </div>
          <Button onClick={() => navigate("/")} variant="secondary">New Batch</Button>
        </div>
      </div>

      {error && <Banner type="error">{error}</Banner>}

      {!error && items.length > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 space-y-8">
            <div className="bg-gray-900 rounded-2xl border border-glass-border shadow-2xl shadow-black/20 overflow-hidden">
              <EditableTable 
                data={items} 
                onChange={setItems} 
                onRowSelect={setSelectedItem}
                selectedRowId={selectedItem?.id}
                onRegenerate={handleRegenerate}
              />
            </div>
            <div className="bg-gray-900 rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20">
              <h3 className="text-xl font-semibold text-gray-100 mb-4">Export Results</h3>
              <ExportButtons items={items} batchId={state.batch_id || batchIdFromUrl || "local"} />
            </div>
          </div>
          <div className="lg:col-span-1">
            <AnalysisPanel item={selectedItem} />
          </div>
        </div>
      )}
    </div>
  );
}