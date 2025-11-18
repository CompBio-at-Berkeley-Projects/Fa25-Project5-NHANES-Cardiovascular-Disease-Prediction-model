import pandas as pd

# load the raw NHANES file

#blood pressure and cholesterol
quest_2017_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2017_2018.xpt")
quest_2015_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2015_2016.xpt")
quest_2013_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2013_2014.xpt")
quest_2011_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2011_2012.xpt")
quest_2009_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2009_2010.xpt")
quest_2007_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2007_2008.xpt")
quest_2005_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2005_2006.xpt")
quest_2003_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2003_2004.xpt")
quest_2001_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_2001_2002.xpt")
quest_1999_BPQ = pd.read_sas("../data/raw/quest_data/questBPQ_1999_2000.xpt")

#diabetes
quest_2017_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2017_2018.xpt")
quest_2015_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2015_2016.xpt")
quest_2013_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2013_2014.xpt")
quest_2011_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2011_2012.xpt")
quest_2009_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2009_2010.xpt")
quest_2007_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2007_2008.xpt")
quest_2005_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2005_2006.xpt")
quest_2003_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2003_2004.xpt")
quest_2001_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_2001_2002.xpt")
quest_1999_DIQ = pd.read_sas("../data/raw/quest_data/questDIQ_1999_2000.xpt")

#kidney condition
quest_2017_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2017_2018.xpt")
quest_2015_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2015_2016.xpt")
quest_2013_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2013_2014.xpt")
quest_2011_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2011_2012.xpt")
quest_2009_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2009_2010.xpt")
quest_2007_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2007_2008.xpt")
quest_2005_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2005_2006.xpt")
quest_2003_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2003_2004.xpt")
quest_2001_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_2001_2002.xpt")
quest_1999_KIQ = pd.read_sas("../data/raw/quest_data/questKIQ_1999_2000.xpt")

#medical condition
quest_2017_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2017_2018.xpt")
quest_2015_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2015_2016.xpt")
quest_2013_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2013_2014.xpt")
quest_2011_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2011_2012.xpt")
quest_2009_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2009_2010.xpt")
quest_2007_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2007_2008.xpt")
quest_2005_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2005_2006.xpt")
quest_2003_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2003_2004.xpt")
quest_2001_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_2001_2002.xpt")
quest_1999_MCQ = pd.read_sas("../data/raw/quest_data/questMCQ_1999_2000.xpt")

#physical activity
quest_2017_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2017_2018.xpt")
quest_2015_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2015_2016.xpt")
quest_2013_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2013_2014.xpt")
quest_2011_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2011_2012.xpt")
quest_2009_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2009_2010.xpt")
quest_2007_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2007_2008.xpt")
quest_2005_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2005_2006.xpt")
quest_2003_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2003_2004.xpt")
quest_2001_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_2001_2002.xpt")
quest_1999_PAQ = pd.read_sas("../data/raw/quest_data/questPAQ_1999_2000.xpt")

#smoking
quest_2017_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2017_2018.xpt")
quest_2015_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2015_2016.xpt")
quest_2013_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2013_2014.xpt")
quest_2011_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2011_2012.xpt")
quest_2009_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2009_2010.xpt")
quest_2007_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2007_2008.xpt")
quest_2005_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2005_2006.xpt")
quest_2003_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2003_2004.xpt")
quest_2001_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_2001_2002.xpt")
quest_1999_SMQ = pd.read_sas("../data/raw/quest_data/questSMQ_1999_2000.xpt")

#weight history
quest_2017_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2017_2018.xpt")
quest_2015_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2015_2016.xpt")
quest_2013_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2013_2014.xpt")
quest_2011_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2011_2012.xpt")
quest_2009_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2009_2010.xpt")
quest_2007_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2007_2008.xpt")
quest_2005_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2005_2006.xpt")
quest_2003_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2003_2004.xpt")
quest_2001_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_2001_2002.xpt")
quest_1999_WHQ = pd.read_sas("../data/raw/quest_data/questWHQ_1999_2000.xpt")

# --- 2. ADD CYCLE COLUMN ---
# Helper function to add cycle to list of dfs
def add_cycle_to_dfs(df_list, cycles):
    for df, cycle in zip(df_list, cycles):
        df['Cycle'] = cycle
    return df_list

cycles = ["2017-2018", "2015-2016", "2013-2014", "2011-2012", "2009-2010", 
          "2007-2008", "2005-2006", "2003-2004", "2001-2002", "1999-2000"]

# Create lists of dataframes to loop through easily
bpq_dfs = [quest_2017_BPQ, quest_2015_BPQ, quest_2013_BPQ, quest_2011_BPQ, quest_2009_BPQ, 
           quest_2007_BPQ, quest_2005_BPQ, quest_2003_BPQ, quest_2001_BPQ, quest_1999_BPQ]

diq_dfs = [quest_2017_DIQ, quest_2015_DIQ, quest_2013_DIQ, quest_2011_DIQ, quest_2009_DIQ,
           quest_2007_DIQ, quest_2005_DIQ, quest_2003_DIQ, quest_2001_DIQ, quest_1999_DIQ]

kiq_dfs = [quest_2017_KIQ, quest_2015_KIQ, quest_2013_KIQ, quest_2011_KIQ, quest_2009_KIQ,
           quest_2007_KIQ, quest_2005_KIQ, quest_2003_KIQ, quest_2001_KIQ, quest_1999_KIQ]

mcq_dfs = [quest_2017_MCQ, quest_2015_MCQ, quest_2013_MCQ, quest_2011_MCQ, quest_2009_MCQ,
           quest_2007_MCQ, quest_2005_MCQ, quest_2003_MCQ, quest_2001_MCQ, quest_1999_MCQ]

paq_dfs = [quest_2017_PAQ, quest_2015_PAQ, quest_2013_PAQ, quest_2011_PAQ, quest_2009_PAQ,
           quest_2007_PAQ, quest_2005_PAQ, quest_2003_PAQ, quest_2001_PAQ, quest_1999_PAQ]

smq_dfs = [quest_2017_SMQ, quest_2015_SMQ, quest_2013_SMQ, quest_2011_SMQ, quest_2009_SMQ,
           quest_2007_SMQ, quest_2005_SMQ, quest_2003_SMQ, quest_2001_SMQ, quest_1999_SMQ]

whq_dfs = [quest_2017_WHQ, quest_2015_WHQ, quest_2013_WHQ, quest_2011_WHQ, quest_2009_WHQ,
           quest_2007_WHQ, quest_2005_WHQ, quest_2003_WHQ, quest_2001_WHQ, quest_1999_WHQ]

# Apply the cycle labels
add_cycle_to_dfs(bpq_dfs, cycles)
add_cycle_to_dfs(diq_dfs, cycles)
add_cycle_to_dfs(kiq_dfs, cycles)
add_cycle_to_dfs(mcq_dfs, cycles)
add_cycle_to_dfs(paq_dfs, cycles)
add_cycle_to_dfs(smq_dfs, cycles)
add_cycle_to_dfs(whq_dfs, cycles)

#CHANGE BELOW STUFF, THIS WAS FOR DEMO BUT NOW IT NEEDS TO BE UPDATED FOR QUESTIONNAIRE

# combine all years vertically for each category 
bpq_all = pd.concat(bpq_dfs, axis=0, ignore_index=True)
diq_all = pd.concat(diq_dfs, axis=0, ignore_index=True)
kiq_all = pd.concat(kiq_dfs, axis=0, ignore_index=True)
mcq_all = pd.concat(mcq_dfs, axis=0, ignore_index=True)
paq_all = pd.concat(paq_dfs, axis=0, ignore_index=True)
smq_all = pd.concat(smq_dfs, axis=0, ignore_index=True)
whq_all = pd.concat(whq_dfs, axis=0, ignore_index=True)

# keep certain variables 
# BPQ Variables
# BPQ020: Ever told you had high blood pressure
# BPQ080: Ever told blood cholesterol high
bpq_subset = bpq_all[['SEQN', 'Cycle', 'BPQ020', 'BPQ080']]

# DIQ Variables
# DIQ010: Doctor told you have diabetes
diq_subset = diq_all[['SEQN', 'Cycle', 'DIQ010']]

# WHQ Variables
# WHD010: Current self-reported height (inches)
# WHD020: Current self-reported weight (pounds)
whq_subset = whq_all[['SEQN', 'Cycle', 'WHD010', 'WHD020']]

# SMQ Variables
# SMQ020: Smoked at least 100 cigarettes in life
# SMQ040: Do you now smoke cigarettes
smq_subset = smq_all[['SEQN', 'Cycle', 'SMQ020', 'SMQ040']]

# MCQ Variables
# MCQ300a (or MCQ300A): Close relative had heart attack?
# Note: Variable names can sometimes be capitalized differently in older files (e.g. MCQ300A vs MCQ300a). 
# We use a check below to handle capitalization.
mcq_var = 'MCQ300A' if 'MCQ300A' in mcq_all.columns else 'MCQ300a'
mcq_subset = mcq_all[['SEQN', 'Cycle', mcq_var]]
mcq_subset = mcq_subset.rename(columns={mcq_var: 'MCQ300A'}) # Standardize name

# PAQ Variables
# PAD680: Minutes sedentary activity
paq_subset = paq_all[['SEQN', 'Cycle', 'PAD680']]

# KIQ Variables
# KIQ022: Ever told you had weak/failing kidneys
kiq_subset = kiq_all[['SEQN', 'Cycle', 'KIQ022']]

#merge datasets based on seqn and cycle #
merged_df = bpq_subset.merge(diq_subset, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(whq_subset, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(smq_subset, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(mcq_subset, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(paq_subset, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(kiq_subset, on=['SEQN', 'Cycle'], how='outer')

#rename columns
final_df = merged_df.rename(columns={
    "BPQ020": "HighBP",
    "BPQ080": "HighChol",
    "DIQ010": "Diabetes",
    "WHD010": "Height_in",
    "WHD020": "Weight_lb",
    "SMQ020": "Smoked100",
    "SMQ040": "SmokeNow",
    "MCQ300A": "FamHistory_HeartAttack",
    "PAD680": "Sedentary_Mins",
    "KIQ022": "WeakKidneys"
})

# --- 7. SAVE ---
output_path = "../data/interim/questionnaire_subset.csv"
final_df.to_csv(output_path, index=False)

print(f"Questionnaire data cleaned and saved to {output_path}!")