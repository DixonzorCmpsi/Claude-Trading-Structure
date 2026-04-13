# TJR Core — Live Trading Cheat Sheet

> For the full TJR guide, see `knowledge.md` in project root.

---

## Kill Zones

| Session | Window | Notes |
|---------|--------|-------|
| AM Kill Zone | 9:50 - 10:10 AM ET | Primary. 4H candle closes at 10:00 AM. Never trade before 9:50. |
| PM Kill Zone | 1:30 - 3:00 PM ET | Lower volatility. Use lower TFs (15m bias, 5m liquidity, 1m entry). |
| Pre-market | 8:30 AM ET | Observe only. Check if sweeps already happened. |

---

## 7 Core Confluences

**1. Liquidity** — Resting orders above highs (buy-side) and below lows (sell-side) act as magnets. Institutions sweep these pools to fill large orders, then reverse. The market is drawn toward liquidity before it can change direction.

**2. Order Blocks** — The price range where large orders caused a directional move. A bearish OB is the leg UP before a downside BOS; a bullish OB is the leg DOWN before an upside BOS. If price revisits the OB and shows pressure in the expected direction, continuation is likely.

**3. Fair Value Gaps (FVGs)** — A 3-candle imbalance: the gap between candle 1's wick and candle 3's wick (no overlap = FVG exists). Price revisiting the FVG with matching pressure suggests continuation. Invalidated if price closes through it — an invalidated FVG in the opposite direction can serve as entry confluence.

**4. Balanced Price Range (BPR)** — The overlap zone where a bullish FVG and bearish FVG occupy the same price range. High-quality imbalance area that price strongly reacts from. Best used on execution TFs (5m, 1m) for precise entries.

**5. Equilibrium** — The 50% level of a swing (Gann Box). In an uptrend, below 50% = discount (buy zone); above = premium. In a downtrend, above 50% = discount (sell zone); below = premium. Institutions seek the best price — they buy discount, sell premium.

**6. Breaker Blocks** — A failed retracement zone: the move prior to a BOS that broke through the previous trend's structure. This zone now lacks orders in the old direction. If price revisits and shows pressure in the new direction, continuation is likely. Often overlaps with FVGs.

**7. SMT Divergence** — One index forecasting another (e.g., NQ vs ES). Bullish SMT: one makes a higher low while the other makes a lower low. Bearish SMT: one makes a lower high while the other makes a higher high. Must align with your bias. Use on 5m/15m, not 1m.

---

## The Strategy (Step by Step)

1. **Bias** — 4H trend direction. Uptrend = bullish, downtrend = bearish. Do not predict reversals.
2. **Execution TF** — 1H in line with 4H? Use 5m. 1H opposite 4H? Use 15m.
3. **Mark liquidity** — 1H and 4H highs/lows as draws on liquidity.
4. **Wait for sweep** — HTF liquidity sweep or HTF confluence hit. Hands off until then.
5. **Break of structure** — On execution TF, in bias direction.
6. **Third confluence** — Price retraces into OB, FVG, breaker, or equilibrium.
7. **Confirmation** — Pressure candle out of confluence, or lower TF BOS.
8. **Execute** — Stop loss at sweep level or confluence zone. TP at HTF draws/confluences.

---

## Quick Reference: Strategy Checklist

```
BEFORE MARKET OPEN:
[ ] Check 4H trend -> Bullish or Bearish? (This is your bias)
[ ] Check 1H trend -> In line with 4H?
    -> Yes: Execute on 5-min
    -> No:  Execute on 15-min
[ ] Mark high time frame liquidity levels (1H and 4H highs/lows)
[ ] Check if pre-market already caused a sweep

DURING SESSION (9:50 AM - 10:10 AM kill zone):
[ ] Wait for high time frame liquidity sweep OR HTF confluence hit
[ ] Scale to execution time frame (5-min or 15-min)
[ ] Wait for break of structure in bias direction
[ ] Wait for third confluence (FVG, order block, breaker, equilibrium)
[ ] Confirm: pressure candle out of confluence OR lower TF BOS
[ ] Execute trade
[ ] Stop loss: Above/below liquidity sweep, or confluence zone
[ ] Take profit: At HTF draws on liquidity / confluences

AFTER TRADE:
[ ] Do NOT move stop loss or take profit
[ ] Journal the trade -- win or loss
[ ] Identify what worked and what didn't
```

---

## Stop Loss Levels

1. **Level 1** — Above/below the liquidity sweep (most conservative, best R:R)
2. **Level 2** — Above/below the swing point inside the confluence zone
3. **Level 3** — Above/below the entire confluence zone (most room, worst R:R)

## Take Profit Rules

- Set at HTF confluences where price could reverse (1H/4H draws, OBs, FVGs, breakers)
- Match TP timeframe to entry TF (5m entry -> 1H/4H TP; 1m entry -> 15m/5m TP)
- Never move TP. Never move SL. Set and forget.
