import pandas as pd 

# laboratory data
lab_file = pd.read_csv("../data/interim/laboratory_subset5.csv")
laboratory_subset = lab_file.drop(columns="Direct HDL-Cholesterol (mg/dL)")
laboratory_subset.to_csv("../data/interim/laboratory_subset_final.csv", index=False)

print("lab data subset saved successfully!")

# questionnaire data
quest_file = pd.read_csv("../data/interim/questionnaire_subset.csv")
quest_subset = quest_file.drop(columns="Smoked100")
quest_subset.to_csv("../data/interim/questionnaire_subset_final.csv", index=False)

print("questionnaire data subset saved successfully!")