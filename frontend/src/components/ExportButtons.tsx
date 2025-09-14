import React from "react";
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
    <div className="flex flex-wrap gap-4">
      <Button 
        onClick={handleCsv}
        className="bg-gradient-to-r from-accent-success to-green-400"
      >
        <span className="flex items-center gap-2">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
          </svg>
          Export CSV
        </span>
      </Button>
      <Button 
        onClick={handleJson}
        className="bg-gradient-to-r from-secondary to-purple-400"
      >
        <span className="flex items-center gap-2">
           <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
          </svg>
          Export JSON
        </span>
      </Button>
    </div>
  );
}