# Brain Architecture — Design Reference

## Overview

This directory contains the cognitive processing pipeline for the trading system. Each file is a "brain region" that processes information in sequence, inspired by:

- **MAP** (Nature Communications 2025) — Modular Agentic Planner mapped to prefrontal cortex regions
- **ACT-R** (Carnegie Mellon) — Cognitive architecture with module/buffer system
- **Reflexion** (2023) — Self-critique stored in memory for future decisions
- **TradingAgents** — Multi-agent trading firm architecture

## Architecture

```
CLAUDE.md (Router / Prefrontal Cortex)
    |
    v
eyes.md ──> analysis.md ──> psychology.md ──> decision.md
  (see)      (recognize)     (feel check)     (decide)
                                  |
                 rules.md ───────┘ (can VETO)
                 journal.md ─────── (memory)
```

## Brain Region Mapping

| File | Brain Region | ACT-R Module | Role |
|------|-------------|-------------|------|
| eyes.md | Visual cortex | Visual Module | Perceive market data |
| analysis.md | Temporal lobe | Imaginal Buffer | Recognize patterns |
| psychology.md | Limbic system | — | Regulate emotions |
| journal.md | Hippocampus | Declarative Memory | Remember past trades |
| decision.md | Anterior cingulate | Goal Module | Final synthesis |

## Knowledge Base (Root Level)

| File | Brain Region | ACT-R Module | Role |
|------|-------------|-------------|------|
| rules.md | Amygdala | Production Rules | Threat detection, veto |
| soul.md | Default mode network | — | Identity, beliefs |
| knowledge.md | Hippocampus | Declarative Memory | TJR system |
| strategies.md | Cerebellum | Procedural Memory | Trained procedures |

## Key Design Principles

1. **Sequential processing with gating** — Information flows through modules in order
2. **Veto power** — rules.md and psychology.md can kill any trade
3. **Binary gating, not scoring** — Each gate passes or fails. No "good enough"
4. **Reflexion pattern** — Past trade outcomes directly inform future decisions
5. **Constraints create discipline** — Like ACT-R, the system's power comes from what it WON'T do

## ACT-R Insights Applied

- **One thing at a time**: Each brain region produces ONE structured output
- **Production compilation**: As the trader gains experience, the journal tracks internalized rules
- **Utility learning**: Journal tracks win rates per pattern to resolve strategy conflicts
- **Spreading activation**: Journal entries tagged by conditions, not just dates
- **Goal stack**: Trading session → determine bias → check 4H → read chart (hierarchical)
