import { useState } from "react";
import FileUpload from "../components/FileUpload";
import ManualForm from "../components/ManualForm";
import { Button, Banner, Spinner, StatusAnnouncer } from "../components/UI";
import { ProductInput } from "../types";
import { generateDescriptions } from "../api/generate";
import { handleApiError } from "../api/client";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const [batch, setBatch] = useState<ProductInput[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  function addRows(rows: ProductInput[]) { setBatch(prev => [...prev, ...rows]); }
  function addRow(row: ProductInput) { addRows([row]); }
  function clearBatch() { setBatch([]); }

  async function handleGenerate() {
    setError(null);
    setLoading(true);
    try {
      // Prefer JSON array payload; backend may also accept CSV form-data
      const res = await generateDescriptions(batch);
      // Pass via navigation state and include batch_id in URL for durability
      navigate(`/results?batch_id=${encodeURIComponent(res.batch_id)}`, { state: res });
    } catch (e: any) {
      setError(handleApiError(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto max-w-7xl p-8 space-y-8">
      {/* Hero Section */}
      <div className="text-center space-y-6 py-8">
        <div className="space-y-4">
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-indigo-600 bg-clip-text text-transparent leading-tight">
            AI Product Description Generator
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Transform your e-commerce catalog with AI-powered, SEO-optimized product descriptions that convert visitors into customers.
          </p>
        </div>
        <div className="flex justify-center space-x-8 text-sm text-gray-500">
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <span>Batch Processing</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
            <span>SEO Optimized</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
            <span>Export Ready</span>
          </div>
        </div>
      </div>

      {error && <Banner type="error">{error}</Banner>}

      {/* Input Methods Section */}
      <section className="grid gap-8 lg:grid-cols-2">
        <div className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 p-6 shadow-lg hover:shadow-xl transition-shadow duration-300">
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
              </div>
              <h2 className="text-xl font-semibold text-gray-800">Upload CSV</h2>
            </div>
            <p className="text-gray-600 text-sm">Bulk upload your product catalog for efficient processing</p>
            <FileUpload onParsed={addRows} />
          </div>
        </div>
        <div className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 p-6 shadow-lg hover:shadow-xl transition-shadow duration-300">
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-xl flex items-center justify-center">
                <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <h2 className="text-xl font-semibold text-gray-800">Add Manually</h2>
            </div>
            <p className="text-gray-600 text-sm">Create individual product entries with custom details</p>
            <ManualForm onAdd={addRow} />
          </div>
        </div>
      </section>

      {/* Batch Preview Section */}
      <section className="bg-white/70 backdrop-blur-sm rounded-2xl border border-gray-200 p-6 shadow-lg">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-gradient-to-r from-orange-500 to-red-500 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">{batch.length}</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-800">Product Batch</h3>
          </div>
          <Button onClick={clearBatch} disabled={!batch.length} className="px-4 py-2 text-sm">
            Clear All
          </Button>
        </div>
        <div className="rounded-xl border-2 border-gray-100 p-4 bg-gray-50/50 max-h-64 overflow-y-auto">
          {batch.length ? (
            <div className="space-y-3">
              {batch.map((b, i) => (
                <div key={i} className="flex flex-col md:flex-row md:items-center gap-2 p-3 bg-white rounded-lg border border-gray-100 shadow-sm">
                  <div className="font-medium text-gray-800">{b.product_name}</div>
                  <div className="text-sm text-gray-500 flex items-center space-x-2">
                    <span className="px-2 py-1 bg-blue-100 text-blue-700 rounded-full text-xs">{b.category}</span>
                    <span>→</span>
                    <span>{b.audience}</span>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8 text-gray-500">
              <svg className="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
              </svg>
              <p className="text-lg font-medium">No products added yet</p>
              <p className="text-sm">Upload a CSV file or add products manually to get started</p>
            </div>
          )}
        </div>
      </section>

      {/* Generate Button */}
      <div className="flex justify-center">
        <Button 
          onClick={handleGenerate} 
          disabled={!batch.length || loading}
          className="px-8 py-4 text-lg font-semibold min-w-[200px]"
        >
          {loading ? (
            <span className="flex items-center gap-3">
              <Spinner />
              <span>Generating AI Descriptions...</span>
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Generate Descriptions
            </span>
          )}
        </Button>
      </div>

      <StatusAnnouncer 
        message={loading ? "Generating product descriptions..." : error ? `Error: ${error}` : batch.length > 0 ? `Ready to generate ${batch.length} product descriptions` : "No products added yet"} 
      />
    </div>
  );
}
