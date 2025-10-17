import pandas as pd

# load the raw NHANES  file
demo_2017 = pd.read_sas("data/raw/demo_2017_2018.xpt")
demo_2015 = pd.read_sas("data/raw/demo_2015_2016.xpt") # path to your raw XPT file

# make a column for the cycle
demo_2017["Cycle"] = "2017-2018"
demo_2015["Cycle"] = "2015-2016"

# only the variables you want
keep_vars = [
    "SEQN",       # Respondent ID
    "RIDAGEYR",   # Age in years
    "RIAGENDR",   # Sex
    "RIDRETH1",   # Race/ethnicity
    "WTMEC2YR",   # MEC exam weight
    "SDMVPSU",    # Pseudo-PSU
    "SDMVSTRA",   # Pseudo-stratum
    "Cycle"
]

#vertically concatenate
demo_all = pd.concat([demo_2015, demo_2017], axis=0, ignore_index=True)

# create a subset dataframe with only the variables you want
demo_subset = demo_all[keep_vars]

#rename columns
df = demo_subset.rename(columns = {
    "RIDAGEYR": "Age",
    "RIAGENDR": "Sex",
    "RIDRETH1": "Race/Ethnicity",
    "WTMEC2YR": "MEC exam weight",
    "SDMVPSU": "Pseudo PSU",
    "SDMVSTRA": "Pseudo stratum"
})

# Save the cleaned dataset
df.to_csv("data/interim/demo_subset.csv", index=False)

print("Demographics data subset saved successfully!")