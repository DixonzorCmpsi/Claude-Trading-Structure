## 10. Previous Day High/Low (PDH/PDL) Fade & Breakout

### Description
Previous Day High (PDH) and Previous Day Low (PDL) are universally watched levels that act as liquidity magnets. Since everyone sees these levels, stop losses and breakout orders cluster around them, creating predictable institutional behavior.

### Exact Rules

**Strategy A -- PDH/PDL Fade (Mean Reversion):**

**Entry -- Fade PDH (Short):**
1. Price rallies to PDH and shows rejection (long upper wicks, bearish engulfing)
2. Volume spike at PDH followed by declining volume
3. Enter short when price closes below PDH after touching it
4. Confirmation: RSI divergence (price makes higher high, RSI makes lower high)

**Entry -- Fade PDL (Long):**
1. Price drops to PDL and shows rejection (long lower wicks, bullish engulfing)
2. Volume spike at PDL followed by declining volume
3. Enter long when price closes above PDL after touching it

**Stop Loss:** 10-15 points beyond PDH (for short) or below PDL (for long)
**Take Profit:** VWAP or session midpoint

**Strategy B -- PDH/PDL Breakout (Trend Continuation):**

**Entry -- Breakout Above PDH (Long):**
1. Price breaks above PDH with a 5-minute candle close
2. Strong volume on the breakout candle
3. Price is above VWAP (confirming bullish trend)
4. Enter on the close of the breakout candle

**Stop Loss:** Below PDH (now support)
**Take Profit:** Trail with 20 EMA or target next significant level

### Statistics
- PDH/PDL are the most commonly cited levels by institutional traders
- Estimated 55-65% success rate for fades at these levels with confirmation
- Breakout plays depend heavily on the broader market trend
- These levels are most powerful when they align with other confluences (VWAP, ORB, IB levels)

### Why It Works (The Edge)
- PDH/PDL are liquidity accumulation zones: stops cluster just beyond these levels
- Institutions sweep PDH/PDL to collect stop-loss orders, then reverse
- When price truly breaks and holds beyond PDH/PDL, it signals acceptance of a new value area
- The levels are universally visible -- every platform shows them automatically

### Best Market Conditions
- Fade: range-bound or mean-reverting days
- Breakout: trending days with strong directional bias
- Combine with IB strategy: if IB breaks in the direction of PDH/PDL, you have double confirmation

### MNQ Implementation
- Always mark PDH and PDL on your chart before the session opens
- Add to your pre-market routine: note overnight high/low, PDH, PDL
- Use as TP/SL reference levels for other strategies (e.g., VWAP bounce TP at PDH)
- Combine with gap strategy: if there is a gap and PDL is nearby, it becomes a magnet
