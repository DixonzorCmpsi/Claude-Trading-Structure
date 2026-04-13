## 11. Volume Profile POC Reversion

### Description
The Point of Control (POC) is the price level where the highest volume of trades occurred during the previous session. Price gravitates toward the POC because it represents "fair value" -- the price where the most buyers and sellers agreed. When price deviates from POC, it tends to revert back.

### Exact Rules

**Setup:**
- Display the previous day's Volume Profile on your chart
- Identify: POC (Point of Control), VAH (Value Area High), VAL (Value Area Low)
- Value Area = the range containing 70% of the previous session's volume

**Entry -- Long (POC Reversion from below):**
1. Price opens below or drops below the previous day's POC
2. Price touches or enters the Value Area Low zone
3. Look for buying pressure (bullish candle, volume increase)
4. Enter long targeting the POC

**Entry -- Short (POC Reversion from above):**
1. Price opens above or rallies above the previous day's POC
2. Price touches or enters the Value Area High zone
3. Look for selling pressure
4. Enter short targeting the POC

**Stop Loss:**
- Below VAL (for longs) or above VAH (for shorts)
- Typically 15-30 MNQ points

**Take Profit:**
- TP1: POC (the main target)
- TP2: Opposite side of the Value Area (VAH for longs, VAL for shorts)

### Statistics
- POC reversion trades have approximately 60-70% success rate in range-bound markets
- The edge diminishes on strong trend days where price breaks away from the value area
- Combining POC with VWAP creates a powerful confluence zone

### Why It Works (The Edge)
- POC represents the price where the market found maximum agreement
- Institutions use VWAP and Volume Profile for execution benchmarks
- Deviations from POC create mean-reversion opportunities because the market "remembers" where the most business was done
- 70% of volume occurs within the Value Area, creating strong gravitational pull

### MNQ Implementation
- Add Volume Profile (Fixed Range, set to previous session) on TradingView
- Mark the previous day's POC, VAH, and VAL before each session
- Use POC as a confluence level for other strategies (e.g., if VWAP bounce happens near POC, double confluence)
- Best for range-bound days; skip this on breakout/trend days
