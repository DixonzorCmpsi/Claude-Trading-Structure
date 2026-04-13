## 4. VWAP Pullback / Bounce

### Description
VWAP (Volume Weighted Average Price) represents institutional fair value for the day. In trending markets, pullbacks to VWAP frequently provide high-probability continuation entries because institutions defend the VWAP level with resting orders.

### Exact Rules

**Setup (Daily):**
- Determine daily bias: Is price trending above or below VWAP?
- Price above VWAP = bullish bias (look for long entries on pullbacks)
- Price below VWAP = bearish bias (look for short entries on rallies)
- VWAP must have a clear slope (not flat/choppy)

**Entry — Long (VWAP Bounce):**
1. Price is in an uptrend (above VWAP, making higher highs)
2. Price pulls back to touch or briefly pierce VWAP
3. Volume declines on the pullback (sellers exhausted)
4. Look for a rejection candle: long lower wick touching VWAP, close back above it
5. Volume surges on the rejection candle (buyers stepping in)
6. Enter when price closes a 1-min or 5-min candle back above VWAP
7. Confirmation: RSI > 50 on the bounce candle

**Entry — Short (VWAP Rejection):**
1. Price is in a downtrend (below VWAP, making lower lows)
2. Price rallies up to touch or briefly pierce VWAP
3. Volume declines on the rally
4. Look for rejection: long upper wick at VWAP, close back below
5. Enter when price closes below VWAP after the test

**Stop Loss:**
- Place below the wick low of the bounce candle (for longs)
- On a 1-minute chart: typically 5-15 MNQ points
- On a 5-minute chart: typically 10-25 MNQ points
- Never more than the recent swing low below VWAP

**Take Profit:**
- TP1: Prior intraday high (or prior swing high)
- TP2: 1.5-2R from entry
- Trail stop after 1R is achieved

### Statistics

| Metric | Value |
|--------|-------|
| Win Rate | 60-65% (Steady Turtle Trading) |
| Best Time Window | 9:30-11:00 AM ET and 3:00-4:00 PM ET |
| Worst Time Window | 11:30 AM - 1:30 PM ET (midday lull, unreliable) |

### Why It Works (The Edge)
- VWAP is the benchmark used by institutional algorithms for execution
- Institutions buying at VWAP means they are getting "fair value" -- they defend this level
- Pullbacks to VWAP in a trend represent mean reversion to institutional fair value
- The declining volume on pullback + surging volume on bounce is a clear demand/supply signature

### Best Market Conditions
- Clear trending days (not choppy/range-bound)
- High volume sessions (first 90 minutes, last 60 minutes)
- Works exceptionally well on NQ/MNQ due to NQ's tendency to trend intraday

### MNQ Implementation
- Add anchored VWAP to your TradingView chart (auto-anchored to session open)
- Use 1-minute chart for entries, 5-minute for confirmation
- Best setup: 1st or 2nd pullback to VWAP after a strong opening move
- 3rd+ touches of VWAP reduce reliability (level becomes exhausted)
- Combine with opening range direction for added confluence
