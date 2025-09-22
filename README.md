# Fa25-Porject5-NHANES-Cardiovascular-Disease-Prediction-model
The NHANES dataset contains rich health, lifestyle, lab, and biomarker information from a large, diverse U.S. population. This project aims to build a reproducible pipeline that leverages NHANES data to develop and benchmark machine learning models for CVD risk prediction, with an interactive dashboard for exploring key risk factors.
Nahnes Dataste: https://wwwn.cdc.gov/nchs/nhanes/default.aspx

nhanes-cvd/
├─ data/                  # All datasets
│  ├─ raw/                # Untouched SAS/XPT files directly from NHANES
│  ├─ external/           # Mortality linkage files, ICD-10 code lists, etc.
│  ├─ interim/            # Intermediate cleaned/merged tables
│  └─ processed/          # Model-ready datasets and train/val/test splits
│
├─ src/                   # Source code for pipeline stages
│  ├─ 00_download.py      # Download or ingest NHANES data
│  ├─ 01_clean_merge.py   # Clean and merge raw modules into a single cohort
│  ├─ 02_feature_engineering.py # Feature transformations, encodings, imputations
│  ├─ 03_make_splits.py   # Train/validation/test split creation
│  ├─ 04_train.py         # Model training scripts
│  ├─ 05_evaluate.py      # Evaluation and metrics generation
│  └─ 06_dashboard_prep.py# Prep artifacts for visualization dashboard
│
├─ dashboard/             # Interactive exploration
│  └─ app.py              # Streamlit (or Dash) dashboard entrypoint
│
├─ conf/                  # Configuration files
│  ├─ features.yaml       # Selected features and transforms
│  ├─ outcome.yaml        # Outcome definition (ICD-10 codes, time windows)
│  └─ cycles.yaml         # Which NHANES cycles are used
│
├─ models/                # Trained model artifacts
│
├─ reports/               # Generated outputs
│  ├─ metrics/            # Model performance metrics
│  └─ figures/            # Plots and figures (ROC, calibration, SHAP, etc.)
│
├─ env.yml                # Conda environment specification
├─ dvc.yaml               # (Optional) Data & model versioning with DVC
├─ Snakefile              # Or Makefile for pipeline orchestration
└─ README.md              # Project documentation (this file)
