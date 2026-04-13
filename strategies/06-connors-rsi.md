## 6. Mean Reversion -- Connors RSI(2)

### Description
Developed by Larry Connors, this strategy uses a 2-period RSI (not the standard 14-period) to identify extreme short-term oversold/overbought conditions. When RSI(2) reaches extreme levels, the statistical tendency is for price to snap back. This has been backtested across decades of market data with consistently high win rates.

### Exact Rules

**Indicators Required:**
- 200-period SMA (trend filter)
- 2-period RSI (signal generator)
- Standard OHLCV chart (daily bars for position, 5-min bars for intraday adaptation)

**Entry — Long (Mean Reversion Buy):**
1. Price must be ABOVE the 200-period SMA (only buy in uptrends)
2. RSI(2) drops below 5 (extreme oversold on 2-period lookback)
3. Enter long at the close of the bar where RSI(2) < 5
4. More aggressive: enter when RSI(2) < 10

**Entry — Short (Mean Reversion Sell):**
1. Price must be BELOW the 200-period SMA (only short in downtrends)
2. RSI(2) rises above 95 (extreme overbought)
3. Enter short at the close of the bar where RSI(2) > 95

**Exit:**
- Exit long when RSI(2) rises above 65 (some variants use 55 or 70)
- Exit short when RSI(2) drops below 35
- Alternative exit: when price crosses back above the 5-period SMA

**Stop Loss:**
- Fixed stop at 2x ATR (14-period) below entry
- Or use the recent swing low as the stop

### Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Win Rate (buy below RSI 5) | ~75-82% | QuantifiedStrategies.com |
| Win Rate (buy below RSI 10) | ~70-75% | QuantifiedStrategies.com |
| Profit Factor | ~2.0-2.08 | 288 trades, S&P 500 |
| Win Rate (Connors RSI variant, CRSI < 15) | ~75% | QuantifiedStrategies.com |
| Win Rate (RSI 2 on S&P 500, 1993-2025) | ~91% | Aggressive variant |

**Key finding:** Returns were higher when buying on RSI dips below 5 than on dips below 10. The more extreme the oversold reading, the higher the subsequent return.

### Why It Works (The Edge)
- Short-term price moves are largely mean-reverting in equity indices
- A 2-period RSI captures the most extreme short-term dislocations
- The 200 SMA filter ensures you only buy dips in uptrends (going with the long-term flow)
- Institutions create these short-term dislocations, then buy back at better prices

### Best Market Conditions
- Uptrending markets (for long side) -- the 200 SMA filter ensures this
- Works best during pullbacks within a larger trend
- Less effective during sustained crashes or one-directional moves
- Historically, mean reversion works well in volatile/bear markets due to larger oversold snaps

### MNQ Implementation (Intraday Adaptation)
- Use 5-minute chart with 200-period SMA and 2-period RSI
- When 5-min RSI(2) drops below 5 AND price is above the 200 SMA on the 5-min chart: enter long
- Exit when RSI(2) crosses back above 55-65
- Stop: below the swing low that created the RSI(2) < 5 reading
- This is best used as a "second chance" entry when combined with a VWAP or key level test
- Note: Intraday adaptation has less historical backing than daily bars -- use as supplementary confluence
