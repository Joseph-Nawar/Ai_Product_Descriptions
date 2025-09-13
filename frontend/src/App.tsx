import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Results from "./pages/Results";

export default function App() {
  return (
    <div className="min-h-dvh bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 text-gray-900">
      <header className="bg-white/80 backdrop-blur-md border-b border-gray-200 shadow-sm sticky top-0 z-50">
        <div className="w-full px-4 py-4 flex items-center justify-between">
          <Link to="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">AI</span>
            </div>
            <span className="font-bold text-xl bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Describer</span>
          </Link>
          <nav className="text-sm text-gray-600">
            <a href="https://github.com" target="_blank" rel="noreferrer" className="hover:text-blue-600 transition-colors duration-200">Docs</a>
          </nav>
        </div>
      </header>
      <main className="relative">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </main>
      <footer className="bg-white/60 backdrop-blur-sm border-t border-gray-200 mt-12">
        <div className="mx-auto max-w-7xl p-4 text-xs text-gray-500 text-center">
          &copy; {new Date().getFullYear()} AI Describer - Transform your e-commerce with AI-powered descriptions
        </div>
      </footer>
    </div>
  );
}
