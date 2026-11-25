# FDI, Economic Growth and Living Standards in Albania, 2010–2025

Individual project for *Advanced Mathematics* (VUB). Author: **Ergita**

**Website:** *coming soon (will be added in a later commit)*

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

## Plan
1. Download and clean the data (this commit: download script and raw data).
2. Run two analyses in Python: FDI vs growth; growth vs living standards.
3. Make two PDF figures and a website, and finish this README with findings and the website URL.

*Work in progress. Results will be added in later commits.*
