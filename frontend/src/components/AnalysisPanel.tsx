import React from 'react';
import { GeneratedItem } from '../types';
import { calculateWordCount, getReadabilityScore, checkKeywords, getSentiment } from '../utils/analysis';

type Props = {
  item: GeneratedItem | null;
};

export default function AnalysisPanel({ item }: Props) {
  if (!item) {
    return (
      <div className="sticky top-28 bg-glass-bg backdrop-blur-xl rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20 text-center text-gray-400">
        Select a row to see its analysis.
      </div>
    );
  }

  const wordCount = calculateWordCount(item.description);
  const readability = getReadabilityScore(item.description);
  const keywords = checkKeywords(item.description, item.keywords);
  const sentiment = getSentiment(item.description);

  return (
    <div className="sticky top-28 space-y-6 bg-glass-bg backdrop-blur-xl rounded-2xl border border-glass-border p-6 shadow-2xl shadow-black/20 animate-fade-in">
      <div>
        <h3 className="text-lg font-semibold text-white mb-1">Live Analysis</h3>
        <p className="text-sm text-gray-400 truncate">For: <span className="font-medium text-gray-300">{item.product_name}</span></p>
      </div>

      <div className="grid grid-cols-2 gap-4 text-center">
        <MetricCard label="Word Count" value={wordCount} />
        <MetricCard label="Readability" value={readability} />
      </div>

      <AnalysisSection title="SEO Keywords">
        {keywords.found.length === 0 && keywords.missing.length === 0 ? (
          <p className="text-sm text-gray-400">No keywords provided.</p>
        ) : (
          <div className="space-y-2">
            <div>
              <h4 className="text-sm font-medium text-emerald-400 mb-1">Found ({keywords.found.length})</h4>
              <div className="flex flex-wrap gap-1.5">
                {keywords.found.map(k => <Badge key={k} color="emerald">{k}</Badge>)}
              </div>
            </div>
            <div>
              <h4 className="text-sm font-medium text-red-400 mb-1">Missing ({keywords.missing.length})</h4>
              <div className="flex flex-wrap gap-1.5">
                {keywords.missing.map(k => <Badge key={k} color="red">{k}</Badge>)}
              </div>
            </div>
          </div>
        )}
      </AnalysisSection>

      <AnalysisSection title="Sentiment Analysis">
        <div className="w-full bg-gray-700 rounded-full h-2.5">
            <div 
              className="bg-gradient-to-r from-sky-400 to-emerald-400 h-2.5 rounded-full transition-all duration-500" 
              style={{ width: `${(sentiment.score + 5) * 10}%` }}
            ></div>
        </div>
        <p className="text-center text-sm font-medium mt-2 text-gray-300">{sentiment.label}</p>
      </AnalysisSection>
    </div>
  );
}

const MetricCard = ({ label, value }: { label: string, value: string | number }) => (
  <div className="bg-black/20 border border-glass-border rounded-lg p-3">
    <div className="text-2xl font-bold text-white">{value}</div>
    <div className="text-xs text-gray-400 uppercase tracking-wider">{label}</div>
  </div>
);

const AnalysisSection = ({ title, children }: { title: string, children: React.ReactNode }) => (
  <div>
    <h3 className="text-md font-semibold text-white mb-3 border-b border-glass-border pb-2">{title}</h3>
    {children}
  </div>
);

const Badge = ({ color, children }: { color: 'emerald' | 'red'; children: React.ReactNode }) => {
  const colors = {
    emerald: 'bg-emerald-500/20 text-emerald-300',
    red: 'bg-red-500/20 text-red-300',
  };
  return <span className={`px-2 py-0.5 text-xs font-medium rounded-full ${colors[color]}`}>{children}</span>;
};