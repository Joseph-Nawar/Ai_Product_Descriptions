import { useEffect, useState } from "react";
import { useLocation, useNavigate, useSearchParams } from "react-router-dom";
import EditableTable from "../components/EditableTable";
import ExportButtons from "../components/ExportButtons";
import { Banner, Button } from "../components/UI";
import { BatchResponse, GeneratedItem } from "../types";
import { fetchBatch } from "../api/generate";
import { handleApiError } from "../api/client";

export default function Results() {
  const navigate = useNavigate();
  const location = useLocation();
  const [search] = useSearchParams();
  const batchIdFromUrl = search.get("batch_id") || undefined;
  const state = (location.state || {}) as BatchResponse;
  const [items, setItems] = useState<GeneratedItem[]>(state.items || []);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function ensureData() {
      
      // If we have state data, use it (even if items is empty)
      if (state) {
        setItems(state.items || []);
        
        // Show errors if there are any
        if (state.errors && state.errors.length > 0) {
          const errorMessages = state.errors.map((err: any) => err.error || err.message || 'Unknown error').join(', ');
          setError(`Generation completed with errors: ${errorMessages}`);
        }
        return;
      }

      // If we have a batch_id in the URL but no state, try fetching from the backend.
      if (batchIdFromUrl) {
        try {
          const res = await fetchBatch(batchIdFromUrl);
          setItems(res.items);
          setError(null);
          return;
        } catch (e: any) {
          setError(handleApiError(e));
        }
      } else {
        setError("Missing batch data. Please generate again.");
      }
    }
    ensureData();
  }, [state, batchIdFromUrl]);


  return (
    <div className="mx-auto max-w-7xl p-8 space-y-8">
      {/* Header Section */}
      <div className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 p-6 shadow-lg">
        <div className="flex items-center justify-between">
          <div className="space-y-2">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-green-600 to-emerald-600 bg-clip-text text-transparent">
                Generated Descriptions
              </h1>
            </div>
            <p className="text-gray-600">
              {items.length} AI-generated product descriptions ready for editing and export
            </p>
          </div>
          <Button 
            onClick={() => navigate("/")} 
            className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700"
          >
            <span className="flex items-center gap-2">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              New Batch
            </span>
          </Button>
        </div>
      </div>

      {error && <Banner type="error">{error}</Banner>}

      {!error && (
        <>
          {/* Table Section */}
          <div className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 shadow-lg overflow-hidden">
            <EditableTable data={items} onChange={setItems} />
          </div>
          
          {/* Export Actions */}
          <div className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 p-6 shadow-lg">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-800">Export Options</h3>
              <div className="text-sm text-gray-500">
                {items.length} descriptions ready
              </div>
            </div>
            <div className="flex flex-wrap gap-4">
              <ExportButtons items={items} batchId={state.batch_id || "local"} />
            </div>
          </div>
        </>
      )}
    </div>
  );
}
