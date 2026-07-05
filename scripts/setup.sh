#!/bin/bash
set -euo pipefail
echo "Setting up Fraud Detection Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
