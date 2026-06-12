#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv-browser-use"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required for the Browser Use integration."
  echo "Install uv first: https://docs.astral.sh/uv/"
  exit 1
fi

cd "$ROOT"

if [ -d "$VENV" ]; then
  echo "Reusing existing Browser Use virtual environment: $VENV"
else
  echo "Creating Browser Use virtual environment..."
  uv venv --python 3.12 "$VENV"
fi

echo "Installing Browser Use dependencies..."
uv pip install --python "$VENV/bin/python" browser-use python-dotenv

echo "Installing Browser Use browser runtime..."
uvx browser-use install

if [ ! -f "$ROOT/.env" ]; then
  cat > "$ROOT/.env.example" <<'EOF'
# Pick one provider.
# Browser Use Cloud:
BROWSER_USE_API_KEY=

# Or OpenAI:
OPENAI_API_KEY=
HERMES_BROWSER_USE_LLM=openai
HERMES_BROWSER_USE_MODEL=gpt-4.1-mini
EOF
  echo "Created .env.example. Copy it to .env and add your API key."
fi

echo
echo "Browser Use integration installed."
echo "Run:"
echo "  $VENV/bin/python scripts/run_browser_use_task.py --dry-run --task \"Open example.com\""
