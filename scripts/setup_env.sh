#!/usr/bin/env bash
# =============================================================================
# One-time environment bootstrap:
#   - creates a virtualenv
#   - installs requirements.txt
#   - downloads required NLTK corpora + spaCy model
#
# Usage:  bash scripts/setup_env.sh
# =============================================================================
set -e

echo ">> Creating virtual environment (venv/)..."
python3 -m venv venv

echo ">> Activating venv and installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ">> Downloading spaCy model (en_core_web_sm)..."
python -m spacy download en_core_web_sm

echo ">> Downloading NLTK corpora (punkt, stopwords)..."
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"

echo ">> Installing project in editable mode..."
pip install -e .

echo ""
echo "Setup complete. Activate with:  source venv/bin/activate"
echo "(Windows: venv\\Scripts\\activate)"
