## 7. Smart Money Concepts (Liquidity Sweep + FVG)

### Description
A comprehensive framework based on institutional order flow, backtested across 2,600 trades on 10 assets over 26 months (Jan 2024 - Mar 2026). The core premise: institutions sweep obvious liquidity pools (stop losses above highs / below lows), then deploy capital through Fair Value Gaps and Order Blocks.

### Exact Rules

**Bias Determination (Higher Timeframe):**
1. Check 4H trend direction (uptrend = bullish, downtrend = bearish)
2. Identify the nearest untouched liquidity pool:
   - Bullish: Sell-Side Liquidity (lows) that has NOT been swept yet
   - Bearish: Buy-Side Liquidity (highs) that has NOT been swept yet

**Entry — Bullish Setup:**
1. Price sweeps below a significant low (liquidity grab below SSL)
2. Price shows displacement: a strong bullish candle or series of candles away from the sweep
3. A Fair Value Gap (FVG) forms during the displacement (gap between candle 1's high wick and candle 3's low wick)
4. Wait for price to retrace into the FVG
5. Enter long inside the FVG (ideally at the 50% level, known as Consequent Encroachment)
6. Confirmation: lower timeframe break of structure (1-min BOS) inside the FVG

**Entry -- Bearish Setup:**
1. Price sweeps above a significant high (liquidity grab above BSL)
2. Strong bearish displacement follows
3. Bearish FVG forms
4. Wait for retrace into FVG
5. Enter short inside the FVG

**Stop Loss:**
- Below the low of the liquidity sweep (longs)
- Above the high of the liquidity sweep (shorts)

**Take Profit:**
- TP1: Next significant liquidity level (high/low on 1H or 4H)
- TP2: Higher timeframe order block or FVG
- Minimum 2R target

### Statistics (2,600-Trade Backtest)

| Metric | Value |
|--------|-------|
| Win Rate | 61% |
| Profit Factor | 2.17 |
| Average Return per Trade | +2.27R |
| Assets Tested | Gold, BTC, ETH, EUR/USD, GBP/USD, NAS100, SOL, USD/JPY, SPX500, XRP |
| Period | January 2024 - March 2026 |
| Comparison: Typical retail strategy | 45-55% win rate, PF < 1.5 |

**Individual concept performance:**
- Fair Value Gaps fill approximately 70% of the time
- Order Blocks show 60-65% reaction rate
- Liquidity sweeps followed by displacement: 65-70% continuation rate

### Why It Works (The Edge)
- Institutions need liquidity to fill large orders -- they actively engineer sweeps of obvious levels
- Retail traders cluster stops above highs and below lows, creating the liquidity pools
- After sweeping liquidity, institutions deploy in the opposite direction through FVGs and OBs
- Trading with institutional flow (rather than against it) creates a measurable statistical edge

### Best Market Conditions
- Works across all market conditions (trending and ranging)
- Highest conviction when 4H and 1H trends are aligned
- Strongest on high-volatility days with clear liquidity levels

### MNQ Implementation
- This is essentially the TJR/ICT framework already documented in your knowledge.md
- 4H bias + 1H trend alignment + 5-min or 15-min execution
- Key difference from basic SMC: the 2,600-trade backtest validates that the full sequence (sweep + displacement + FVG entry) produces a 61% win rate at 2.17 PF
- Focus on NAS100 specifically (one of the 10 backtested assets)
