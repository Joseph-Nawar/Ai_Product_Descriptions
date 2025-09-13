import { GeneratedItem } from "../types";
import { toCsv, download } from "../utils/csv";
import { Button } from "./UI";

type Props = { items: GeneratedItem[]; batchId: string };

export default function ExportButtons({ items, batchId }: Props) {
  const handleCsv = () => {
    const csv = toCsv(items);
    const blob = new Blob(["\uFEFF", csv], { type: "text/csv;charset=utf-8" });
    download(`descriptions_${batchId}.csv`, blob);
  };

  const handleJson = () => {
    const blob = new Blob([JSON.stringify(items, null, 2)], { type: "application/json" });
    download(`descriptions_${batchId}.json`, blob);
  };

  return (
    <div className="flex flex-wrap gap-3">
      <Button 
        onClick={handleCsv}
        className="px-6 py-3 bg-gradient-to-r from-emerald-500 to-green-500 hover:from-emerald-600 hover:to-green-600"
      >
        <span className="flex items-center gap-2">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Export CSV
        </span>
      </Button>
      <Button 
        onClick={handleJson}
        className="px-6 py-3 bg-gradient-to-r from-purple-500 to-indigo-500 hover:from-purple-600 hover:to-indigo-600"
      >
        <span className="flex items-center gap-2">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
          </svg>
          Export JSON
        </span>
      </Button>
    </div>
  );
}
