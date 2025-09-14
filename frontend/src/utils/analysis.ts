// A simple sentiment word list (expand for more accuracy)
const POSITIVE_WORDS = ['amazing', 'best', 'brilliant', 'beautiful', 'excellent', 'fantastic', 'great', 'high-quality', 'innovative', 'love', 'perfect', 'premium', 'revolutionary', 'stunning', 'versatile', 'wonderful'];
const NEGATIVE_WORDS = ['bad', 'cheap', 'flimsy', 'hate', 'poor', 'problem', 'terrible', 'worst'];

export function calculateWordCount(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

export function getReadabilityScore(text: string): string {
  // Simplified Flesch-Kincaid reading ease score simulation
  const wordCount = calculateWordCount(text);
  const sentenceCount = text.split(/[.!?]+/).filter(Boolean).length || 1;
  const syllableCount = (text.match(/[aeiouy]{1,2}/gi) || []).length;
  
  if (wordCount < 10) return "N/A";

  const score = 206.835 - 1.015 * (wordCount / sentenceCount) - 84.6 * (syllableCount / wordCount);

  if (score >= 90) return "5th Grade";
  if (score >= 80) return "6th Grade";
  if (score >= 70) return "7th Grade";
  if (score >= 60) return "8th-9th Grade";
  if (score >= 50) return "10th-12th Grade";
  if (score >= 30) return "College";
  return "Graduate";
}

export function checkKeywords(description: string, keywords?: string): { found: string[], missing: string[] } {
  if (!keywords) return { found: [], missing: [] };
  
  const keywordList = keywords.split(',').map(k => k.trim().toLowerCase()).filter(Boolean);
  const descriptionLower = description.toLowerCase();
  
  const found = keywordList.filter(k => new RegExp(`\\b${k}\\b`).test(descriptionLower));
  const missing = keywordList.filter(k => !found.includes(k));
  
  return { found, missing };
}

export function getSentiment(text: string): { score: number, label: string } {
  const words = text.toLowerCase().split(/\s+/);
  let score = 0;
  
  words.forEach(word => {
    if (POSITIVE_WORDS.includes(word)) score++;
    if (NEGATIVE_WORDS.includes(word)) score--;
  });
  
  const normalizedScore = Math.max(-5, Math.min(5, score)); // Clamp score between -5 and 5
  
  let label = "Neutral";
  if (normalizedScore > 1) label = "Positive";
  if (normalizedScore < -1) label = "Negative";

  return { score: normalizedScore, label };
}