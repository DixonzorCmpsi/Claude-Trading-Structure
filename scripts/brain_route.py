#!/usr/bin/env python3
"""
BAML Brain Router — Typed, deterministic query routing.

Uses BAML to classify user queries and return typed routing decisions.
The LLM understands semantics (not just keywords), but output is
constrained to our defined types.

Usage:
    python scripts/brain_route.py "should I take this trade?"
    python scripts/brain_route.py "what is an order block?"
    python scripts/brain_route.py "I'm frustrated I keep losing"

Output: JSON with intent, primary file, secondary files, and reasoning.
"""

import asyncio
import json
import sys
import os

# Add parent dir to path so baml_client is importable
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "baml_client"))

from baml_client.async_client import b
from baml_client.types import RouteResult

# Map BrainNode enum values to actual file paths
NODE_TO_FILE = {
    "SPECIALIZATION": "brain/specialization.md",
    "EYES": "brain/eyes.md",
    "ANALYSIS": "brain/analysis.md",
    "DECISION": "brain/decision.md",
    "PSYCHOLOGY": "brain/psychology.md",
    "JOURNAL": "brain/journal.md",
    "RULES": "rules.md",
    "SOUL": "soul.md",
    "KNOWLEDGE_CORE": "knowledge/core.md",
    "KNOWLEDGE_FULL": "knowledge.md",
    "STRATEGY_INDEX": "strategies/index.md",
    "STRATEGY_ORB": "strategies/01-orb.md",
    "STRATEGY_GAP": "strategies/02-gap-fill.md",
    "STRATEGY_IB": "strategies/03-initial-balance.md",
    "STRATEGY_VWAP": "strategies/04-vwap-pullback.md",
    "STRATEGY_SB": "strategies/05-silver-bullet.md",
    "STRATEGY_RSI2": "strategies/06-connors-rsi.md",
    "STRATEGY_SMC": "strategies/07-smc.md",
    "STRATEGY_P3": "strategies/08-power-of-3.md",
    "STRATEGY_SQUEEZE": "strategies/09-squeeze.md",
    "STRATEGY_PDH": "strategies/10-pdh-pdl.md",
    "STRATEGY_VPOC": "strategies/11-volume-profile.md",
    "STRATEGY_EMA": "strategies/12-ema-vwap.md",
    "STRATEGY_PRINCIPLES": "strategies/principles.md",
}


async def route(query: str) -> dict:
    result: RouteResult = await b.RouteBrain(query)

    primary_file = NODE_TO_FILE.get(result.primary.value, "CLAUDE.md")
    secondary_files = [NODE_TO_FILE.get(n.value, "") for n in result.secondary if n.value in NODE_TO_FILE]

    return {
        "intent": result.intent.value,
        "primary": {
            "node": result.primary.value,
            "file": primary_file,
        },
        "secondary": [
            {"node": n.value, "file": NODE_TO_FILE.get(n.value, "")}
            for n in result.secondary
            if n.value in NODE_TO_FILE
        ],
        "total_lines": result.total_lines,
        "reasoning": result.reasoning,
    }


async def main():
    if len(sys.argv) < 2:
        print("Usage: python brain_route.py <query>", file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    result = await route(query)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
