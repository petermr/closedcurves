#!/bin/bash
set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing package in editable mode..."
pip install -e .

echo "Setup complete! To activate later, run:"
echo "  source .venv/bin/activate"
