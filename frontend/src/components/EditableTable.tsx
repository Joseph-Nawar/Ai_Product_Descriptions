import { useMemo } from "react";
import { 
  useReactTable, 
  ColumnDef, 
  getCoreRowModel, 
  flexRender,
  createColumnHelper
} from "@tanstack/react-table";
import { GeneratedItem } from "../types";
import { copyText } from "../utils/clipboard";
import { Button } from "./UI";

type Props = {
  data: GeneratedItem[];
  onChange: (next: GeneratedItem[]) => void;
};

const columnHelper = createColumnHelper<GeneratedItem>();

export default function EditableTable({ data, onChange }: Props) {
  const columns = useMemo<ColumnDef<GeneratedItem, any>[]>(() => [
    columnHelper.accessor("product_name", {
      header: "Product",
    }),
    columnHelper.accessor("category", {
      header: "Category",
    }),
    columnHelper.accessor("audience", {
      header: "Audience",
    }),
    columnHelper.accessor("description", {
      header: "Description",
      cell: ({ getValue, row }) => {
        const value = String(getValue());
        return (
          <textarea
            className="w-full min-h-[120px] rounded-xl border-2 border-gray-200 p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-white shadow-sm hover:border-gray-300 resize-none text-sm leading-relaxed"
            value={value}
            onChange={(e) => {
              const next = [...data];
              next[row.index] = { ...row.original, description: e.target.value };
              onChange(next);
            }}
          />
        );
      }
    }),
    columnHelper.display({
      id: "copy",
      header: "Copy",
      cell: ({ row }) => (
        <Button
          onClick={async () => { await copyText(row.original.description); }}
          className="text-sm px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600"
        >
          <span className="flex items-center gap-1">
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            Copy
          </span>
        </Button>
      )
    })
  ], [data, onChange]);

  const table = useReactTable<GeneratedItem>({ 
    data, 
    columns, 
    getCoreRowModel: getCoreRowModel() 
  });

  return (
    <div className="overflow-auto">
      <table className="min-w-[900px] w-full text-sm">
        <thead className="bg-gradient-to-r from-gray-50 to-gray-100">
          {table.getHeaderGroups().map(hg => (
            <tr key={hg.id}>
              {hg.headers.map(h => (
                <th key={h.id} className="text-left font-semibold p-4 border-b-2 border-gray-200 text-gray-700">
                  {flexRender(h.column.columnDef.header, h.getContext())}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody className="divide-y divide-gray-100">
          {table.getRowModel().rows.map(r => (
            <tr key={r.id} className="hover:bg-gray-50/50 transition-colors duration-150">
              {r.getVisibleCells().map(c => (
                <td key={c.id} className="align-top p-4">
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
