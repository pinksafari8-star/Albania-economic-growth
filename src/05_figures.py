"""05_figures.py - create the two figures (PDF for the assignment, PNG for the website)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.alpha": 0.25, "font.family": "DejaVu Sans"})
BLUE, ORANGE, GREEN, GREY, RED = "#1f4e79", "#d98324", "#2a8c5a", "#666666", "#b03a2e"

df = pd.read_csv("data/processed/albania_clean.csv", index_col="year")

# ---------- Figure 1: FDI and GDP growth ----------
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.8))

a.bar(df.index, df["gdp_growth_pct"], color=ORANGE, alpha=0.8, label="Real GDP growth (% per year, left axis)")
a.set_ylabel("Real GDP growth (% per year)")
a.set_xlabel("Year")
a2 = a.twinx()
a2.plot(df.index, df["fdi_pct_gdp"], color=BLUE, marker="o", lw=2, label="FDI net inflows (% of GDP, right axis)")
a2.set_ylabel("FDI net inflows (% of GDP)")
a2.set_ylim(0, 11); a2.grid(False); a2.spines["right"].set_visible(True)
h1, l1 = a.get_legend_handles_labels(); h2, l2 = a2.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, loc="upper center", fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.18))
a.set_title("(a) FDI share of GDP has drifted down while growth fluctuated")

lr = stats.linregress(df["fdi_pct_gdp"], df["gdp_growth_pct"])
b.scatter(df["fdi_pct_gdp"], df["gdp_growth_pct"], color=BLUE, zorder=3)
for y, row in df.iterrows():
    b.annotate(str(y), (row["fdi_pct_gdp"], row["gdp_growth_pct"]), fontsize=7, xytext=(3, 3), textcoords="offset points")
xs = pd.Series([df["fdi_pct_gdp"].min(), df["fdi_pct_gdp"].max()])
b.plot(xs, lr.intercept + lr.slope * xs, color=RED, lw=2)
b.set_xlabel("FDI net inflows (% of GDP)")
b.set_ylabel("Real GDP growth (% per year)")
b.set_title("(b) No clear positive link: same-year scatter, 2010-2025")
b.text(0.97, 0.95, f"Pearson r = {lr.rvalue:.2f}, R² = {lr.rvalue**2:.2f}, p = {lr.pvalue:.2f}\nslope = {lr.slope:.2f} pp per +1 pp of FDI/GDP (n = 16)",
       transform=b.transAxes, fontsize=8.5, ha="right", va="top", bbox=dict(boxstyle="round", fc="white", ec=GREY))
fig.suptitle("Figure 1. Foreign direct investment and economic growth in Albania, 2010-2025", fontweight="bold")
fig.text(0.5, -0.01, "Source: World Bank, World Development Indicators (BX.KLT.DINV.WD.GD.ZS; NY.GDP.MKTP.KD.ZG). Association, not causation.",
         ha="center", fontsize=8, color=GREY)
fig.tight_layout()
fig.savefig("figures/figure1_fdi_vs_growth.pdf", bbox_inches="tight")
fig.savefig("figures/figure1_fdi_vs_growth.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ---------- Figure 2: growth vs living standards ----------
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.8))
a.plot(df.index, df["gdp_pc_index"], color=BLUE, lw=2.2, label="Real GDP per capita")
a.plot(df.index, df["hh_cons_index"], color=GREEN, lw=2.2, label="Household consumption per capita")
a.plot(df.index, df["gdp_total_index"], color=ORANGE, lw=2, ls="--", label="Real total GDP")
a.plot(df.index, df["population_index"], color=GREY, lw=2, ls=":", label="Population")
a.axhline(100, color="black", lw=0.8)
a.set_xlabel("Year"); a.set_ylabel("Index (2010 = 100)")
a.set_title("(a) Output per person grew faster than consumption per person")
for col, c in [("gdp_pc_index", BLUE), ("hh_cons_index", GREEN), ("gdp_total_index", ORANGE), ("population_index", GREY)]:
    a.annotate(f"{df[col].loc[2025]:.0f}", (2025, df[col].loc[2025]), xytext=(4, -3), textcoords="offset points", fontsize=8, color=c)
a.set_xlim(2010, 2026.2)
a.legend(fontsize=8, frameon=False, loc="upper left")

b.plot(df.index, df["cons_to_gdp_ratio_pct"], color=GREEN, marker="o", lw=2, label="Household consumption / GDP per capita (%)")
b.set_ylabel("Household consumption per capita as % of GDP per capita")
b.set_xlabel("Year"); b.set_ylim(60, 85)
b2 = b.twinx()
b2.plot(df.index, df["unemployment_pct"], color=RED, lw=1.8, ls="--", label="Unemployment rate (%, right axis)")
b2.set_ylabel("Unemployment (% of labour force)"); b2.set_ylim(0, 25); b2.grid(False); b2.spines["right"].set_visible(True)
h1, l1 = b.get_legend_handles_labels(); h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, fontsize=8, frameon=False, loc="lower left")
b.set_title("(b) Consumption share fell; unemployment peaked in 2014")
fig.suptitle("Figure 2. National growth versus household living standards in Albania, 2010-2025", fontweight="bold")
fig.text(0.5, -0.01, "Source: World Bank, World Development Indicators (NY.GDP.PCAP.KD; NE.CON.PRVT.PC.KD; SP.POP.TOTL; SL.UEM.TOTL.ZS). National averages only.",
         ha="center", fontsize=8, color=GREY)
fig.tight_layout()
fig.savefig("figures/figure2_growth_vs_living_standards.pdf", bbox_inches="tight")
fig.savefig("figures/figure2_growth_vs_living_standards.png", dpi=200, bbox_inches="tight")
print("Figures saved")
