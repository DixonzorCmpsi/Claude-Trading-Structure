## 12. EMA Crossover + VWAP Filter

### Description
A simple EMA crossover (9 EMA crossing 20 EMA) combined with a VWAP directional filter to reduce false signals. This is the simplest strategy listed but has the weakest standalone edge. Best used as a confirmation tool rather than a primary strategy.

### Exact Rules

**Indicators:**
- 9-period EMA
- 20-period EMA (or 21 EMA)
- Session VWAP

**Entry -- Long:**
1. 9 EMA crosses above 20 EMA (bullish crossover)
2. Price is above VWAP (bullish filter)
3. RSI > 50 (momentum confirmation)
4. Enter on the candle close after the crossover

**Entry -- Short:**
1. 9 EMA crosses below 20 EMA (bearish crossover)
2. Price is below VWAP (bearish filter)
3. RSI < 50
4. Enter on the candle close after the crossover

**Stop Loss:**
- Below the most recent swing low (for longs)
- Above the most recent swing high (for shorts)

**Take Profit:**
- 1.5-2R
- Or exit when the EMAs cross back

### Statistics

| Metric | Value |
|--------|-------|
| Win Rate (standalone crossover, no filter) | 24-43% (high false signal rate) |
| Win Rate (with VWAP + RSI filter) | ~50-60% estimated |
| False Signal Rate (S&P 500, 1960-2025) | 57-76% for basic crossovers |

### Why It Works (only with filters)
- EMAs capture short-term momentum shifts
- VWAP filter eliminates counter-trend crossovers
- RSI filter eliminates crossovers in choppy/flat markets
- Without filters, the basic EMA crossover has a negative expectancy on futures

### MNQ Implementation
- Use as a SECONDARY confirmation tool, not as a standalone strategy
- Best application: confirm ORB or VWAP bounce direction with EMA alignment
- 5-minute chart with 9/20 EMA + VWAP overlay
- If you are taking an ORB long and the 9 EMA is above the 20 EMA AND price is above VWAP, you have triple confirmation
