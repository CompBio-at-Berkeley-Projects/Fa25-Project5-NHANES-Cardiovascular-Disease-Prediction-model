import pandas as pd

# --- 1. Load the Raw NHANES Files ---  
demo_2017 = pd.read_sas("../data/raw/demo_2017_2018.xpt")
demo_2015 = pd.read_sas("../data/raw/demo_2015_2016.xpt")
demo_2013 = pd.read_sas("../data/raw/demo_2013_2014.xpt")
demo_2011 = pd.read_sas("../data/raw/demo_2011_2012.xpt")
demo_2009 = pd.read_sas("../data/raw/demo_2009_2010.xpt")
demo_2007 = pd.read_sas("../data/raw/demo_2007_2008.xpt")
demo_2005 = pd.read_sas("../data/raw/demo_2005_2006.xpt")
demo_2003 = pd.read_sas("../data/raw/demo_2003_2004.xpt")
demo_2001 = pd.read_sas("../data/raw/demo_2001_2002.xpt")
demo_1999 = pd.read_sas("../data/raw/demo_1999_2000.xpt")   

# --- 2. Add Cycle Column & Group DataFrames ---
def add_cycle_to_dfs(df_list, cycles):
    for df, cycle in zip(df_list, cycles):
        df['Cycle'] = cycle
    return df_list  
cycles = ["2017-2018", "2015-2016", "2013-2014", "2011-2012", "2009-2010", 
          "2007-2008", "2005-2006", "2003-2004", "2001-2002", "1999-2000"]
demo_dfs = [demo_2017, demo_2015, demo_2013, demo_2011, demo_2009, 
             demo_2007, demo_2005, demo_2003, demo_2001, demo_1999]
demo_dfs = add_cycle_to_dfs(demo_dfs, cycles)   

# --- 3. Vertical Concatenation (Within Each Group) ---
demo_all = pd.concat(demo_dfs, axis=0, ignore_index=True)   

# --- 4. Subsetting ---
keep_vars = [
    "SEQN", "Cycle", "RIAGENDR", "RIDAGEYR", "RIDRETH1",
    "WTMEC2YR", "SDMVPSU", "SDMVSTRA"
]
demo_subset = demo_all[[c for c in keep_vars if c in demo_all.columns]].rename(
    columns={
        "RIAGENDR": "Sex",
        "RIDAGEYR": "Age",
        "RIDRETH1": "Race/Ethnicity",
        "WTMEC2YR": "MEC exam weight",
        "SDMVPSU": "Pseudo PSU",
        "SDMVSTRA": "Pseudo stratum",   
    }
)

# --- 5. Save Cleaned Subset ---
out = "../data/interim/demo_subset_final.csv"
demo_subset.to_csv(out, index=False)
print("Demographics subset saved successfully!")