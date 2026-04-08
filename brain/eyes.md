# Eyes — Market Perception Layer

> You have been routed here to LOOK at the market. Do not interpret yet.
> Collect data systematically, then pass it forward.

## Purpose
Intake raw market data in a specific order. Output a structured Market Snapshot that other brain regions consume.

## Step 1: Establish Context (30 seconds)
- Instrument: MNQ1! (default) or as specified
- Session: Pre-market / AM Session / Lunch / PM Session / After Hours
- Current time ET: Determine kill zone status
  - AM Kill Zone: 9:50-10:10 AM ET (primary)
  - PM Kill Zone: 1:30-3:00 PM ET (secondary)
  - Dead Zone: 11:30 AM-1:30 PM ET (DO NOT TRADE)
  - Pre-market: Before 9:30 AM ET (observe only)

## Step 2: Top-Down Timeframe Scan

### 4-Hour (The Compass)
MCP: `chart_set_timeframe("240")` → `data_get_ohlcv(summary: true)` → `data_get_study_values`
Record:
- Trend direction: Uptrend / Downtrend / Sideways
- EMA positions relative to price
- Last 3 candle pattern (momentum, exhaustion, indecision)

### 1-Hour (The Map)
MCP: `chart_set_timeframe("60")` → `data_get_ohlcv(summary: true)` → `data_get_study_values`
Record:
- Trend direction: Aligned with 4H? Yes/No
- Key swing highs and lows (these are liquidity targets)
- Distance from VWAP

### 15-Minute (The Terrain)
MCP: `chart_set_timeframe("15")`
Record:
- Current structure: higher highs/higher lows or lower highs/lower lows
- Nearest support and resistance levels
- Volume compared to average

### 5-Minute (The Execution Map)
MCP: `chart_set_timeframe("5")`
Record:
- Current micro-structure
- Distance from key 1H/4H levels
- MACD state (bullish cross, bearish cross, flat)
- EMA 9 position relative to price

## Step 3: Read Custom Indicators (if present)
MCP: `data_get_pine_labels` → Bias labels, level annotations
MCP: `data_get_pine_lines` → Price levels from custom indicators
MCP: `data_get_pine_tables` → Session stats if available

## Step 4: Key Levels Checklist
Note these levels (calculate or read from indicators):
- [ ] Prior day high (PDH)
- [ ] Prior day low (PDL)
- [ ] Prior day close (PDC)
- [ ] Overnight high / low
- [ ] VWAP and standard deviation bands
- [ ] Opening range high/low (first 15 min after 9:30)
- [ ] Round numbers (nearest 100-point levels on MNQ)

## Step 5: Visual Confirmation
MCP: `capture_screenshot(region: "chart")` → Confirm everything above visually

## Output: Market Snapshot

Produce this structured output for downstream brain regions:

```
MARKET SNAPSHOT
- Instrument: [symbol]
- Time: [current ET time]
- Session: [which session]
- Kill Zone: [active / inactive / approaching]
- Price: [current]
- 4H Bias: [Bullish/Bearish/Neutral] — [reason]
- 1H Trend: [Aligned/Opposing/Neutral] — [reason]
- 5m Structure: [Higher highs or lower lows]
- MACD: [bullish cross / bearish cross / flat]
- EMA 9: [above/below price]
- VWAP: [above/below price, distance]
- Key Levels: [list with prices]
- Liquidity Targets: [highs/lows price is drawn to]
- Volume: [above/below average]
- Notable: [anything unusual — gap, news, low volume, etc.]
```
