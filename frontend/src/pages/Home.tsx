import React, { useState } from "react";
import { useTranslation } from "react-i18next";
import FileUpload from "../components/FileUpload";
import ManualForm from "../components/ManualForm";
import ChoiceCards from "../components/ChoiceCards";
import ToneSelector from "../components/ToneSelector";
import StyleSelector from "../components/StyleSelector";
import LanguageSelector from "../components/LanguageSelector";
import ProductGenieLogo from "../components/ProductGenieLogo";
import { UpgradePrompt } from "../components/UpgradePrompt";
import { Button, Banner, Spinner, StatusAnnouncer } from "../components/UI";
import { ProductInput } from "../types";
import { generateDescriptions } from "../api/generate";
import { handleApiError } from "../api/client";
import { useNavigate } from "react-router-dom";
import { usePaymentContext } from "../contexts/PaymentContext";
import { DEFAULT_LANGUAGE } from "../constants/languages";

export default function Home() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
  const [batch, setBatch] = useState<ProductInput[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [batchTone, setBatchTone] = useState<string>("professional");
  const [batchStyle, setBatchStyle] = useState<string>("amazon");
  const [batchLanguage, setBatchLanguage] = useState<string>(DEFAULT_LANGUAGE);
  const [showManualForm, setShowManualForm] = useState(false);
  const navigate = useNavigate();

  function addRows(rows: ProductInput[]) { 
    setBatch(prev => [...prev, ...rows]); 
  }
  function addRow(row: ProductInput) { 
    setBatch(prev => [...prev, row]); 
    setShowManualForm(false);
  }
  function clearBatch() { setBatch([]); }

  async function handleGenerate() {
    setError(null);
    
    // Check if user has enough credits
    const creditsNeeded = batch.length;
    if (!payment.canGenerate(creditsNeeded)) {
      setError("Insufficient credits. Please upgrade your plan or purchase more credits.");
      payment.setShowUpgradePrompt(true);
      return;
    }

    // Try to consume credits
    const canProceed = await payment.handleGeneration(creditsNeeded);
    if (!canProceed) {
      setError("Unable to process generation. Please check your credit balance.");
      return;
    }

    setLoading(true);
    try {
      const batchRequest = {
        products: batch,
        batchTone: batchTone,
        batchStyle: batchStyle,
        languageCode: batchLanguage
      };
      const res = await generateDescriptions(batchRequest);
      navigate(`/results?batch_id=${encodeURIComponent(res.batch_id)}`, { state: res });
    } catch (e: any) {
      setError(handleApiError(e));
      // Refund credits on error
      if (payment.creditBalance) {
        payment.updateCredits(payment.creditBalance.current_credits + creditsNeeded, 'set');
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto max-w-7xl p-4 space-y-12 animate-fade-in">
      {/* Hero Section */}
      <section className="text-center py-16 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tighter">
          <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
            {t('pageTitles.dashboard')}
          </span>
        </h1>
        <p className="mt-6 text-lg text-gray-400 max-w-2xl mx-auto">
          {t('hero.subtitle')}
        </p>
      </section>

      {error && <Banner type="error">{error}</Banner>}

      {/* Upgrade Prompt */}
      <UpgradePrompt 
        threshold={75}
        variant="banner"
        onUpgrade={() => navigate('/pricing')}
      />

      {/* Batch Style Configuration - Always Visible */}
      <section className="animate-slide-in relative z-[99997]" style={{ animationDelay: '200ms' }}>
        <GlassPanel icon="style" title={t('sections.styleConfiguration.title')}>
          <div className="space-y-6">
            {batch.length > 0 ? (
              <>
                <p className="text-gray-400 text-sm">{t('sections.styleConfiguration.description')}</p>
                
                <div className="grid gap-6 md:grid-cols-3">
                  <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-300">{t('sections.styleConfiguration.brandVoice')} *</label>
                    <ToneSelector value={batchTone} onChange={setBatchTone} />
                    <p className="text-xs text-gray-400">{t('sections.styleConfiguration.brandVoiceDescription')}</p>
                  </div>
                  
                  <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-300">{t('sections.styleConfiguration.platformStyle')} *</label>
                    <StyleSelector value={batchStyle} onChange={setBatchStyle} />
                    <p className="text-xs text-gray-400">{t('sections.styleConfiguration.platformStyleDescription')}</p>
                  </div>

                  <div className="space-y-2">
                    <LanguageSelector 
                      value={batchLanguage} 
                      onChange={setBatchLanguage}
                      showNativeNames={true}
                    />
                  </div>
                </div>
              </>
            ) : (
              <>
                <div className="text-center space-y-4">
                  <div className="w-16 h-16 mx-auto bg-gradient-to-br from-primary/20 to-secondary/20 rounded-2xl flex items-center justify-center">
                    <svg className="w-8 h-8 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM21 5a2 2 0 00-2-2h-4a2 2 0 00-2 2v12a4 4 0 004 4h4a2 2 0 002-2V5z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-semibold text-gray-100">{t('sections.getStarted.chooseVoice')}</h3>
                  <p className="text-gray-400 max-w-md mx-auto">
                    {t('sections.getStarted.description')}
                  </p>
                </div>
                
                <div className="grid gap-6 md:grid-cols-3">
                  <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-300">{t('sections.styleConfiguration.brandVoice')} *</label>
                    <ToneSelector value={batchTone} onChange={setBatchTone} />
                    <p className="text-xs text-gray-400">Choose the voice and personality for your descriptions</p>
                  </div>
                  
                  <div className="space-y-2">
                    <label className="text-sm font-medium text-gray-300">{t('sections.styleConfiguration.platformStyle')} *</label>
                    <StyleSelector value={batchStyle} onChange={setBatchStyle} />
                    <p className="text-xs text-gray-400">Select platform-specific writing style (Amazon, Etsy, Shopify, eBay)</p>
                  </div>

                  <div className="space-y-2">
                    <LanguageSelector 
                      value={batchLanguage} 
                      onChange={setBatchLanguage}
                      showNativeNames={true}
                    />
                  </div>
                </div>
                
                <div className="bg-gradient-to-r from-primary/10 to-secondary/10 border border-primary/20 rounded-xl p-4">
                  <div className="flex items-start gap-3">
                    <svg className="w-5 h-5 text-primary mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <div>
                      <p className="text-sm text-gray-200 font-medium mb-1">{t('sections.getStarted.readyToGrant')}</p>
                      <p className="text-xs text-gray-400">
                        {t('sections.getStarted.addProducts')}
                      </p>
                    </div>
                  </div>
                </div>
              </>
            )}
          </div>
        </GlassPanel>
      </section>

      {/* Input Methods Section - Only show when batch has products */}
      {batch.length > 0 && (
        <section className="grid gap-8 lg:grid-cols-2 animate-slide-in relative z-[1]" style={{ animationDelay: '300ms' }}>
          <GlassPanel icon="upload" title={t('sections.inputMethods.uploadMore')}>
            <p className="text-gray-400 text-sm mb-4">{t('sections.inputMethods.uploadMoreDescription')}</p>
            <FileUpload onParsed={addRows} />
          </GlassPanel>
          <GlassPanel icon="add" title={t('sections.inputMethods.addMore')}>
            <p className="text-gray-400 text-sm mb-4">{t('sections.inputMethods.addMoreDescription')}</p>
            <ManualForm onAdd={addRow} />
          </GlassPanel>
        </section>
      )}

      {/* Choice Cards - Only show when batch is empty */}
      {batch.length === 0 && (
        <section className="animate-slide-in" style={{ animationDelay: '300ms' }}>
          <GlassPanel icon="start" title={t('sections.getStarted.title')}>
            <ChoiceCards 
              onParsed={addRows} 
              onManualAdd={() => setShowManualForm(true)} 
            />
          </GlassPanel>
        </section>
      )}

      {/* Batch Preview Section */}
      <section className="animate-slide-in relative z-[1]" style={{ animationDelay: '400ms' }}>
        <GlassPanel icon="batch" title={t('sections.productWishlist.title')} count={batch.length}>
          <div className="rounded-xl border border-glass-border p-4 bg-gray-900 max-h-80 overflow-y-auto">
            {batch.length > 0 ? (
              <div className="space-y-3">
                {batch.map((b, i) => (
                  <div key={i} className="flex items-center justify-between gap-4 p-3 bg-white/5 rounded-lg border border-glass-border">
                    <div className="font-medium text-gray-200 truncate">{b.product_name}</div>
                    <div className="text-sm text-gray-400 flex items-center space-x-2 flex-shrink-0">
                      <span className="px-2 py-0.5 bg-primary/20 text-primary rounded-full text-xs font-medium">{b.category}</span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                <svg className="w-16 h-16 mx-auto mb-4 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c.251.023.501.05.75.082a.75.75 0 01.75.75v5.714a2.25 2.25 0 00.659 1.591L14.25 14.5M14.25 14.5L19 9.75M14.25 14.5L19 19.25M12 21a9 9 0 110-18 9 9 0 010 18z" /></svg>
                <h3 className="text-lg font-semibold text-gray-300">{t('sections.productWishlist.empty')}</h3>
                <p className="mt-1">{t('sections.productWishlist.emptyDescription')}</p>
              </div>
            )}
          </div>
          {batch.length > 0 && <Button variant="tertiary" onClick={clearBatch} className="mt-4">{t('sections.productWishlist.clearWishlist')}</Button>}
        </GlassPanel>
      </section>

      {/* Generate Button */}
      <div className="flex justify-center pt-6 animate-slide-in" style={{ animationDelay: '500ms' }}>
        <div className="text-center space-y-4">
          <Button 
            onClick={handleGenerate} 
            disabled={!batch.length || loading || !batchTone || !batchStyle} 
            glowing={!loading && batch.length > 0 && !!batchTone && !!batchStyle} 
            className={`px-10 py-5 text-xl font-bold min-w-[300px] transition-all duration-300 ${
              !batch.length ? 'opacity-50' : ''
            }`}
          >
            {loading ? ( 
              <span className="flex items-center justify-center gap-3">
                <Spinner /> {t('buttons.generating')}
              </span> 
            ) : batch.length > 0 ? (
              `${t('buttons.generate')} (${batch.length})`
            ) : (
              <span className="flex items-center justify-center gap-2">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                {t('buttons.addProducts')}
              </span>
            )}
          </Button>
          
          {/* Credit Cost Indicator */}
          {batch.length > 0 && (
            <div className="text-center">
              <div className="text-sm text-gray-400">
                This will cost <span className="font-semibold text-primary">{batch.length} credit{batch.length !== 1 ? 's' : ''}</span>
              </div>
              {payment.creditBalance && (
                <div className="text-xs text-gray-500 mt-1">
                  You have {payment.creditBalance.current_credits} credits remaining
                </div>
              )}
            </div>
          )}
        </div>
      </div>
      <StatusAnnouncer message={loading ? t('buttons.generating') : error ? `Error: ${error}` : "Ready"} />

      {/* Manual Form Modal */}
      {showManualForm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-[99999]">
          <div className="bg-gray-900 rounded-2xl border border-glass-border p-6 w-full max-w-2xl max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold text-gray-100">{t('modals.addProduct.title')}</h2>
              <button
                onClick={() => setShowManualForm(false)}
                className="text-gray-400 hover:text-gray-200 transition-colors"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <ManualForm onAdd={addRow} />
          </div>
        </div>
      )}
    </div>
  );
}

// Helper component for consistent panel styling
const GlassPanel = ({ icon, title, count, children }: { icon: string; title: string; count?: number; children: React.ReactNode }) => {
  const icons: { [key: string]: React.ReactNode } = {
    upload: <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>,
    add: <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>,
    batch: <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0l2-2m-2 2l-2-2" /></svg>,
    style: <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM21 5a2 2 0 00-2-2h-4a2 2 0 00-2 2v12a4 4 0 004 4h4a2 2 0 002-2V5z" /></svg>,
    start: <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>,
  };

  return (
    <div className="bg-gray-900 rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20 relative z-[99996]">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-gradient-to-br from-primary/20 to-secondary/20 rounded-xl flex items-center justify-center text-primary">{icons[icon]}</div>
          <h2 className="text-xl font-semibold text-gray-100">{title}</h2>
        </div>
        {typeof count !== 'undefined' && (
          <span className="px-3 py-1 bg-secondary/20 text-secondary rounded-full text-sm font-bold">{count}</span>
        )}
      </div>
      {children}
    </div>
  );
};