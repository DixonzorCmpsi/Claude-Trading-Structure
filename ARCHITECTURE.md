# Architecture — Trading Brain System

## The Three Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  YOU (Dixon)                                                     │
│  "Should I trade?" / "I'm frustrated" / "What's a FVG?"         │
└──────────────────────────┬──────────────────────────────────────┘
                           │ your words
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: MEMORY          (lives in ~/.claude/projects/memory/) │
│                                                                  │
│  What it stores:                                                 │
│  • Who you are (beginner trader, $250 account)                   │
│  • How you like to work (plain English, no jargon)               │
│  • What we decided (VWAP+FVG sniper, both directions)            │
│  • Mistakes to avoid (check both buy AND sell)                   │
│                                                                  │
│  When it loads: AUTOMATICALLY every conversation start            │
│  Who writes it: Claude, after learning something about you       │
│  Format: Markdown files with frontmatter                         │
│                                                                  │
│  Think of it as: Your permanent file at a doctor's office.       │
│  Every time you walk in, they read your file first.              │
└──────────────────────────┬──────────────────────────────────────┘
                           │ "Dixon is a beginner, use plain
                           │  English, check both directions,
                           │  he can veto the time window"
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2: KNOWLEDGE       (lives in the project repo)           │
│                                                                  │
│  Two steps happen here:                                          │
│                                                                  │
│  STEP A — ROUTING (which files do I need?)                       │
│  ┌─────────────────────────────────────────────────────┐        │
│  │  brain-map.jsonl (25 nodes, tags, parent/child)     │        │
│  │       │                                             │        │
│  │       ▼                                             │        │
│  │  Gemma4 (local LLM via Ollama)                      │        │
│  │  + BAML typed contract                              │        │
│  │       │                                             │        │
│  │       ▼                                             │        │
│  │  RouteResult {                                      │        │
│  │    intent: TRADE_DECISION                           │        │
│  │    primary: specialization.md                       │        │
│  │    secondary: [decision.md, analysis.md]            │        │
│  │    total_lines: 355                                 │        │
│  │  }                                                  │        │
│  └─────────────────────────────────────────────────────┘        │
│                           │                                      │
│  STEP B — LOADING (read only what's needed)                      │
│  ┌─────────────────────────────────────────────────────┐        │
│  │  specialization.md  ← "Run the 5 checkboxes"       │        │
│  │  decision.md        ← "Apply the 5-gate system"    │        │
│  │  analysis.md        ← "Identify the setup"         │        │
│  │                                                     │        │
│  │  (NOT loaded: knowledge.md, strategies.md,          │        │
│  │   soul.md, journal.md — not needed this time)       │        │
│  └─────────────────────────────────────────────────────┘        │
│                                                                  │
│  Think of it as: A library. The routing step is the librarian    │
│  who says "you need books from shelf 3 and 7." You don't        │
│  read the whole library — just those two shelves.                │
└──────────────────────────┬──────────────────────────────────────┘
                           │ "5 checkboxes say: buy if VWAP + FVG
                           │  + RSI < 40 + 4H trend + bounce"
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: EXECUTION       (TradingView via MCP tools)           │
│                                                                  │
│  Claude (me) reads the live chart:                               │
│  • Neural Dashboard → VWAP, EMA, RSI, MACD, FVG boxes          │
│  • quote_get → current price                                    │
│  • data_get_pine_tables → bias table, momentum summary          │
│                                                                  │
│  Claude runs the 5 checkboxes against live data                  │
│  Claude gives you the verdict + personal analysis                │
│                                                                  │
│  If you say "do it":                                             │
│  • Click buy-order-button or sell-order-button                   │
│  • Set stop loss and take profit                                 │
│                                                                  │
│  Think of it as: The trading floor. The knowledge told me        │
│  WHAT to look for. The execution layer is WHERE I look           │
│  and WHERE I act.                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Sequence Diagram — "Should I trade?"

This is what happens step by step when you ask that question:

```
 YOU          MEMORY         GEMMA (local)      CLAUDE         TRADINGVIEW
  │           LAYER          (router)           (brain)        (MCP tools)
  │                                                               │
  │──"should I trade?"──────────────────────────▶│                │
  │                                              │                │
  │           │◀─── auto-loaded on start ────────│                │
  │           │  "Dixon: beginner, plain English, │                │
  │           │   check both directions"          │                │
  │           │─────────────────────────────────▶│                │
  │                                              │                │
  │                          │◀── query ─────────│                │
  │                          │  "should I trade?" │                │
  │                          │                    │                │
  │                          │── reads ──▶ brain-map.jsonl        │
  │                          │                    │                │
  │                          │── BAML typed ────▶│                │
  │                          │  RouteResult:      │                │
  │                          │  primary: spec.md  │                │
  │                          │  secondary:        │                │
  │                          │   decision.md      │                │
  │                          │   analysis.md      │                │
  │                                              │                │
  │                              Claude loads:    │                │
  │                              specialization.md│                │
  │                              decision.md      │                │
  │                              rules.md         │                │
  │                                              │                │
  │                                              │──read chart──▶│
  │                                              │  quote_get     │
  │                                              │  study_values  │
  │                                              │  pine_tables   │
  │                                              │  pine_boxes    │
  │                                              │◀── live data──│
  │                                              │   price: 24970 │
  │                                              │   RSI: 15      │
  │                                              │   VWAP: 24964  │
  │                                              │   MACD: bear   │
  │                                              │                │
  │                              Claude runs:     │                │
  │                              □ 4H trend?      │                │
  │                              □ At VWAP?       │                │
  │                              □ FVG here?      │                │
  │                              □ RSI tired?     │                │
  │                              □ Bounce?        │                │
  │                                              │                │
  │◀──── "3/5 checkboxes. NO TRADE. Here's why  │                │
  │       + here's my honest read on what        │                │
  │       I think happens next" ─────────────────│                │
  │                                                               │
  │                                                               │
  │── (later) "do it" ──────────────────────────▶│                │
  │                                              │──click BUY───▶│
  │                                              │──set SL/TP──▶│
  │◀──── "Bought 1 MNQ at 24970,               │                │
  │       SL 24967.50, TP 24980" ───────────────│                │
  │                                                               │
```

---

## Sequence Diagram — "What is a fair value gap?"

Different query, different route, different files loaded:

```
 YOU          MEMORY         GEMMA (local)      CLAUDE         TRADINGVIEW
  │                                              │                │
  │──"what is a fair value gap?"────────────────▶│                │
  │                                              │                │
  │           │─── "use plain English" ─────────▶│                │
  │                                              │                │
  │                          │◀── query ─────────│                │
  │                          │── BAML ──────────▶│                │
  │                          │  RouteResult:      │                │
  │                          │  intent: EDUCATION │                │
  │                          │  primary:          │                │
  │                          │   knowledge/core   │                │
  │                          │  secondary:        │                │
  │                          │   strategies/smc   │                │
  │                                              │                │
  │                              Claude loads:    │                │
  │                              knowledge/core.md│ (87 lines)    │
  │                              strategies/07-smc│ (69 lines)    │
  │                              NOT knowledge.md │ (saves 502!)  │
  │                                              │                │
  │◀──── "A fair value gap is when price        │                │
  │       moves so fast it skips over part       │                │
  │       of the road. Those green and red       │                │
  │       boxes on your chart? Those are         │                │
  │       FVGs..." (plain English per memory)    │                │
```

---

## Sequence Diagram — "I'm frustrated"

Emotional query — psychology gets VETO POWER:

```
 YOU          MEMORY         GEMMA (local)      CLAUDE         TRADINGVIEW
  │                                              │                │
  │──"I'm frustrated I keep losing"─────────────▶│                │
  │                                              │                │
  │           │─── "beginner, be supportive" ───▶│                │
  │                                              │                │
  │                          │◀── query ─────────│                │
  │                          │── BAML ──────────▶│                │
  │                          │  intent:           │                │
  │                          │   EMOTIONAL_SUPPORT│                │
  │                          │  primary:          │                │
  │                          │   psychology.md    │                │
  │                          │  secondary:        │                │
  │                          │   journal.md       │                │
  │                          │   rules.md         │                │
  │                                              │                │
  │                              psychology.md:   │                │
  │                              VETO ACTIVATED   │                │
  │                              "Do NOT trade    │                │
  │                               in this state"  │                │
  │                                              │                │
  │◀──── "I hear you. Let's step back.          │                │
  │       Livermore said: 'The market will       │                │
  │       be there tomorrow.' You followed       │                │
  │       your rules — that's what matters.      │                │
  │       Take a break. Come back tomorrow."     │                │
  │                                              │                │
  │       ⛔ ALL TRADING BLOCKED FOR SESSION      │                │
```

---

## How Memory Feeds Knowledge

```
MEMORY says:                          KNOWLEDGE does:
─────────────────────────────────     ──────────────────────────────────
"Dixon is a beginner"            ──▶  Use plain English in all outputs
"Use plain English, no jargon"   ──▶  Translate: VWAP = "blue line"
"Check both buy AND sell"        ──▶  Run 5 checkboxes TWICE per analysis
"He can veto time window"        ──▶  Skip time check when Dixon says so
"Locked in VWAP+FVG sniper"     ──▶  Route to specialization.md first
"Analysis style: system + read"  ──▶  Give checkboxes AND personal opinion
```

Memory is WHO YOU ARE.
Knowledge is WHAT I KNOW.
Memory shapes HOW I use knowledge.

Without memory: I'd explain things like you're an expert, only check buys,
enforce time windows strictly, and give dry checkbox outputs.

With memory: I explain in plain English, check both directions, let you
override time windows, and give you my honest gut read alongside the system.

---

## File Map (what lives where)

```
Claude-Trading-Structure/
├── CLAUDE.md                    ← 60 lines. Entry point. Routing table.
├── brain-map.jsonl              ← 25 nodes. The graph Gemma reads.
├── baml_src/main.baml           ← Typed contract. Input→Output schema.
│
├── brain/                        ← Brain regions (loaded on demand)
│   ├── specialization.md         ← THE strategy. 5 checkboxes. 148 lines.
│   ├── eyes.md                   ← How to read charts. 88 lines.
│   ├── analysis.md               ← Pattern recognition. 102 lines.
│   ├── decision.md               ← 5-gate system. 105 lines.
│   ├── psychology.md             ← Emotions. VETO POWER. 97 lines.
│   └── journal.md                ← Trade history. 110 lines.
│
├── knowledge/                    ← Knowledge (progressive)
│   └── core.md                   ← Cheat sheet. 87 lines.
├── knowledge.md                  ← Full TJR guide. 502 lines. HEAVY.
│
├── strategies/                   ← Strategy library (progressive)
│   ├── index.md                  ← Summary table. 39 lines. START HERE.
│   ├── 01-orb.md ... 12-ema.md  ← Individual strategies. ~60 lines each.
│   └── principles.md             ← Cross-cutting rules. 76 lines.
│
├── rules.md                      ← 30 rules. 220 lines.
├── soul.md                       ← Livermore personality. 170 lines.
│
├── scripts/
│   ├── brain_route.py            ← BAML runner (calls Gemma)
│   └── route.py                  ← Keyword fallback (no LLM needed)
│
├── baml_client/                  ← Generated Python client
└── baml_src/main.baml            ← BAML type definitions
```
