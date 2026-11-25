"""
01_fetch_data.py
Download Albania's indicators from the World Bank World Development Indicators (WDI) API
and save them as CSV files in data/raw/.

Run from the repository root:
    python src/01_fetch_data.py

Nothing is invented here: every number written to disk comes straight from the
World Bank API. The retrieval date is stored so the dataset is citable.
"""
from datetime import date
from pathlib import Path

import pandas as pd
import requests

COUNTRY = "ALB"
START, END = 2010, 2025

# WDI code -> short column name used in the analysis
INDICATORS = {
    "BX.KLT.DINV.WD.GD.ZS": "fdi_pct_gdp",            # FDI net inflows, % of GDP
    "BX.KLT.DINV.CD.WD": "fdi_usd",                   # FDI net inflows, current US$
    "NY.GDP.MKTP.KD.ZG": "gdp_growth_pct",            # real GDP growth, annual %
    "NY.GDP.PCAP.KD": "gdp_pc_const_usd",             # GDP per capita, constant 2015 US$
    "NY.GDP.PCAP.PP.KD": "gdp_pc_ppp_const",          # GDP per capita, PPP, constant intl $
    "NE.CON.PRVT.PC.KD": "hh_consumption_pc",         # household consumption per capita, constant US$
    "SL.UEM.TOTL.ZS": "unemployment_pct",             # unemployment, % of labour force (ILO est.)
    "SL.UEM.1524.ZS": "youth_unemployment_pct",       # youth unemployment, % (ILO est.)
    "FP.CPI.TOTL.ZG": "inflation_pct",                # consumer price inflation, annual %
    "BX.TRF.PWKR.DT.GD.ZS": "remittances_pct_gdp",    # personal remittances received, % of GDP
    "SP.POP.TOTL": "population",                      # total population
}

API = "https://api.worldbank.org/v2/country/{c}/indicator/{i}"


def fetch_indicator(code: str) -> pd.Series:
    params = {"format": "json", "date": f"{START}:{END}", "per_page": 200}
    r = requests.get(API.format(c=COUNTRY, i=code), params=params, timeout=30)
    r.raise_for_status()
    payload = r.json()
    if len(payload) < 2 or payload[1] is None:
        return pd.Series(dtype="float64", name=code)
    rows = {int(x["date"]): x["value"] for x in payload[1]}
    return pd.Series(rows, name=code, dtype="float64").sort_index()


def main() -> None:
    out = Path("data/raw")
    out.mkdir(parents=True, exist_ok=True)

    columns = {}
    for code, name in INDICATORS.items():
        s = fetch_indicator(code)
        columns[name] = s
        print(f"{code:24s} -> {name:24s} {s.notna().sum():2d} non-missing values")

    df = pd.DataFrame(columns).reindex(range(START, END + 1))
    df.index.name = "year"
    df.to_csv(out / "wdi_albania_2010_2025.csv")

    meta = pd.DataFrame(
        [{"wdi_code": k, "column": v, "retrieved": date.today().isoformat()}
         for k, v in INDICATORS.items()]
    )
    meta.to_csv(out / "wdi_indicator_metadata.csv", index=False)
    print("\nSaved data/raw/wdi_albania_2010_2025.csv")
    print("\nMissing values per column (these years are NOT filled in):")
    print(df.isna().sum())


if __name__ == "__main__":
    main()
