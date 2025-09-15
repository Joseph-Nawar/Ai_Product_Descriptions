import React, { useRef } from 'react';
import { useTranslation } from 'react-i18next';
import { parseProductsCsv } from '../utils/csv';
import { ProductInput } from '../types';
import { Button } from './UI';

type Props = {
  onParsed: (rows: ProductInput[]) => void;
  onManualAdd: () => void;
};

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

export default function ChoiceCards({ onParsed, onManualAdd }: Props) {
  const { t } = useTranslation();
  const inputRef = useRef<HTMLInputElement | null>(null);
  const [audience, setAudience] = React.useState("");

  async function handleFile(f: File) {
    try {
      // Check file size
      if (f.size > MAX_FILE_SIZE) {
        throw new Error(`File too large. Maximum size is ${MAX_FILE_SIZE / (1024 * 1024)}MB.`);
      }
      
      // Check file type
      if (!f.name.toLowerCase().endsWith('.csv')) {
        throw new Error('Please select a CSV file.');
      }
      
      // Check if audience is provided
      if (!audience.trim()) {
        throw new Error('Please provide a target audience.');
      }
      
      const rows = await parseProductsCsv(f);
      // Apply the target audience to all products
      const rowsWithAudience = rows.map(row => ({
        ...row,
        audience: audience.trim()
      }));
      onParsed(rowsWithAudience);
    } catch (e: any) {
      alert(e.message || 'Failed to parse CSV file.');
    } finally {
      if (inputRef.current) inputRef.current.value = "";
    }
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-100 mb-2">{t('choiceCards.title')}</h2>
        <p className="text-gray-400">{t('choiceCards.subtitle')}</p>
      </div>

      {/* Choice Cards */}
      <div className="grid gap-6 md:grid-cols-2">
        {/* CSV Upload Card */}
        <div className="group cursor-pointer">
          <div className="bg-gray-800 border-2 border-gray-600 rounded-2xl p-8 text-center transition-all duration-300 hover:border-blue-500 hover:bg-gray-750 hover:shadow-lg hover:shadow-blue-500/20">
            <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
              <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            
            <h3 className="text-xl font-semibold text-gray-100 mb-2">{t('choiceCards.csvUpload.title')}</h3>
            <p className="text-gray-400 mb-6">
              {t('choiceCards.csvUpload.description')}
            </p>
            
            <div className="space-y-3">
              <div>
                <label htmlFor="audience" className="block text-sm font-medium text-gray-300 mb-1">
                  {t('choiceCards.csvUpload.targetAudience')} *
                </label>
                <input
                  id="audience"
                  type="text"
                  value={audience}
                  onChange={(e) => setAudience(e.target.value)}
                  placeholder={t('choiceCards.csvUpload.audiencePlaceholder')}
                  className="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-lg text-gray-100 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  required
                />
              </div>
              
              <input
                ref={inputRef}
                type="file"
                accept=".csv"
                onChange={(e) => {
                  const file = e.target.files?.[0];
                  if (file) {
                    handleFile(file);
                  }
                }}
                className="hidden"
              />
              <Button 
                onClick={() => inputRef.current?.click()} 
                className="w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800"
              >
                {t('choiceCards.csvUpload.button')}
              </Button>
              
              <div className="text-xs text-gray-500 bg-gray-900/50 rounded-lg p-3">
                <div className="font-medium text-gray-300 mb-1">{t('choiceCards.csvUpload.smartProcessing.title')}</div>
                <div>{t('choiceCards.csvUpload.smartProcessing.description')}</div>
                <div className="mt-1 text-gray-400">{t('choiceCards.csvUpload.smartProcessing.maxSize')}</div>
              </div>
            </div>
          </div>
        </div>

        {/* Manual Entry Card */}
        <div className="group cursor-pointer">
          <div className="bg-gray-800 border-2 border-gray-600 rounded-2xl p-8 text-center transition-all duration-300 hover:border-purple-500 hover:bg-gray-750 hover:shadow-lg hover:shadow-purple-500/20">
            <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
              <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
            </div>
            
            <h3 className="text-xl font-semibold text-gray-100 mb-2">{t('choiceCards.manualEntry.title')}</h3>
            <p className="text-gray-400 mb-6">
              {t('choiceCards.manualEntry.description')}
            </p>
            
            <div className="space-y-3">
              <Button 
                onClick={onManualAdd}
                className="w-full bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-700 hover:to-purple-800"
              >
                {t('choiceCards.manualEntry.button')}
              </Button>
              
              <div className="text-xs text-gray-500 bg-gray-900/50 rounded-lg p-3">
                <div className="font-medium text-gray-300 mb-1">{t('choiceCards.manualEntry.perfectFor.title')}</div>
                <div>• {t('choiceCards.manualEntry.perfectFor.testing')}</div>
                <div>• {t('choiceCards.manualEntry.perfectFor.adding')}</div>
                <div>• {t('choiceCards.manualEntry.perfectFor.precision')}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Help Text */}
      <div className="text-center">
        <div className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-primary/10 to-secondary/10 border border-primary/20 rounded-xl">
          <svg className="w-4 h-4 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span className="text-sm text-gray-300">
            {t('choiceCards.helpText')}
          </span>
        </div>
      </div>
    </div>
  );
}
