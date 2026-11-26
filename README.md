# FDI, Economic Growth and Living Standards in Albania, 2010–2025

Individual project for *Advanced Mathematics* (VUB). Author: **Ergita**

**Website:** [WEBSITE_URL — add after publishing with GitHub Pages]

## Research question
> Has foreign direct investment contributed to Albania's economic growth, and has this growth translated into improved living standards for ordinary citizens?

Made measurable as two parts:
1. Is the FDI share of GDP statistically associated with annual real GDP growth in Albania (2010–2025)?
2. Did growth in output per person carry through to household consumption per person, and what do unemployment, inflation and population add?

The 2026 *Flamingo Revolution* protests are used only as political context. The data end in 2025, so nothing here tests what caused or followed the protests. All results are **associations, not causal effects**.

## Data
All data: World Bank *World Development Indicators* (WDI), Albania, 2010–2025, downloaded through the World Bank API on 25 Nov 2026 by `src/01_fetch_data.py`. No missing values. Indicator codes are in `data/raw/wdi_indicator_metadata.csv`:
FDI net inflows (% of GDP and current US$), real GDP growth, GDP per capita (constant 2015 US$ and PPP), household consumption per capita (constant US$), unemployment (total, youth), CPI inflation, remittances (% of GDP), population.
Average wages and inequality measures are not available as a consistent WDI series, so they are not used (see Limitations).

## Analyses
1. **FDI and growth** (`src/03_analysis1_fdi_growth.py`): descriptive statistics, Pearson/Spearman correlation, simple OLS regression, one-year lag, robustness check excluding 2020–21.
2. **Growth vs living standards** (`src/04_analysis2_growth_vs_living_standards.py`): index numbers, CAGR, consumption-to-GDP ratio, sub-period comparison, regression of consumption growth on GDP-per-capita growth.

## Main findings
- FDI averaged 7.8% of GDP and has trended down (−0.17 pp/year). Its correlation with GDP growth is **not statistically significant** (same year: r = −0.21, p = 0.43; lagged: r = −0.31, p = 0.27; excl. COVID years: r = −0.46, p = 0.096). With n ≈ 15 the test has low power, so this is "no clear evidence", not "no effect".
- Real GDP per capita rose **+92%** (2010→2025); household consumption per capita rose **+72%**; population fell **−19%**.
- Household consumption fell from 78.1% to 70.0% of GDP per capita.
- Annual consumption growth tracks GDP-per-capita growth closely (slope 0.86, R² = 0.66).
- Unemployment peaked at 18.1% in 2014 and was 10.9% in 2025.

## Repository structure
```
├── README.md
├── requirements.txt
├── run_all.sh                 # reproduces everything
├── data/
│   ├── raw/                   # as downloaded from the World Bank API
│   └── processed/             # cleaned data with derived variables
├── src/                       # 01 fetch, 02 clean, 03 analysis 1, 04 analysis 2, 05 figures
├── results/                   # CSV outputs of the analyses
├── figures/                   # figure1_*.pdf, figure2_*.pdf (+ PNG copies)
├── explanations/              # beginner explanations and exam preparation
└── docs/                      # the website (index.html, style.css, script.js, assets/), served by GitHub Pages
```

## Reproduce
```bash
pip install -r requirements.txt
bash run_all.sh        # or run the scripts in src/ in numerical order
```
Python 3.10+. Re-downloading may give slightly different numbers if the World Bank has revised its data.

## Limitations
Small sample; correlation not causation; national averages only (no wages/inequality); modelled and revised data; no formal time-series tests; data end before the 2026 protests.

## Data licence and sources
World Bank WDI data are published under CC BY 4.0. See the website's reference list for all sources.
