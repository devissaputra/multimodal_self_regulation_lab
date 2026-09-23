#!/usr/bin/env bash
set -euo pipefail
python -m compileall -q src
PYTHONPATH=src pytest -q
PYTHONPATH=src python examples/demo.py
echo "Reproduction complete. See results/."
