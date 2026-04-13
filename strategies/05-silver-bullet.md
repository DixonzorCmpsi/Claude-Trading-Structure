## 5. ICT Silver Bullet

### Description
The ICT Silver Bullet is a time-window-based strategy that restricts entries to three specific one-hour windows where institutional displacement is statistically most likely to occur. Originally designed and tested on NQ futures and ES futures by Inner Circle Trader (Michael J. Huddleston).

### Exact Rules

**Time Windows (Pick ONE per day):**
1. **London Open:** 3:00-4:00 AM ET (winter) / 2:00-3:00 AM ET (summer)
2. **NY AM Session:** 10:00-11:00 AM ET (HIGHEST PROBABILITY for NQ)
3. **NY PM Session:** 2:00-3:00 PM ET

**Setup (before the window opens):**
1. Determine daily bias using higher timeframe analysis (daily/4H trend)
2. On the 15-minute chart, identify nearby liquidity levels:
   - Buy-Side Liquidity (BSL): obvious highs where stops are resting above
   - Sell-Side Liquidity (SSL): obvious lows where stops are resting below
3. Wait for the chosen time window to open

**Entry Steps (during the window):**
1. Observe a liquidity sweep: price raids above BSL or below SSL
2. On the 1-minute or 3-minute chart, look for a Market Structure Shift (MSS) -- a break of structure in the opposite direction of the sweep
3. After the MSS, look for a Fair Value Gap (FVG) forming in the same direction as the MSS
4. Enter when price returns to fill or touch the FVG zone
5. Entry is inside the FVG, typically at the 50% level of the gap (CE -- Consequent Encroachment)

**Stop Loss:**
- Below the low of the liquidity sweep (for longs)
- Above the high of the liquidity sweep (for shorts)
- Typically 10-25 MNQ points

**Take Profit:**
- Minimum 2R (risk-to-reward)
- Target the next liquidity level (opposite side highs/lows)
- For the 10-11 AM window: target afternoon session levels

### Statistics

| Metric | Value | Conditions |
|--------|-------|------------|
| Win Rate (every FVG, no filter) | 55-60% | Mechanical, no bias filter |
| Win Rate (with daily bias + SMC alignment) | 72-83% | Filtered, higher conviction |
| Profit Factor (unfiltered) | 1.5-1.8 | All signals taken |
| Profit Factor (filtered) | 2.5+ | Only aligned with daily bias |
| Best Window for NQ | 10:00-11:00 AM ET | NY AM session |

### Why It Works (The Edge)
- The 10:00-11:00 AM window sits at the overlap of London and New York kill zones
- By 10:00 AM, initial opening volatility has settled, revealing true institutional intent
- Liquidity sweeps during these windows represent institutional order filling
- The time restriction eliminates overtrading and forces patience

### Best Market Conditions
- Volatile sessions with clear liquidity levels
- Days where pre-market established obvious highs/lows to be swept
- NQ is one of the two instruments this strategy was specifically designed for

### MNQ Implementation
- Focus exclusively on the 10:00-11:00 AM ET window to start
- Use 15-minute chart to identify liquidity levels before 10:00 AM
- Switch to 1-minute chart at 10:00 AM sharp
- Wait for sweep + MSS + FVG sequence
- If the sequence does not complete by 11:00 AM, no trade for the day
- Maximum 1 trade per window
