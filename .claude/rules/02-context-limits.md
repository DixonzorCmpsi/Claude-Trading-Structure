# Context Management Rules

These TradingView MCP tools can return large payloads. Follow these rules to avoid context bloat:

1. **Always use `summary: true` on `data_get_ohlcv`** unless you specifically need individual bars
2. **Always use `study_filter`** on pine tools when you know which indicator you want
3. **Never use `verbose: true`** on pine tools unless the user asks for raw drawing data
4. **Avoid calling `pine_get_source`** on complex scripts — can return 200KB+
5. **Avoid calling `data_get_indicator`** on protected indicators — use `data_get_study_values` instead
6. **Use `capture_screenshot`** for visual context instead of pulling large datasets
7. **Call `chart_get_state` once** at the start, then reference entity IDs
8. **Cap OHLCV requests** — `count: 20` for quick, `count: 100` for deep, `count: 500` only when needed

## Output Size Estimates

| Tool | Typical Output |
|------|---------------|
| `quote_get` | ~200 bytes |
| `data_get_study_values` | ~500 bytes |
| `data_get_pine_lines` | ~1-3 KB per study |
| `data_get_pine_labels` | ~2-5 KB per study |
| `data_get_pine_tables` | ~1-4 KB per study |
| `data_get_pine_boxes` | ~1-2 KB per study |
| `data_get_ohlcv` (summary) | ~500 bytes |
| `data_get_ohlcv` (100 bars) | ~8 KB |
| `capture_screenshot` | ~300 bytes (returns file path) |
