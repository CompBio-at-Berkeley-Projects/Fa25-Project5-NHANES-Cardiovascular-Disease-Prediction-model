import pandas as pd

# MAKE SURE FILENAMES MATCH THESE EXACTLY
diet_2017 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2017_2018.xpt")
diet_2015 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2015_2016.xpt")
diet_2013 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2013_2014.xpt")
diet_2011 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2011_2012.xpt")
diet_2009 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2009_2010.xpt")
diet_2007 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2007_2008.xpt")
diet_2005 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2005_2006.xpt")
diet_2003 = pd.read_sas("../data/raw/dietary_data/DR1TOT_2003_2004.xpt")
diet_2001 = pd.read_sas("../data/raw/dietary_data/DRXTOT_2001_2002.xpt")
diet_1999 = pd.read_sas("../data/raw/dietary_data/DRXTOT_1999_2000.xpt")

# --- 3. ADD CYCLE COLUMN ---
cycles = ["2017-2018", "2015-2016", "2013-2014", "2011-2012", "2009-2010", 
          "2007-2008", "2005-2006", "2003-2004", "2001-2002", "1999-2000"]

diet_dfs = [diet_2017, diet_2015, diet_2013, diet_2011, diet_2009, 
            diet_2007, diet_2005, diet_2003, diet_2001, diet_1999]

for df, cycle in zip(diet_dfs, cycles):
    df['Cycle'] = cycle

# --- 4. CONCATENATE YEARS ---
diet_all = pd.concat(diet_dfs, axis=0, ignore_index=True)

# --- 5. SELECT AND RENAME VARIABLES ---
# We strictly select the 7 variables identified + SEQN and Cycle
# Note: Variable names like DR1TSUGR might be missing in very old years (1999). 
# We use .reindex to safely include them (filling missing years with NaN).

target_vars = [
    'SEQN', 'Cycle',
    'DR1TSODI',  # Sodium
    'DR1TSFAT',  # Saturated Fat
    'DR1TPOTA',  # Potassium
    'DR1TFIBE',  # Dietary Fiber
    'DR1TSUGR',  # Total Sugars
    'DR1TCHOL',  # Cholesterol
    'DR1TKCAL'   # Energy (Calories)
]

# Filter the big dataframe to just these columns
diet_subset = diet_all.reindex(columns=target_vars)

# Rename to human-readable names
diet_subset = diet_subset.rename(columns={
    "DR1TSODI": "Sodium_mg",
    "DR1TSFAT": "SaturatedFat_gm",
    "DR1TPOTA": "Potassium_mg",
    "DR1TFIBE": "Fiber_gm",
    "DR1TSUGR": "Sugar_gm",
    "DR1TCHOL": "Cholesterol_mg",
    "DR1TKCAL": "Calories_kcal"
})


# --- 7. SAVE FINAL MERGED FILE ---
output_path = "..data/interim/dietary_subset.csv"
diet_subset.to_csv(output_path, index=False)

print(f"Success! Merged data saved to {output_path}")