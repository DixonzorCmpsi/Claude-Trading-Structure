#!/usr/bin/env python3
"""
Brain Map Router — Deterministic query-to-file routing.

Takes a natural language query, scores it against brain-map.jsonl tags
and descriptions, returns ranked file paths to load.

Usage:
    python scripts/route.py "should I take this trade?"
    python scripts/route.py "what is an order block?"
    python scripts/route.py "I'm frustrated"

Output: JSONL — one line per matched node, sorted by score descending.
"""

import json
import sys
import re
import os

# Synonym expansion — maps common words to tag keywords
SYNONYMS = {
    # Trading actions
    "trade": ["trade", "setup", "entry"],
    "buy": ["trade", "setup", "entry", "vwap", "checkboxes"],
    "sell": ["trade", "setup", "entry", "vwap", "checkboxes"],
    "short": ["trade", "setup", "entry"],
    "long": ["trade", "setup", "entry"],
    "entry": ["trade", "setup", "entry", "checkboxes"],
    # Analysis
    "analyze": ["chart", "mcp", "data", "pattern"],
    "chart": ["chart", "mcp", "data", "read"],
    "look": ["chart", "mcp", "data", "read"],
    "see": ["chart", "mcp", "data", "read"],
    # Emotions
    "frustrated": ["emotion", "tilt", "revenge"],
    "angry": ["emotion", "tilt", "revenge"],
    "lost": ["emotion", "tilt", "review"],
    "losing": ["emotion", "tilt", "revenge"],
    "scared": ["emotion", "fomo"],
    "fomo": ["emotion", "fomo"],
    "revenge": ["emotion", "revenge", "veto"],
    # Education
    "teach": ["tjr", "confluences", "education", "beginner"],
    "learn": ["tjr", "confluences", "education", "beginner"],
    "explain": ["tjr", "confluences", "education", "beginner"],
    "what": ["tjr", "confluences", "cheatsheet"],
    # Specific concepts
    "vwap": ["vwap", "pullback", "mean-reversion", "institutional"],
    "fvg": ["fvg", "pattern", "confluence"],
    "gap": ["fvg", "gap", "fade"],
    "rsi": ["rsi", "mean-reversion", "oversold"],
    "tired": ["rsi", "oversold"],
    "overbought": ["rsi", "oversold"],
    "oversold": ["rsi", "oversold", "mean-reversion"],
    "macd": ["pattern", "setup"],
    "ema": ["ema", "crossover", "trend"],
    "breakout": ["breakout", "opening-range", "initial-balance"],
    "squeeze": ["squeeze", "compression", "volatility", "bollinger", "keltner"],
    "silver": ["ict", "silver-bullet", "10am", "time-window"],
    "bullet": ["ict", "silver-bullet", "10am"],
    "liquidity": ["liquidity", "sweep", "smart-money"],
    "sweep": ["liquidity", "sweep", "smart-money"],
    "structure": ["bos", "pattern", "confluence"],
    "bos": ["bos", "pattern"],
    "order": ["smart-money", "institutional", "order-flow"],
    "block": ["smart-money", "confluence"],
    "pdh": ["pdh", "pdl", "previous-day", "levels"],
    "pdl": ["pdh", "pdl", "previous-day", "levels"],
    "yesterday": ["pdh", "pdl", "previous-day"],
    "volume": ["volume-profile", "poc", "value-area"],
    "profile": ["volume-profile", "poc"],
    # Risk / Rules
    "risk": ["risk", "stop", "daily-loss", "checklist"],
    "stop": ["risk", "stop", "checklist"],
    "rules": ["risk", "stop", "daily-loss", "checklist", "veto"],
    "checklist": ["checklist", "risk", "trade"],
    # Review
    "review": ["review", "history", "lesson", "past-trade"],
    "journal": ["review", "history", "lesson"],
    # Strategy comparison
    "compare": ["compare", "win-rate", "strategy", "research"],
    "strategy": ["compare", "strategy", "research"],
    "which": ["compare", "strategy", "research"],
    "best": ["compare", "win-rate", "strategy"],
    # Session
    "morning": ["chart", "killzone", "timeframe"],
    "brief": ["chart", "killzone", "timeframe"],
    "session": ["killzone", "timeframe", "10am"],
    # Wisdom
    "patience": ["livermore", "wisdom", "discipline"],
    "discipline": ["livermore", "wisdom", "discipline"],
    "livermore": ["livermore", "wisdom"],
}


def tokenize(text: str) -> list[str]:
    """Extract lowercase words from text."""
    return re.findall(r'[a-z]+', text.lower())


def expand_query(words: list[str]) -> set[str]:
    """Expand query words using synonym map + keep originals."""
    expanded = set(words)
    for w in words:
        if w in SYNONYMS:
            expanded.update(SYNONYMS[w])
    return expanded


def score_node(query_tags: set[str], node: dict) -> int:
    """Score a node against expanded query tags."""
    node_tags = set(node.get("tags", []))
    desc_words = set(tokenize(node.get("description", "")))
    all_keywords = node_tags | desc_words

    return len(query_tags & all_keywords)


def route(query: str, brain_map_path: str = None) -> list[dict]:
    """Route a query to the best matching brain map nodes."""
    if brain_map_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        brain_map_path = os.path.join(script_dir, "..", "brain-map.jsonl")

    with open(brain_map_path) as f:
        nodes = [json.loads(line) for line in f if line.strip()]

    words = tokenize(query)
    expanded = expand_query(words)

    scored = []
    for node in nodes:
        s = score_node(expanded, node)
        if s > 0:
            scored.append({
                "score": s,
                "id": node["id"],
                "file": node["file"],
                "lines": node.get("lines", 0),
                "type": node.get("type", ""),
                "description": node.get("description", ""),
                "win_rate": node.get("win_rate", None),
            })

    scored.sort(key=lambda x: (-x["score"], x["lines"]))
    return scored[:5]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python route.py <query>", file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = route(query)

    if not results:
        print(json.dumps({"score": 0, "id": "root", "file": "CLAUDE.md", "lines": 60, "type": "router", "description": "No match — start at root."}))
    else:
        for r in results:
            print(json.dumps(r))
