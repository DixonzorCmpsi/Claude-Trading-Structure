## 8. ICT Power of 3 (AMD)

### Description
The Accumulation-Manipulation-Distribution (AMD) framework describes the three phases of every trading day. Originally developed for NQ and ES futures. Rather than a specific entry signal, this is a market structure framework that tells you WHEN and WHERE to enter.

### Exact Rules

**Phase 1 -- Accumulation (9:30-10:00 AM ET typically):**
- Price ranges near the opening price
- Smart money accumulates positions
- Identify the range (tight consolidation zone)
- Mark the high and low of this range

**Phase 2 -- Manipulation (10:00-10:30 AM ET typically):**
- Price makes a FALSE move:
  - Bullish day: price dips BELOW the accumulation range (sweeping sell-side liquidity)
  - Bearish day: price spikes ABOVE the accumulation range (sweeping buy-side liquidity)
- This move traps retail traders on the wrong side

**Phase 3 -- Distribution (10:30 AM - 3:00 PM ET):**
- Price moves aggressively in the TRUE direction
- Bullish: strong rally after the manipulation dip
- Bearish: strong sell-off after the manipulation spike

**Entry:**
- Enter after the manipulation phase completes
- For longs: when price closes above the accumulation range high after first dipping below the range low
- For shorts: when price closes below the accumulation range low after first spiking above the range high

**Stop Loss:**
- At the manipulation phase extreme (the low of the manipulation dip for longs, the high of the spike for shorts)

**Take Profit:**
- 1:2 risk-to-reward minimum
- Target: the next significant liquidity level (prior day high/low, weekly level)
- Distribution phase can run for hours on trend days

### Statistics
- Reported win rates: 60-70% when the daily bias is correctly identified
- The framework overlaps heavily with the Initial Balance and ORB strategies
- No large-scale independent backtest available -- it is primarily a discretionary framework

### Why It Works (The Edge)
- Institutions need to fill large orders at favorable prices
- They accumulate during the quiet phase, manipulate to grab retail stops, then distribute in the intended direction
- The manipulation phase creates the highest probability entry point because it represents the exhaustion of counter-trend orders
- This pattern repeats daily because institutional execution algorithms follow this cycle

### Best Market Conditions
- Trending days with clear institutional participation
- Days with overnight moves followed by a regular-session reversal (manipulation)
- Best when combined with ICT Silver Bullet time windows

### MNQ Implementation
- Watch for tight consolidation in first 15-30 minutes after open
- When price breaks one side of the range then quickly reverses, that is the manipulation
- Enter in the direction of the reversal once price closes back inside or beyond the range
- Stop at manipulation extreme, target 2R minimum
- Combine with VWAP: manipulation often coincides with a VWAP test
