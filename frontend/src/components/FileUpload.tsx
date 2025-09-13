import { useRef, useState } from "react";
import { parseProductsCsv } from "../utils/csv";
import { ProductInput } from "../types";
import { Button, Banner } from "./UI";

type Props = { onParsed: (rows: ProductInput[]) => void };

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

export default function FileUpload({ onParsed }: Props) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement | null>(null);

  async function handleFile(f: File) {
    setError(null);
    setLoading(true);
    
    try {
      // Check file size
      if (f.size > MAX_FILE_SIZE) {
        throw new Error(`File too large. Maximum size is ${MAX_FILE_SIZE / (1024 * 1024)}MB.`);
      }
      
      // Check file type
      if (!f.name.toLowerCase().endsWith('.csv')) {
        throw new Error('Please select a CSV file.');
      }
      
      const rows = await parseProductsCsv(f);
      onParsed(rows);
    } catch (e: any) {
      setError(e.message || 'Failed to parse CSV file.');
    } finally {
      setLoading(false);
      if (inputRef.current) inputRef.current.value = "";
    }
  }

  return (
    <div className="space-y-3">
      <div className="border-2 border-dashed border-gray-300 rounded-xl p-6 bg-gray-50/50 hover:border-blue-400 hover:bg-blue-50/50 transition-all duration-200">
        <input
          ref={inputRef}
          type="file"
          accept=".csv"
          onChange={(e) => e.target.files && handleFile(e.target.files[0])}
          className="block w-full text-sm text-gray-700 file:mr-4 file:rounded-xl file:border-0 file:bg-gradient-to-r file:from-blue-600 file:to-purple-600 file:px-6 file:py-3 file:text-white file:font-semibold hover:file:from-blue-700 hover:file:to-purple-700 file:transition-all file:duration-200 file:cursor-pointer"
        />
        <div className="text-center mt-4">
          <svg className="w-8 h-8 mx-auto mb-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          <p className="text-sm text-gray-500">Or click "Choose File" button above</p>
        </div>
      </div>
      <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded-lg">
        <strong>Expected headers:</strong> product_name, category, features, audience, (keywords optional)<br/>
        <strong>Max size:</strong> 10MB
      </div>
      {error && <Banner type="error">{error}</Banner>}
      {loading && (
        <div className="flex items-center gap-2 text-sm p-3 bg-blue-50 rounded-lg">
          <div className="h-4 w-4 rounded-full border-2 border-blue-200 border-t-blue-600 animate-spin"></div>
          <span className="text-blue-700">Parsing CSV file...</span>
        </div>
      )}
      <Button onClick={() => inputRef.current?.click()} className="hidden">Upload</Button>
    </div>
  );
}
