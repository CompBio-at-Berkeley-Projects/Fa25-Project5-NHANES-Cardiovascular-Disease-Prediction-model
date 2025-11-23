
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

MISSING_CODES = [
    7, 77, 777, 7777, 77777,
    9, 99, 999, 9999, 99999,
    -1, -2, -3, -4, " ", "", "NA", "NaN"
]

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Try to convert any column that looks numeric into numeric dtype."""
    for col in df.columns:
        # skip obvious identifiers that should remain string if they’re not numeric
        if col.upper() in {"SEQN"}:
            continue
        # try numeric conversion (errors='ignore' leaves non-numeric columns alone)
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input",  default="data/interim/questionnaire_subset.csv",
                   help="Path to the questionnaire subset CSV")
    p.add_argument("--output", default="data/interim/quest_cleaned_subset.csv",
                   help="Path for cleaned CSV")
    p.add_argument("--report", default="data/interim/quest_cleaned_report.txt",
                   help="Path for a simple text report")
    args = p.parse_args()

    in_path  = Path(args.input)
    out_path = Path(args.output)
    rep_path = Path(args.report)

    if not in_path.exists():
        raise FileNotFoundError(f"Input not found: {in_path}")

    print(f"🔹 Loading {in_path} …")
    df = pd.read_csv(in_path, dtype="object")  # read everything as object first

    n0 = len(df)

    # Normalize whitespace in string columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype("string").str.strip()

    # Replace NHANES missing codes with NaN
    df = df.replace(MISSING_CODES, np.nan)

    # Coerce numerics where possible
    df = coerce_numeric(df)

    # Drop exact duplicate rows
    dup_rows = df.duplicated().sum()
    if dup_rows:
        print(f"🔸 Dropping {dup_rows} exact duplicate rows")
        df = df.drop_duplicates()

    # De-duplicate SEQN if present
    if "SEQN" in df.columns:
        # Keep first occurrence with any non-NaN data besides SEQN
        before = df["SEQN"].duplicated().sum()
        if before:
            print(f"🔸 Resolving {before} duplicated SEQN entries")
            # Prefer the first non-all-NaN (excluding SEQN) row per SEQN
            non_id_cols = [c for c in df.columns if c != "SEQN"]
            # Mark rows that are all NaN across non-id cols
            all_nan_mask = df[non_id_cols].isna().all(axis=1)
            # Keep first per SEQN, preferring non-all-NaN; fallback to first overall
            df = (df[~all_nan_mask]
                    .drop_duplicates(subset=["SEQN"], keep="first")
                 ).append(
                    df[all_nan_mask].drop_duplicates(subset=["SEQN"], keep="first")
                      .loc[lambda x: ~x["SEQN"].isin(df[~all_nan_mask]["SEQN"])]
                 )
            # Restore original column order and sort by SEQN if numeric
            df = df[df.columns]
            if pd.api.types.is_numeric_dtype(df["SEQN"]):
                df = df.sort_values("SEQN")

    # (Optional) You can add simple label expansions here if your subset has codes
    # Example:
    # if "RIAGENDR" in df.columns:
    #     df["RIAGENDR"] = df["RIAGENDR"].map({1: "Male", 2: "Female"}).fillna(df["RIAGENDR"])

    n1 = len(df)

    # Write outputs
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"✅ Saved cleaned file → {out_path} (rows: {n1}, cols: {df.shape[1]})")

    # Simple report
    rep_path.parent.mkdir(parents=True, exist_ok=True)
    with open(rep_path, "w") as f:
        f.write(f"Input:  {in_path}\n")
        f.write(f"Output: {out_path}\n")
        f.write(f"Rows before: {n0}\n")
        f.write(f"Rows after:  {n1}\n\n")
        f.write("Missing values per column (top 20):\n")
        f.write(df.isna().sum().sort_values(ascending=False).head(20).to_string())
        f.write("\n")
    print(f"📝 Wrote report → {rep_path}")

if __name__ == "__main__":
    main()

