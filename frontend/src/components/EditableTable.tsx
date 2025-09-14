import React, { useMemo, useState } from "react";
import { 
  useReactTable, 
  ColumnDef, 
  getCoreRowModel, 
  flexRender,
  createColumnHelper
} from "@tanstack/react-table";
import { GeneratedItem } from "../types";
import { copyText } from "../utils/clipboard";
import { Button, Spinner } from "./UI";

type Props = {
  data: GeneratedItem[];
  onChange: (next: GeneratedItem[]) => void;
  onRowSelect: (item: GeneratedItem) => void;
  selectedRowId?: string | null;
  onRegenerate: (item: GeneratedItem) => void;
};

const columnHelper = createColumnHelper<GeneratedItem>();

export default function EditableTable({ data, onChange, onRowSelect, selectedRowId, onRegenerate }: Props) {
  const [copiedRowId, setCopiedRowId] = useState<string | null>(null);
  
  const columns = useMemo<ColumnDef<GeneratedItem, any>[]>(() => [
    { 
      header: "Product", 
      accessorKey: "product_name", 
      cell: info => (
        <div className="space-y-1">
          <span className="font-medium text-gray-200">{info.getValue<string>()}</span>
          <div className="text-xs text-gray-400">
            {info.row.original.style_variation} • {info.row.original.tone}
          </div>
        </div>
      ),
      size: 200
    },
    { 
      header: "Category", 
      accessorKey: "category", 
      cell: info => <span className="px-2 py-0.5 bg-primary/20 text-primary rounded-full text-xs font-medium">{info.getValue<string>()}</span>,
      size: 120
    },
    { 
      header: "Audience", 
      accessorKey: "audience",
      cell: info => <span className="text-sm text-gray-300">{info.getValue<string>()}</span>,
      size: 150
    },
    columnHelper.accessor("description", {
      header: () => (
        <div className="text-center">
          <div className="text-lg font-bold text-primary mb-1">✨ AI-Generated Description</div>
          <div className="text-xs text-gray-400">The star of the show</div>
        </div>
      ),
      cell: ({ getValue, row }) => (
        <div className="space-y-3">
          <textarea
            className="w-full min-h-[200px] rounded-xl border-2 border-primary/30 bg-gradient-to-br from-primary/5 to-secondary/5 p-4 text-gray-900 focus:bg-gradient-to-br focus:from-primary/10 focus:to-secondary/10 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-primary transition-all duration-200 resize-y text-base leading-relaxed font-medium"
            value={getValue()}
            onChange={(e) => {
              const next = [...data];
              next[row.index] = { ...row.original, description: e.target.value };
              onChange(next);
            }}
            placeholder="Your AI-generated description will appear here..."
          />
          <div className="flex items-center justify-between">
            <div className="text-xs text-gray-400">
              {getValue().length} characters
            </div>
            <div className="flex gap-2">
              <Button 
                variant="secondary" 
                onClick={() => onRegenerate(row.original)} 
                disabled={row.original.regenerating}
                className="text-xs px-3 py-1"
              >
                {row.original.regenerating ? <Spinner size="sm" /> : "🔄 Regenerate"}
              </Button>
              <Button 
                variant="secondary" 
                onClick={async () => { 
                  await copyText(row.original.description);
                  setCopiedRowId(row.id);
                  setTimeout(() => setCopiedRowId(null), 2000);
                }}
                className="text-xs px-3 py-1"
              >
                {copiedRowId === row.id ? "✅ Copied!" : "📋 Copy"}
              </Button>
            </div>
          </div>
        </div>
      ),
      size: 600
    }),
    columnHelper.display({
      id: "features",
      header: "Features",
      cell: ({ row }) => (
        <div className="max-w-[200px]">
          <details className="group">
            <summary className="cursor-pointer text-sm text-gray-400 hover:text-gray-200 transition-colors">
              View Features
            </summary>
            <div className="mt-2 p-3 bg-gray-800 rounded-lg text-xs text-gray-300">
              {row.original.features}
            </div>
          </details>
        </div>
      ),
      size: 200
    })
  ], [data, onChange, copiedRowId, onRegenerate]);

  const table = useReactTable<GeneratedItem>({ data, columns, getCoreRowModel: getCoreRowModel() });

  return (
    <div className="overflow-auto">
      <table className="min-w-[1024px] w-full text-base">
        <thead className="bg-black/20">
          {table.getHeaderGroups().map(hg => (
            <tr key={hg.id}>
              {hg.headers.map(h => (
                <th key={h.id} className="text-left font-semibold p-4 border-b border-glass-border text-gray-300 tracking-wider">
                  {flexRender(h.column.columnDef.header, h.getContext())}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map(r => (
            <tr 
              key={r.id} 
              onClick={() => onRowSelect(r.original)}
              className={`border-b border-glass-border last:border-b-0 cursor-pointer transition-all duration-200
                ${selectedRowId === r.id ? 'bg-primary/20' : 'hover:bg-white/5'}`
              }
            >
              {r.getVisibleCells().map(c => (
                <td key={c.id} className="align-top p-4 text-gray-300">
                  {flexRender(c.column.columnDef.cell, c.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}