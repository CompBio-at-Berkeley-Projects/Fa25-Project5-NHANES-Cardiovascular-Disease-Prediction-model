import pandas as pd
from pathlib import Path
import re

RAW = Path("data/raw")
INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

def find_cycles():
    pairs = []
    for p in sorted(RAW.glob("demo_*_*.xpt")):
        m = re.search(r"demo_(\d{4}_\d{4})", p.name)
        if m:
            pairs.append((m.group(1).replace("_", "-"), p))
    if not pairs:
        raise FileNotFoundError("⚠️ No demo_[YYYY_YYYY].xpt files found in data/raw/")
    print(f"🔍 Found {len(pairs)} demo files:")
    for c, p in pairs:
        print(f"   {c}: {p.name}")
    return pairs

def load_demo(path: Path) -> pd.DataFrame:
    return pd.read_sas(path, format="xport")

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    race_col = "RIDRETH3" if "RIDRETH3" in df.columns else ("RIDRETH1" if "RIDRETH1" in df.columns else None)
    keep = ["SEQN", "RIDAGEYR", "RIAGENDR", race_col, "WTMEC2YR", "SDMVPSU", "SDMVSTRA"]
    keep = [c for c in keep if c]
    return df[keep].rename(columns={
        "RIDAGEYR": "Age",
        "RIAGENDR": "Sex",
        "RIDRETH1": "Race/Ethnicity",
        "RIDRETH3": "Race/Ethnicity",
        "WTMEC2YR": "MEC exam weight",
        "SDMVPSU": "Pseudo PSU",
        "SDMVSTRA": "Pseudo stratum",
    })

def main():
    frames = []
    for cycle, path in find_cycles():
        try:
            df = load_demo(path)
            df = normalize_columns(df)
            df["Cycle"] = cycle
            frames.append(df)
            print(f"✅ Loaded {cycle} ({df.shape[0]} rows)")
        except Exception as e:
            print(f"⚠️ Skipping {cycle}: {e}")

    demo_all = pd.concat(frames, ignore_index=True)
    out = INTERIM / "demo_subset.csv"
    demo_all.to_csv(out, index=False)
    print(f"\n✅ Combined demographics saved → {out}")
    print(f"   Total shape: {demo_all.shape}")
    print("   Cycles included:", sorted(demo_all['Cycle'].unique()))

if __name__ == "__main__":
    main()
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

