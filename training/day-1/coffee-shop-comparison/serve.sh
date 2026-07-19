#!/usr/bin/env bash
# Serve the coffee shop comparison app (required for fetch() to load the CSV).
set -euo pipefail
cd "$(dirname "$0")"
PORT="${PORT:-8080}"
echo "Open http://127.0.0.1:${PORT}/index.html"
exec python3 -m http.server "$PORT"
