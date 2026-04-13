# TradingView MCP — Quick Reference

The MCP server self-describes its tools. This file covers **routing** and **conventions** only.

## Decision Tree — Which Tools When

- **Chart state:** `chart_get_state` (call first) → `data_get_study_values` → `quote_get`
- **Pine indicator output** (lines/labels/tables/boxes): `data_get_pine_*` tools with `study_filter`
- **Price data:** `data_get_ohlcv` (always `summary: true` unless you need bars) or `quote_get`
- **Full chart analysis:** quote → study values → pine lines/labels/tables → OHLCV summary → screenshot
- **Change chart:** `chart_set_symbol`, `chart_set_timeframe`, `chart_set_type`, `chart_manage_indicator`
- **Pine Script:** `pine_set_source` → `pine_smart_compile` → `pine_get_errors` → `pine_get_console`
- **Replay:** `replay_start` → `replay_step`/`replay_autoplay` → `replay_trade` → `replay_status` → `replay_stop`
- **Drawing:** `draw_shape`, `draw_list`, `draw_remove_one`, `draw_clear`
- **Alerts:** `alert_create`, `alert_list`, `alert_delete`
- **Screenshots:** `capture_screenshot` (regions: "full", "chart", "strategy_tester")
- **Multi-symbol:** `batch_run` with symbols array
- **Connection issues:** `tv_launch`, `tv_health_check`

## Conventions

- Entity IDs from `chart_get_state` are **session-specific** — never cache across sessions
- Pine indicators must be **visible** on chart for `data_get_pine_*` tools to work
- `chart_manage_indicator` requires **full names** ("Relative Strength Index", not "RSI")
- Always use `study_filter` on pine tools to target specific indicators
- Never use `verbose: true` on pine tools unless the user asks for raw data
- Avoid `pine_get_source` on complex scripts (can return 200KB+)
- OHLCV: always pass `summary: true` unless individual bars are needed; cap at `count: 100`
- Pine labels capped at 50 per study (pass `max_labels` to override)
