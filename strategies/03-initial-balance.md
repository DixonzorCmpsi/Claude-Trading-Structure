## 3. Initial Balance Breakout

### Description
The Initial Balance (IB) is the range established during the first hour of regular trading (9:30-10:30 AM ET). This strategy trades the breakout of that range, exploiting the statistical fact that NQ breaks one side of the IB 73-84% of the time and rarely breaks both sides.

### Exact Rules

**Setup:**
- Mark the high and low of the first 60 minutes (9:30-10:30 AM ET)
- This is your Initial Balance (IB)
- Calculate IB range = IB High - IB Low

**Entry — Long:**
- Price breaks above IB High with a 5-minute candle close
- VWAP slope should be positive (confirming bullish bias)
- Enter on the breakout candle close or first pullback to IB High

**Entry — Short:**
- Price breaks below IB Low with a 5-minute candle close
- VWAP slope should be negative
- Enter on the breakout candle close or first pullback to IB Low

**Stop Loss:**
- Conservative: 25% of IB range below entry (for long) or above entry (for short)
- This gives approximately 70% win rate

**Take Profit:**
- Target: 40% of IB range beyond the breakout level
- Alternative (for trend days): 1.5x IB extension with trailing stop
- One-sided volume with no pullback to IB midpoint = ride the breakout

**Position Management:**
- One trade per session
- If IB is extremely narrow (< 20 MNQ points), skip the day -- breakout likely to be a false one
- If IB is extremely wide (> 100 MNQ points), skip -- insufficient risk/reward

### Statistics

| Metric | Value | Timeframe |
|--------|-------|-----------|
| NQ single-side break probability | 73-84% | Various (Edgeful, Steady Turtle) |
| Single break (6-month rolling) | 82.17% | Edgeful data |
| Double break (both sides broken) | ~16-27% | Derived |
| No break (stays inside IB) | Rare (~5%) | Estimated |

### Why It Works (The Edge)
- The first hour captures the bulk of institutional order flow and price discovery
- Institutions establish their directional bias during this period
- Once the IB is set, market structure tends to follow through in one direction
- The IB acts as a "commitment zone" -- once price exits, institutions defend the breakout

### Best Market Conditions
- Clear trend days (NQ tends to trend more often than ES)
- Days with macro catalysts that establish direction early
- Avoid: Consolidation/chop days, FOMC announcement days (wait until after the announcement)

### MNQ Implementation
- Use 5-minute chart
- Set alarm at 10:30 AM ET to lock in IB levels
- Mark IB High and IB Low with horizontal lines
- Wait for breakout with 5-min close confirmation
- Risk: 25% of IB range per contract
- Target: 40% of IB range (this gives ~70% win rate at ~1.6:1 R:R)
