## 1. Opening Range Breakout (ORB)

### Description
The ORB strategy identifies the high and low of the first 15 minutes of regular trading hours (9:30-9:45 AM ET), then trades the breakout when price closes a full 5-minute candle outside that range. This is one of the most backtested and automatable strategies in existence for NQ/MNQ futures.

### Exact Rules

**Setup:**
- Chart: 5-minute timeframe on MNQ
- Mark the high and low of the first 15 minutes (9:30-9:45 AM ET)
- This is your "opening range"

**Entry — Long:**
- Wait for a full 5-minute candle to CLOSE above the opening range high
- Volume on the breakout candle must exceed 1.5x the average volume (optional but recommended filter)
- Enter at the close of the breakout candle

**Entry — Short:**
- Wait for a full 5-minute candle to CLOSE below the opening range low
- Same volume confirmation
- Enter at the close of the breakout candle

**Stop Loss:**
- Place stop at the opposite side of the opening range
- Cap maximum risk at 50 points on NQ ($100 on MNQ per contract)

**Take Profit:**
- Primary target: 50% of the opening range height, measured from the breakout level
- Alternative: Trail stop after 1R is reached

**Position Management:**
- One trade per direction per session
- Maximum one trade per day for beginners
- Close all positions by 3:45 PM ET

### Backtested Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Win Rate | 74.56% | Trade That Swing (NQ, 114 trades) |
| Profit Factor | 2.512 | Trade That Swing |
| Total Return | +433% | $10,000 account, 1 NQ contract, 1 year |
| Max Drawdown | 12% (~$2,725) | Trade That Swing |
| MNQ-Specific Win Rate | 71% | TradingView backtest (Sep 2025-Apr 2026) |
| MNQ Profit Factor | 1.624 | TradingView backtest |
| MNQ Max Drawdown | 11.27% | TradingView backtest |

### Why It Works (The Edge)
- The first 15 minutes captures initial institutional positioning
- Breakouts from this range show where smart money wants to take price for the session
- The 5-minute close requirement eliminates most false breakouts (vs. just a wick above/below)
- Volume confirmation further filters out low-conviction moves

### Best Market Conditions
- Trending days with clear directional bias
- Days with significant overnight moves or news catalysts
- Avoid: low-volatility, narrow-range days where the opening range is tiny (< 15 MNQ points)

### MNQ Implementation
- Use 5-minute chart on TradingView
- Mark 9:30-9:45 AM ET high/low with horizontal lines
- Set alerts at opening range high + 1 tick and opening range low - 1 tick
- Risk per trade: 10-20 MNQ points (depending on opening range size)
- Start with 1 MNQ contract
