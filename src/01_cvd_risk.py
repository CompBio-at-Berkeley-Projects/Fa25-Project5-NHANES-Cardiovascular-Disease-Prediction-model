import pandas as pd
import numpy as np

# ===============================
# 1. LOAD RAW MCQ (MEDICAL CONDITIONS) FILES
# ===============================

# List of file paths
file_paths = [
    "../data/raw/mcq_2017_2018.xpt",
    "../data/raw/mcq_2015_2016.xpt",
    "../data/raw/mcq_2013_2014.xpt",
    "../data/raw/mcq_2011_2012.xpt",
    "../data/raw/mcq_2009_2010.xpt",
    "../data/raw/mcq_2007_2008.xpt",
    "../data/raw/mcq_2005_2006.xpt",
    "../data/raw/mcq_2003_2004.xpt",
    "../data/raw/mcq_2001_2002.xpt",
    "../data/raw/mcq_1999_2000.xpt"
]

# List of cycles
cycles = [
    "2017-2018", "2015-2016", "2013-2014", "2011-2012", "2009-2010",
    "2007-2008", "2005-2006", "2003-2004", "2001-2002", "1999-2000"
]

# The list of variables to keep
target_vars = [
    "SEQN",      # Respondent ID
    "Cycle",
    "MCQ160E",   # Heart attack
    "MCQ160F",   # Stroke
    "MCQ160B",   # Congestive heart failure
    "MCQ160C",   # Coronary heart disease
    "MCQ160D",   # Angina
]

# =================================================================
# 2. LOAD, ADD CYCLE, REINDEX, AND CONCATENATE
# =================================================================

mcq_list_processed = []

for path, cycle in zip(file_paths, cycles):
    df = pd.read_sas(path)
    
    # 1. Add Cycle column
    df['Cycle'] = cycle
    
    # 2. Reindex to ensure all target columns exist and are in order
    # This is the crucial step to prevent missing data/KeyError upon final concat
    df_reindexed = df.reindex(columns=target_vars)
    
    mcq_list_processed.append(df_reindexed)

# Concatenate all processed dataframes
mcq_subset = pd.concat(mcq_list_processed, ignore_index=True)


# ===============================
# 3. RENAME COLUMNS
# ===============================

mcq_subset = mcq_subset.rename(columns={
    "MCQ160E": "Heart_Attack",
    "MCQ160F": "Stroke",
    "MCQ160B": "Congestive_Heart_Failure",
    "MCQ160C": "Coronary_Heart_Disease",
    "MCQ160D": "Angina"
})

# ================================
# Has_CVD column 
# ================================
# add column for whether has cvd or not
CVD_COLS = ['Heart_Attack', "Stroke", "Congestive_Heart_Failure", "Coronary_Heart_Disease", "Angina"]

# check if any is 1 to set has_cvd to 1 
has_cvd = mcq_subset[CVD_COLS].apply(lambda x: x.isin([1.0]), axis=1).any(axis=1)

# has_cvd is 0 when none of the cvd conditions are met (all values 2)
all_no = mcq_subset[CVD_COLS].apply(lambda x: x.isin([2.0]), axis=1).all(axis=1)

# create column 
mcq_subset['Has_CVD'] = np.select(
    [has_cvd, all_no],
    [1, 0],
    default=np.nan 
)

# drop individual columns
mcq_subset = mcq_subset.drop(columns=CVD_COLS)

# ===============================
# SAVE THE DATASET
# ===============================

output_path = "../data/interim/mcq_subset.csv"
mcq_subset.to_csv(output_path, index=False)

print(f"MCQ subset saved successfully to {output_path}")