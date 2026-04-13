# High-Consistency Day Trading Strategies for MNQ Futures

> For our primary strategy (VWAP + FVG), see brain/specialization.md

## Strategy Comparison Matrix

| # | Strategy | Win Rate | Profit Factor | Trades/Day | Best Conditions | Complexity |
|---|----------|----------|---------------|------------|-----------------|------------|
| 1 | Opening Range Breakout | 71-75% | 1.6-2.5 | 1 | Trending days | Low |
| 2 | Gap Fill (Tiny Gaps) | 78-93% | ~2.0 | 0-1 | Gap days | Low |
| 3 | Initial Balance Breakout | 73-84% | ~1.8 | 1 | Trending days | Low |
| 4 | VWAP Pullback | 60-65% | ~1.5 | 1-3 | Trending days | Medium |
| 5 | ICT Silver Bullet | 55-83% | 1.5-2.5+ | 1 | Volatile sessions | Medium |
| 6 | Connors RSI(2) | 75-91% | ~2.0 | 0-1 | Oversold bounces | Low |
| 7 | SMC (Sweep + FVG) | 61% | 2.17 | 1-2 | All conditions | High |
| 8 | Power of 3 (AMD) | 60-70% | ~1.8 | 1 | Trending days | High |
| 9 | BB/KC Squeeze | ~80% | ~1.5 | 0-1 | Post-compression | Medium |
| 10 | PDH/PDL Levels | 55-65% | ~1.5 | 1-2 | Breakout/fade days | Medium |
| 11 | Volume Profile POC | 60-70% | ~1.6 | 1-2 | Range-bound days | Medium |
| 12 | EMA Cross + VWAP | 50-60% | ~1.3 | 1-3 | Trending days | Low |

## Individual Strategy Files

1. [Opening Range Breakout (ORB)](01-orb.md) -- Most backtested breakout strategy; 15-min opening range with 5-min close confirmation
2. [Gap Fill / Gap Fade](02-gap-fill.md) -- Statistical gap fade based on 2,791 days of NQ data; tiny gaps fill 78-93%
3. [Initial Balance Breakout](03-initial-balance.md) -- First-hour range breakout; NQ breaks one side 73-84% of the time
4. [VWAP Pullback / Bounce](04-vwap-pullback.md) -- Institutional fair value pullback entries in trending markets
5. [ICT Silver Bullet](05-silver-bullet.md) -- Time-window entries (10-11 AM ET) with liquidity sweep + FVG
6. [Connors RSI(2) Mean Reversion](06-connors-rsi.md) -- Extreme short-term oversold/overbought snaps; 75-91% win rate
7. [Smart Money Concepts (Liquidity Sweep + FVG)](07-smc.md) -- Full institutional order flow framework; 2,600-trade backtest
8. [ICT Power of 3 (AMD)](08-power-of-3.md) -- Accumulation-Manipulation-Distribution daily structure
9. [Bollinger-Keltner Squeeze](09-squeeze.md) -- Volatility compression breakout; ~80% directional accuracy
10. [Previous Day High/Low Fade & Breakout](10-pdh-pdl.md) -- Universal liquidity levels for fade and breakout plays
11. [Volume Profile POC Reversion](11-volume-profile.md) -- Mean reversion to previous session's point of control
12. [EMA Crossover + VWAP Filter](12-ema-vwap.md) -- Simple trend confirmation tool; best as secondary signal

## Cross-Cutting Reference

- [Key Principles & MNQ Considerations](principles.md) -- Expectancy formula, risk rules, confluence stacking, time windows, contract specs
