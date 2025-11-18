import pandas as pd

# Add files up here
morality_17__18 = data/raw/NHANES_2017_2018_MORT_2019_PUBLIC.dat
morality_15__16 = data/raw/NHANES_2015_2016_MORT_2019_PUBLIC.dat
morality_13__14 = data/raw/NHANES_2013_2014_MORT_2019_PUBLIC.dat
morality_11__12 = data/raw/NHANES_2011_2012_MORT_2019_PUBLIC.dat
files = [morality_17__18, morality_15__16, morality_13__14,  morality_11__12]

columns = [(15, 16), (16, 17), (17, 20), (20, 21), (21, 23)]
rename = ["Eligibility", "Morality Status", "Leading Underlying Cause of Death", "Diabetes Flag", "Hypertension Flag"]
subtemp = []

for name in files:
    temp = pd.read_fwf(name, colspecs = columns, name = rename)
    temp["Cycle"] = "-".join(name.split("_")[1:3])
    subtemp.append(temp)
    
verticallyConcat = pd.concat(subtemp, axis = 0, ignore_index = True)


'''
[------------------------Notes-----------------------------]
We take what we need but do not further filter columns that
don't provide no-data due to opt-out or inelegbility.
'''