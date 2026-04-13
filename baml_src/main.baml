// ─── Generator ───

generator python_client {
  output_type "python/pydantic"
  output_dir "../baml_client"
  version "0.220.0"
}

// Brain Map Router — BAML typed LLM routing
// Takes a user query, returns deterministic typed output
// specifying exactly which brain files to load and why.

// ─── Clients ───

// Local SLM for routing (free, fast, no API key needed)
client<llm> LocalRouter {
  provider ollama
  options {
    model "gemma4:26b"
    base_url "http://localhost:11434/v1"
  }
}

// ─── Types ───

enum BrainNode {
  SPECIALIZATION    @alias("spec")       @description("brain/specialization.md — VWAP+FVG sniper strategy, 5 checkboxes. 148 lines.")
  EYES              @alias("eyes")       @description("brain/eyes.md — Chart reading via MCP tools. Multi-timeframe scan. 88 lines.")
  ANALYSIS          @alias("analysis")   @description("brain/analysis.md — Pattern recognition, setup ID, entry/SL/TP calc. 102 lines.")
  DECISION          @alias("decision")   @description("brain/decision.md — 5-gate TRADE/NO-TRADE/WAIT system. 105 lines.")
  PSYCHOLOGY        @alias("psychology") @description("brain/psychology.md — Emotional state detection. VETO POWER. 97 lines.")
  JOURNAL           @alias("journal")    @description("brain/journal.md — Trade memory, past setups, lessons. 110 lines.")
  RULES             @alias("rules")      @description("rules.md — 30 non-negotiable trading rules. VETO POWER. 220 lines.")
  SOUL              @alias("soul")       @description("soul.md — Jesse Livermore personality, wisdom, discipline. 170 lines.")
  KNOWLEDGE_CORE    @alias("knowledge_core") @description("knowledge/core.md — TJR cheat sheet. 7 confluences, kill zones. 87 lines.")
  KNOWLEDGE_FULL    @alias("knowledge_full") @description("knowledge.md — Full TJR guide. 502 lines. HEAVY — only for deep teaching.")
  STRATEGY_INDEX    @alias("strat_index")    @description("strategies/index.md — Comparison matrix of all 12 strategies. 39 lines.")
  STRATEGY_ORB      @alias("orb")        @description("strategies/01-orb.md — Opening Range Breakout. 71-75% win rate. 64 lines.")
  STRATEGY_GAP      @alias("gap")        @description("strategies/02-gap-fill.md — Gap Fill. 78-93% win rate. 74 lines.")
  STRATEGY_IB       @alias("ib")         @description("strategies/03-initial-balance.md — Initial Balance Breakout. 73-84%. 63 lines.")
  STRATEGY_VWAP     @alias("vwap")       @description("strategies/04-vwap-pullback.md — VWAP Pullback. Our primary. 60-65%. 65 lines.")
  STRATEGY_SB       @alias("sb")         @description("strategies/05-silver-bullet.md — ICT Silver Bullet. 55-83%. 64 lines.")
  STRATEGY_RSI2     @alias("rsi2")       @description("strategies/06-connors-rsi.md — Connors RSI(2). 75-91% win rate. 63 lines.")
  STRATEGY_SMC      @alias("smc")        @description("strategies/07-smc.md — Smart Money Concepts. Profit factor 2.17. 69 lines.")
  STRATEGY_P3       @alias("p3")         @description("strategies/08-power-of-3.md — ICT Power of 3 (AMD). 60-70%. 59 lines.")
  STRATEGY_SQUEEZE  @alias("squeeze")    @description("strategies/09-squeeze.md — BB/KC Squeeze. ~80% accuracy. 63 lines.")
  STRATEGY_PDH      @alias("pdh")        @description("strategies/10-pdh-pdl.md — PDH/PDL Fade & Breakout. 55-65%. 56 lines.")
  STRATEGY_VPOC     @alias("vpoc")       @description("strategies/11-volume-profile.md — Volume Profile POC. 60-70%. 48 lines.")
  STRATEGY_EMA      @alias("ema")        @description("strategies/12-ema-vwap.md — EMA Cross + VWAP Filter. 50-60%. 51 lines.")
  STRATEGY_PRINCIPLES @alias("principles") @description("strategies/principles.md — Cross-cutting principles, MNQ specs. 76 lines.")
}

enum QueryIntent {
  TRADE_DECISION    @description("User wants to know if they should enter a trade right now")
  CHART_ANALYSIS    @description("User wants current chart read / market analysis")
  EMOTIONAL_SUPPORT @description("User is frustrated, tilted, scared, or euphoric")
  EDUCATION         @description("User wants to learn a concept or understand terminology")
  TRADE_REVIEW      @description("User wants to review a completed trade")
  SESSION_PREP      @description("User wants a morning brief or session plan")
  STRATEGY_RESEARCH @description("User wants to compare or explore strategies")
  TRADE_EXECUTION   @description("User wants to place a trade now (says 'do it', 'execute', etc)")
}

class RouteResult {
  intent QueryIntent        @description("The classified intent of the user's query")
  primary BrainNode         @description("The FIRST file to load. Most important.")
  secondary BrainNode[]     @description("Additional files to load, in priority order. Keep this SHORT — max 3.")
  total_lines int           @description("Estimated total lines that will be loaded")
  reasoning string          @description("One sentence explaining the routing decision")
}

// ─── Function ───

function RouteBrain(query: string) -> RouteResult {
  client LocalRouter
  prompt #"
    You are a routing function for a trading brain system. Given a user query,
    determine which brain files to load.

    RULES:
    - For ANY trade-related question, SPECIALIZATION is always the primary
    - For emotional queries, PSYCHOLOGY is primary (it has VETO POWER)
    - For education, start with KNOWLEDGE_CORE not KNOWLEDGE_FULL
    - For strategy comparison, start with STRATEGY_INDEX not individual files
    - Keep secondary to MAX 3 files. Less is better.
    - NEVER include KNOWLEDGE_FULL unless the query specifically asks for deep teaching
    - Prefer smaller files (fewer lines) when two files could answer the question

    USER QUERY:
    {{ query }}

    {{ ctx.output_format }}
  "#
}
