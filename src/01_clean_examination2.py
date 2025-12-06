import pandas as pd

# --- 1. Load the Raw NHANES Files ---

# Blood Pressure and Pulse (from BPX files)
exam_bp_2017 = pd.read_sas("../data/raw/exam_bp_2017_2018.xpt")
exam_bp_2015 = pd.read_sas("../data/raw/exam_bp_2015_2016.xpt")
exam_bp_2013 = pd.read_sas("../data/raw/exam_bp_2013_2014.xpt")
exam_bp_2011 = pd.read_sas("../data/raw/exam_bp_2011_2012.xpt")
exam_bp_2009 = pd.read_sas("../data/raw/exam_bp_2009_2010.xpt")
exam_bp_2007 = pd.read_sas("../data/raw/exam_bp_2007_2008.xpt")
exam_bp_2005 = pd.read_sas("../data/raw/exam_bp_2005_2006.xpt")
exam_bp_2003 = pd.read_sas("../data/raw/exam_bp_2003_2004.xpt")
exam_bp_2001 = pd.read_sas("../data/raw/exam_bp_2001_2002.xpt")
exam_bp_1999 = pd.read_sas("../data/raw/exam_bp_1999_2000.xpt")

# Body Measures (BMI and Waist Circ, from BMX files)
exam_bodym_2017 = pd.read_sas("../data/raw/exam_bodym_2017_2018.xpt")
exam_bodym_2015 = pd.read_sas("../data/raw/exam_bodym_2015_2016.xpt")
exam_bodym_2013 = pd.read_sas("../data/raw/exam_bodym_2013_2014.xpt")
exam_bodym_2011 = pd.read_sas("../data/raw/exam_bodym_2011_2012.xpt")
exam_bodym_2009 = pd.read_sas("../data/raw/exam_bodym_2009_2010.xpt")
exam_bodym_2007 = pd.read_sas("../data/raw/exam_bodym_2007_2008.xpt")
exam_bodym_2005 = pd.read_sas("../data/raw/exam_bodym_2005_2006.xpt")
exam_bodym_2003 = pd.read_sas("../data/raw/exam_bodym_2003_2004.xpt")
exam_bodym_2001 = pd.read_sas("../data/raw/exam_bodym_2001_2002.xpt")
exam_bodym_1999 = pd.read_sas("../data/raw/exam_bodym_1999_2000.xpt")

# --- 2. Add Cycle Column & Group DataFrames ---

# Helper function to add cycle to list of dfs
def add_cycle_to_dfs(df_list, cycles):
    for df, cycle in zip(df_list, cycles):
        df['Cycle'] = cycle
    return df_list

cycles = ["2017-2018", "2015-2016", "2013-2014", "2011-2012", "2009-2010", 
          "2007-2008", "2005-2006", "2003-2004", "2001-2002", "1999-2000"]

bp_dfs = [exam_bp_2017, exam_bp_2015, exam_bp_2013, exam_bp_2011, exam_bp_2009, 
          exam_bp_2007, exam_bp_2005, exam_bp_2003, exam_bp_2001, exam_bp_1999]

bodym_dfs = [exam_bodym_2017, exam_bodym_2015, exam_bodym_2013, exam_bodym_2011, exam_bodym_2009,
             exam_bodym_2007, exam_bodym_2005, exam_bodym_2003, exam_bodym_2001, exam_bodym_1999]

# Apply the cycle labels
bp_dfs = add_cycle_to_dfs(bp_dfs, cycles)
bodym_dfs = add_cycle_to_dfs(bodym_dfs, cycles)

# --- 3. Vertical Concatenation (Within Each Group) ---

# Concatenate all years for each measurement type separately
bp_all = pd.concat(bp_dfs, axis=0, ignore_index=True)
bodym_all = pd.concat(bodym_dfs, axis=0, ignore_index=True)

# --- 4. Subsetting ---

# Keep only the necessary variables for each concatenated set
bp_vars = [
    "SEQN", "Cycle",
    "BPXPLS",   # 60 sec. pulse
    "BPXDI1",   # Diastolic: Blood pressure (first reading) mm Hg
    "BPXDI2",   # Diastolic: Blood pressure (second reading) mm Hg
    "BPXDI3",   # Diastolic: Blood pressure (third reading) mm Hg
    "BPXSY1",   # Systolic: Blood pressure (first reading) mm Hg
    "BPXSY2",   # Systolic: Blood pressure (second reading) mm Hg
    "BPXSY3",   # Systolic: Blood pressure (third reading) mm Hg
]
bp_subset = bp_all[bp_vars]


bodym_vars = [
    "SEQN", "Cycle",
    "BMXBMI",   # BMI
    "BMXWAIST", # Waist Circumference (cm)
]
bodym_subset = bodym_all[bodym_vars]


# --- 5. Horizontal Merge (THE FIX) ---

# Merge the two subsets using SEQN and Cycle to combine the partial records
# This correctly aligns the BMI/Waist Circ row with the BP/Pulse row for the same person
merged_df = bp_subset.merge(bodym_subset, on=['SEQN', 'Cycle'], how='outer')


# --- 6. Calculations and Final Cleanup ---

# Averaging BP
merged_df["Avg_Diastolic_BP"] = merged_df[["BPXDI1", "BPXDI2", "BPXDI3"]].mean(axis=1, skipna=True)
merged_df["Avg_Systolic_BP"] = merged_df[["BPXSY1", "BPXSY2", "BPXSY3"]].mean(axis=1, skipna=True)

# drop the original columns
diastolic_cols = [col for col in merged_df.columns if col.startswith('BPXDI')]
systolic_cols = [col for col in merged_df.columns if col.startswith('BPXSY')]
cols_to_drop = diastolic_cols + systolic_cols
final_df = merged_df.drop(columns=cols_to_drop)

# Rename Columns
final_df = merged_df.rename(columns = {
    "BPXPLS":  "60 sec. pulse",
    "BMXBMI":  "BMI",
    "BMXWAIST": "Waist Circumference (cm)"
})

# Select final columns and remove leading/trailing spaces
final_cols = [
    "SEQN", "Cycle", "60 sec. pulse", "BMI", "Waist Circumference (cm)", "Avg_Diastolic_BP", "Avg_Systolic_BP"
]
final_df = final_df[final_cols]
final_df.columns = final_df.columns.str.strip() 

# Removing duplicates (in case of true duplicates, though a merge should prevent the partial-row duplicates)
final_df = final_df.drop_duplicates(subset=['SEQN', 'Cycle'], keep='first')

# Drop rows only if ALL key measurements are missing
measure_cols = [
    "60 sec. pulse", "BMI", "Waist Circumference (cm)",
    "Avg_Diastolic_BP", "Avg_Systolic_BP"
]
final_df = final_df.dropna(subset=measure_cols, how='all')

#rounding
rounding_map = {
    "60 sec. pulse": 0,
    "Avg_Diastolic_BP": 0,
    "Avg_Systolic_BP": 0,
    "BMI": 1,
    "Waist Circumference (cm)": 1,
}

for col, decimals in rounding_map.items():
    if col in final_df.columns:
        final_df[col] = final_df[col].round(decimals)

# save ---
output_path = "../data/interim/exam_subset2.csv"
final_df.to_csv(output_path, index=False)

print("Examination data subset fixed, cleaned, and saved successfully!")