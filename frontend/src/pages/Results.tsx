import React, { useState, useEffect, Suspense } from "react";
import { useLocation, useNavigate, useSearchParams } from "react-router-dom";
import { useTranslation } from "react-i18next";
import ExportButtons from "../components/ExportButtons";
import AnalysisPanel from "../components/AnalysisPanel";
import { UpgradePrompt } from "../components/UpgradePrompt";
import { Banner, Button } from "../components/UI";
import { BatchResponse, GeneratedItem } from "../types";
import { fetchBatch, regenerateDescription } from "../api/generate";
import { handleApiError } from "../api/client";
import { usePaymentContext } from "../contexts/PaymentContext";

// Lazy load the heavy EditableTable component
const EditableTable = React.lazy(() => import("../components/EditableTable"));

// Loading fallback for the table
const TableLoadingFallback = () => (
  <div className="bg-gray-900 rounded-2xl border border-glass-border shadow-2xl shadow-black/20 overflow-hidden">
    <div className="p-8 flex items-center justify-center">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      <span className="ml-3 text-gray-400">Loading table...</span>
    </div>
  </div>
);

export default function Results() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
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
    // Check if user has enough credits for regeneration
    const creditsNeeded = 1;
    if (!payment.canGenerate(creditsNeeded)) {
      setError("Insufficient credits to regenerate. Please upgrade your plan or purchase more credits.");
      payment.setShowUpgradePrompt(true);
      return;
    }

    // Try to consume credits
    const canProceed = await payment.handleGeneration(creditsNeeded);
    if (!canProceed) {
      setError("Unable to process regeneration. Please check your credit balance.");
      return;
    }

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
      // Refund credits on error
      if (payment.creditBalance) {
        payment.updateCredits(payment.creditBalance.current_credits + creditsNeeded, 'set');
      }
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
            <h1 className="text-4xl font-bold bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
              {t('pageTitles.results')}
            </h1>
            <p className="text-gray-400">
              {items.length} {t('results.descriptionsGenerated')}
            </p>
          </div>
          <Button onClick={() => navigate("/")} variant="secondary">{t('navigation.newCatalog')}</Button>
        </div>
      </div>

      {error && <Banner type="error">{error}</Banner>}

      {/* Upgrade Prompt */}
      <UpgradePrompt 
        threshold={75}
        variant="banner"
        onUpgrade={() => navigate('/pricing')}
      />

      {!error && items.length > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 space-y-8">
            <Suspense fallback={<TableLoadingFallback />}>
              <EditableTable 
                data={items} 
                onChange={setItems} 
                onRowSelect={setSelectedItem}
                selectedRowId={selectedItem?.id}
                onRegenerate={handleRegenerate}
              />
            </Suspense>
            <div className="bg-gray-900 rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20">
              <h3 className="text-xl font-semibold text-gray-100 mb-4">{t('results.exportResults')}</h3>
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