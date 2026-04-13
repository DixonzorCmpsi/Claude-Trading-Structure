## 2. Gap Fill / Gap Fade

### Description
This strategy trades the statistical tendency of overnight gaps in NQ/MNQ futures to fill (return to the previous day's close) during the regular session. Based on 2,791 trading days of NQ data from January 2015 to December 2025.

### Exact Rules

**Setup:**
- Compare the 9:30 AM ET opening price to the previous day's 4:00 PM ET closing price
- Calculate gap size and classify it:
  - **Tiny gap:** Opens inside the previous day's range (fills 77.8% of the time)
  - **Small gap:** Opens slightly outside the range (fills 42.0%)
  - **Medium gap:** Opens well outside the range (fills 25.6%)
  - **Large gap:** Opens far outside the range (fills 8.2% -- DO NOT TRADE)

**Entry — Gap Up Fade (Short):**
- Gap must be classified as "tiny" or "small" (< 0.5% of price)
- Wait for first 5 minutes of price action (let the initial volatility settle)
- If price fails to continue higher and shows rejection, enter short
- Target: previous day's closing price (the gap fill)

**Entry — Gap Down Fade (Long):**
- Gap must be "tiny" or "small"
- Wait for first 5 minutes
- If price fails to continue lower, enter long
- Target: previous day's closing price

**Stop Loss:**
- Tiny gap: 28 points on NQ average risk (approximately 28 MNQ points = $56/contract)
- Small gap: wider stop needed, scale position size down
- Never fade a large gap (> 1% of price)

**Take Profit:**
- TP1: Previous day's close (the gap fill level)
- TP2: Continue 20-40 points past the close (70% of fills extend at least 20 points beyond)
- Median extension past gap fill: 39.5 NQ points

### Statistics (2,791 Days of NQ Data)

| Metric | Value |
|--------|-------|
| Overall gap fill rate (by close) | 60.3% |
| Tiny gap fill rate | 77.8% |
| Tiny gap + confirmation fill rate | 80-93% |
| Small gap fill rate | 42.0% |
| Large gap fill rate | 8.2% (DO NOT TRADE) |
| Gaps filling in first 5 minutes | 34% |
| Gaps filling by 12:00 PM ET | 86.1% |
| Median drawdown (all gaps) | 44 NQ points |
| P90 drawdown (worst 10%) | 203 NQ points |
| Post-fill up-day probability | 54.5% |

**Day-of-week patterns:**
- Wednesday: 77% gap-down fill rate (highest)
- Tuesday: ~70% fill rate for both gap up and gap down

### Why It Works (The Edge)
- Overnight gaps often represent low-liquidity moves that are not supported by full-session volume
- Institutional algorithms rebalance toward the previous day's value area during regular hours
- Tiny gaps represent noise, not directional intent -- hence the extremely high fill rate
- The edge is entirely statistical: you are trading the base rate probability

### Best Market Conditions
- Tiny and small gaps (< 0.5% move)
- Days without major economic releases at open
- Avoid fading gaps on FOMC days, CPI releases, or earnings-driven moves

### MNQ Implementation
- Before 9:30 AM, note previous close and pre-market price
- Calculate gap size: (Open - PrevClose) / PrevClose * 100
- If gap < 0.25%: high-confidence fade, full position
- If gap 0.25-0.5%: reduced position size
- If gap > 1%: DO NOT TRADE the fade
- Be positioned before 10:00 AM CT (86% of fills happen by 12:00 PM ET)
