# Fa25-Porject5-NHANES-Cardiovascular-Disease-Prediction-model
The NHANES dataset contains rich health, lifestyle, lab, and biomarker information from a large, diverse U.S. population. This project aims to build a reproducible pipeline that leverages NHANES data to develop and benchmark machine learning models for CVD risk prediction, with an interactive dashboard for exploring key risk factors.
Nahnes Dataste: https://wwwn.cdc.gov/nchs/nhanes/default.aspx

Suggested structure:
nhanes-cvd/
├─ data/
│  ├─ raw/               # untouched SAS/XPT files
│  ├─ external/          # mortality linkage, code lists
│  ├─ interim/           # cleaned tables
│  └─ processed/         # model-ready datasets, splits
├─ src/
│  ├─ 00_download.py
│  ├─ 01_clean_merge.py
│  ├─ 02_feature_engineering.py
│  ├─ 03_make_splits.py
│  ├─ 04_train.py
│  ├─ 05_evaluate.py
│  └─ 06_dashboard_prep.py
├─ dashboard/
│  └─ app.py             # Streamlit (or Dash)
├─ conf/
│  ├─ features.yaml      # which variables & transforms
│  ├─ outcome.yaml       # ICD-10 codes, windows
│  └─ cycles.yaml        # which NHANES cycles
├─ models/
├─ reports/
│  ├─ metrics/
│  └─ figures/
├─ env.yml               # conda environment
├─ dvc.yaml              # (optional) data & model versioning
├─ Snakefile             # or Makefile, your pick
└─ README.md
