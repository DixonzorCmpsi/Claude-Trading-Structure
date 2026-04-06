#!/bin/bash
# ============================================================
# Start Trading Session
# Launches TradingView with debug port, then opens a terminal
# cd'd into the project so you can run Claude Code.
# ============================================================

PORT=9222
PROJECT_DIR="$HOME/Documents/hobby/Claude-Trading-Structure"

# --- Find TradingView ---
APP=""
LOCATIONS=(
  "/Applications/TradingView.app"
  "$HOME/Applications/TradingView.app"
)

for loc in "${LOCATIONS[@]}"; do
  if [ -d "$loc" ]; then
    APP="$loc"
    break
  fi
done

# Fallback: Spotlight search
if [ -z "$APP" ]; then
  APP=$(mdfind "kMDItemCFBundleIdentifier == 'com.niceincontact.TradingView'" 2>/dev/null | head -1)
fi
if [ -z "$APP" ] || [ ! -d "$APP" ]; then
  APP=$(mdfind "kMDItemKind == 'Application' && kMDItemFSName == 'TradingView.app'" 2>/dev/null | head -1)
fi

if [ -z "$APP" ] || [ ! -d "$APP" ]; then
  echo "TradingView Desktop not found!"
  echo "Download it from: https://www.tradingview.com/desktop/"
  read -p "Press Enter to exit..."
  exit 1
fi

echo "Found TradingView at: $APP"

# --- Kill existing TradingView (to relaunch with debug port) ---
pkill -f "TradingView" 2>/dev/null
sleep 2

# --- Launch TradingView with Chrome DevTools Protocol ---
echo "Launching TradingView with debug port $PORT..."
nohup "$APP/Contents/MacOS/TradingView" --remote-debugging-port=$PORT > /dev/null 2>&1 &
echo "PID: $!"
sleep 5

# --- Wait for CDP to be ready ---
echo "Waiting for CDP connection..."
for i in $(seq 1 20); do
  if curl -s "http://localhost:$PORT/json/version" > /dev/null 2>&1; then
    echo "TradingView CDP ready on port $PORT"
    break
  fi
  sleep 1
done

# --- Open a Terminal cd'd to the project folder ---
echo "Opening terminal at $PROJECT_DIR..."
osascript -e "tell application \"Terminal\"
  activate
  do script \"cd $PROJECT_DIR && echo 'Ready. Run: claude' && echo ''\"
end tell"

echo ""
echo "TradingView is running with debug port."
echo "In the new terminal, type: claude"
echo ""
