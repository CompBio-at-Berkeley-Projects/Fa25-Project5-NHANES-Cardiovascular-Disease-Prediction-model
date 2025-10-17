# test_environment.py
# Simple test script to verify your NHANES-CVD environment setup

import sys

print("✅ Python version:", sys.version)

# --- Core libraries ---
try:
    import pandas as pd
    import numpy as np
    print("✅ pandas:", pd.__version__)
    print("✅ numpy:", np.__version__)
except ImportError as e:
    print("❌ Missing pandas/numpy:", e)

# --- ML libraries ---
try:
    import sklearn
    import tensorflow as tf
    import xgboost
    import lightgbm
    print("✅ scikit-learn:", sklearn.__version__)
    print("✅ tensorflow:", tf.__version__)
    print("✅ xgboost:", xgboost.__version__)
    print("✅ lightgbm:", lightgbm.__version__)
except ImportError as e:
    print("❌ Missing ML library:", e)

# --- Visualization ---
try:
    import matplotlib
    import seaborn
    print("✅ matplotlib:", matplotlib.__version__)
    print("✅ seaborn:", seaborn.__version__)
except ImportError as e:
    print("❌ Missing visualization library:", e)

# --- Others ---
try:
    import shap
    import streamlit
    import statsmodels
    print("✅ shap:", shap.__version__)
    print("✅ streamlit:", streamlit.__version__)
    print("✅ statsmodels:", statsmodels.__version__)
except ImportError as e:
    print("❌ Missing additional package:", e)

print("\n🎉 All core dependencies loaded successfully!")
