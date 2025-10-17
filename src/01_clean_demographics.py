import pandas as pd

# load the raw NHANES  file
demo = pd.read_sas("data/raw/DEMO_J.XPT")  # path to your raw XPT file

# only the variables you want
keep_vars = [
    "SEQN",       # Respondent ID
    "RIDAGEYR",   # Age in years
    "RIAGENDR",   # Sex
    "RIDRETH1",   # Race/ethnicity
    "WTMEC2YR",   # MEC exam weight
    "SDMVPSU",    # Pseudo-PSU
    "SDMVSTRA"    # Pseudo-stratum
]

# create a subset datafram with only the variables you want
demo_subset = demo[keep_vars]

# Save the cleaned dataset
demo_subset.to_csv("data/interim/demo_subset.csv", index=False)

print("Demographics data subset saved successfully!")