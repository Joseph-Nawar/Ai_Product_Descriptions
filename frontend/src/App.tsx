import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Results from "./pages/Results";

export default function App() {
  return (
    <>
      <div className="aurora-background"></div>
      <div className="relative min-h-dvh z-10">
        <header className="sticky top-4 z-50 mx-4 md:mx-8">
            <div className="bg-glass-bg backdrop-blur-lg border border-glass-border rounded-2xl shadow-2xl shadow-black/20">
              <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-3">
                <div className="flex items-center justify-between">
                  <Link to="/" className="flex items-center space-x-3 group">
                    <div className="w-10 h-10 bg-gradient-to-br from-primary to-secondary rounded-lg flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                      <span className="text-white font-extrabold text-lg">A</span>
                    </div>
                    <span className="font-bold text-2xl bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent group-hover:opacity-80 transition-opacity">
                      Describer
                    </span>
                  </Link>
                  <nav className="text-sm font-medium text-gray-300">
                    <a href="https://github.com" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors duration-200">
                      Documentation
                    </a>
                  </nav>
                </div>
              </div>
            </div>
        </header>
        <main className="relative mt-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/results" element={<Results />} />
          </Routes>
        </main>
        <footer className="mt-24 pb-8">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-sm text-center text-gray-400">
            &copy; {new Date().getFullYear()} AI Describer — The Future of E-commerce Content.
          </div>
        </footer>
      </div>
    </>
  );
}