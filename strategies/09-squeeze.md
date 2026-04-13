## 9. Rubber Band / Bollinger-Keltner Squeeze

### Description
The "Squeeze" occurs when Bollinger Bands contract inside Keltner Channels, indicating extremely low volatility. When the bands expand back outside the Keltner Channels, a significant directional move typically follows. Combined with momentum direction (histogram), this identifies high-probability breakouts.

### Exact Rules

**Indicators Required:**
- Bollinger Bands (20-period, 2.0 standard deviations)
- Keltner Channels (20-period, 1.5 ATR)
- Momentum oscillator or histogram (12-period momentum)
- TTM Squeeze indicator (combines all three -- available on TradingView)

**Identifying the Squeeze:**
- Squeeze ON: Bollinger Bands are completely inside Keltner Channels (shown as red dots on TTM Squeeze)
- Squeeze OFF (fired): Bollinger Bands expand back outside Keltner Channels (shown as green dots)

**Entry -- Long:**
1. Squeeze fires (first green dot after one or more red dots)
2. Momentum histogram is above zero and rising
3. Enter on the first green dot candle close
4. Confirmation: price above VWAP

**Entry -- Short:**
1. Squeeze fires (first green dot)
2. Momentum histogram is below zero and falling
3. Enter on the first green dot candle close
4. Confirmation: price below VWAP

**Stop Loss:**
- Below the low of the squeeze range (for longs)
- Above the high of the squeeze range (for shorts)

**Take Profit:**
- 1.5-2x the height of the squeeze range
- Or trail stop using the Keltner Channel midline

### Statistics

| Metric | Value | Notes |
|--------|-------|-------|
| Win Rate (S&P 500, 6-day/1.3 ATR) | ~80% | QuantifiedStrategies.com |
| CAGR | 4.7% | 158 trades, S&P 500 |
| Performance post-2016 | Declined | Strategy may need adaptation |
| Best timeframe | 30-min to Daily | Not ideal for 1-min scalping |

### Why It Works (The Edge)
- Volatility is cyclical: periods of compression (low vol) are always followed by expansion (high vol)
- The squeeze mathematically identifies the compression point
- Momentum direction at the squeeze release predicts the direction of the expansion ~80% of the time
- Combining BB + KC creates a more reliable trigger than either alone

### Best Market Conditions
- Post-consolidation breakouts
- Works on any timeframe but most reliable on 30-min and higher for NQ
- Avoid: already-trending markets (the squeeze fires after compression, not during trends)

### MNQ Implementation
- Add TTM Squeeze indicator to your TradingView chart (5-min or 15-min timeframe)
- When you see red dots (squeeze on), prepare for a trade
- On the first green dot, check momentum histogram direction
- Enter in the direction of momentum
- This is best used as a FILTER for other strategies (e.g., confirming an ORB setup is happening during a squeeze release)
