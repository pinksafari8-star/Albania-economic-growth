#!/usr/bin/env bash
# Reproduce the whole project from the repository root.
set -e
pip install -r requirements.txt
python src/01_fetch_data.py                      # (optional) re-download raw data from the World Bank
python src/02_clean_data.py
python src/03_analysis1_fdi_growth.py
python src/04_analysis2_growth_vs_living_standards.py
python src/05_figures.py
cp figures/*.pdf figures/*.png docs/assets/       # keep website images in sync
