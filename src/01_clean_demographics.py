import pandas as pd
from pathlib import Path

# ---- Load available cycles (guide shows 2015–2016 + 2017–2018) ----
dfs = []

# 2017–2018 (you already have this XPT; we also support CSV if you prefer)
p_2017_xpt = Path("data/raw/demo_2017_2018.xpt")
p_2017_csv = Path("data/interim/demo_2017_2018.csv")
if p_2017_csv.exists():
    d2017 = pd.read_csv(p_2017_csv)
elif p_2017_xpt.exists():
    d2017 = pd.read_sas(p_2017_xpt, format="xport")
else:
    raise FileNotFoundError("Missing 2017–2018 demographics file.")
d2017["Cycle"] = "2017-2018"
dfs.append(d2017)

# 2015–2016 (optional; will be skipped if not present)
p_2015_xpt = Path("data/raw/demo_2015_2016.xpt")
p_2015_csv = Path("data/interim/demo_2015_2016.csv")
if p_2015_csv.exists() or p_2015_xpt.exists():
    if p_2015_csv.exists():
        d2015 = pd.read_csv(p_2015_csv)
    else:
        d2015 = pd.read_sas(p_2015_xpt, format="xport")
    d2015["Cycle"] = "2015-2016"
    dfs.append(d2015)

# ---- Concatenate cycles vertically (as in the guide) ----
demo_all = pd.concat(dfs, axis=0, ignore_index=True)

# ---- Keep variables the guide lists (with 2017+ column variants) ----
# RIDRETH is 1 in older docs, 3 in 2017–2018; keep whichever exists.
race_col = "RIDRETH3" if "RIDRETH3" in demo_all.columns else "RIDRETH1"

keep_vars = [
    "SEQN",        # Respondent ID
    "RIDAGEYR",    # Age in years
    "RIAGENDR",    # Sex
    race_col,      # Race/ethnicity
    "WTMEC2YR",    # MEC exam weight
    "SDMVPSU",     # Pseudo-PSU
    "SDMVSTRA",    # Pseudo-stratum
    "Cycle",
]

demo_subset = demo_all[[c for c in keep_vars if c in demo_all.columns]].rename(
    columns={
        "RIDAGEYR": "Age",
        "RIAGENDR": "Sex",
        "RIDRETH1": "Race/Ethnicity",
        "RIDRETH3": "Race/Ethnicity",
        "WTMEC2YR": "MEC exam weight",
        "SDMVPSU": "Pseudo PSU",
        "SDMVSTRA": "Pseudo stratum",
    }
)

out = Path("data/interim/demo_subset.csv")
out.parent.mkdir(parents=True, exist_ok=True)
demo_subset.to_csv(out, index=False)
print(f"✅ Demographics data subset saved successfully → {out} (shape={demo_subset.shape})")

