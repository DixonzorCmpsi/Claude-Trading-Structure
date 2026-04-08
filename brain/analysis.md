# Analysis — Pattern Recognition Layer

> You have been routed here with a Market Snapshot from eyes.md.
> Your job: identify setups, confluences, and structure. No decisions yet.

## Purpose
Take the Market Snapshot and determine IF a tradeable setup exists.
Output a Setup Assessment that decision.md consumes.

## Step 1: Bias Confirmation
From the Market Snapshot:
- Is 4H bias clear? (Not sideways/choppy)
- Does 1H agree with 4H? → Determines execution timeframe
- Per TJR (knowledge.md): "Higher time frame holds higher power"
- If 4H is unclear → OUTPUT: No clear bias. NO SETUP.

## Step 2: Apply the TJR System (reference knowledge.md)

### Check 1: High Timeframe Liquidity
Has price swept a significant high or low?
- Hourly highs/lows swept? (for 5-min execution)
- 4H highs/lows swept? (for 15-min execution)
- Pre-market sweep already happened?
- If NO sweep: check for hourly confluences (FVG, OB, breaker, equilibrium)
- If NOTHING: No setup yet. WAIT.

### Check 2: Break of Structure (BOS)
On the execution timeframe (5-min or 15-min):
- Has there been a BOS in the bias direction?
- BOS must be a candle CLOSE past the level, not just a wick
- If NO BOS: Setup is not ready. WAIT.

### Check 3: Third Confluence
After BOS, has price retraced into one of:
- [ ] Order block
- [ ] Fair value gap (FVG)
- [ ] Breaker block
- [ ] Equilibrium (50% level)
- [ ] Balanced price range (BPR) — highest quality
- If NO confluence: No entry yet. WAIT for retracement.

### Check 4: Confirmation
At the confluence, look for:
- A candle closing out of the zone in the bias direction?
- Or a lower-timeframe BOS as entry trigger?
- If NO confirmation: Setup exists but is not ready. WAIT.

## Step 3: Cross-Reference with Strategies (reference strategies.md)

Does this setup overlap with any known high-probability strategy?
- **Opening Range Breakout** (if within first 15 min range) — 71-75% win rate
- **Gap Fill** (if overnight gap present) — 78-93% win rate
- **Initial Balance Breakout** (if testing IB range) — 73-84% break rate
- **VWAP Pullback** (if price is at VWAP) — high consistency
- **ICT Silver Bullet** (if within 10:00-11:00 AM window) — 72-83% win rate
- **Connors RSI(2)** (if RSI(2) below 5 above 200 SMA) — 75-91% win rate

Overlapping strategies = higher confluence. Note which ones align.

## Step 4: Define Trade Parameters
IF a setup exists, calculate:
- **Entry price:** [exact level]
- **Stop loss:** [exact level, using TJR's 3-level system]
  - Level 1: Above/below the liquidity sweep (tightest)
  - Level 2: Above/below the swing inside the confluence
  - Level 3: Above/below the entire confluence zone (widest)
- **Stop loss in points:** [calculate]
- **Risk in dollars:** [stop points x $2 per contract]
- **Take profit:** [at high timeframe liquidity draws]
- **R:R ratio:** [must be at least 2:1 per rules.md R13]

## Step 5: THE $250 REALITY CHECK

This is critical. Reference .claude/rules/03-account-profile.md:
- Account: $250 → 2% max risk = $5.00
- Max stop loss = $5.00 / $2.00 per point = **2.5 MNQ points**
- Is the calculated stop within 2.5 points?

If YES → Setup fits our account. Proceed.
If NO → "This setup is valid but the stop is too wide for your account.
  Options: (1) Paper trade this one, (2) Wait for a tighter entry on lower TF,
  (3) Accept higher risk (NOT recommended)."

Be honest. Do not force trades that don't fit the risk math.

## Output: Setup Assessment

```
SETUP ASSESSMENT
- Setup Found: [Yes / No / Developing]
- TJR System Stage: [which step — 1 through 8]
- Bias: [Long / Short / None]
- Entry: [price or "not ready"]
- Stop Loss: [price] ([X] points = $[Y] risk)
- Take Profit: [price] ([X] points = $[Y] reward)
- R:R: [ratio]
- Risk vs Account: [fits 2% rule? Yes/No — $X of $250]
- Confluences Present: [list]
- Overlapping Strategies: [list from strategies.md]
- Confidence: [Low / Medium / High — based on confluence count]
- Warning: [wide stop, low volume, news, dead zone, etc.]
```
