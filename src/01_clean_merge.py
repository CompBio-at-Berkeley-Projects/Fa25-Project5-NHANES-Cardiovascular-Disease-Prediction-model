import pandas as pd

# load cleaned subsets
demographics_file = pd.read_csv("../data/interim/demo_subset_final.csv")
dietary_file = pd.read_csv("../data/interim/dietary_subset_final.csv")
examination_file = pd.read_csv("../data/interim/exam_subset2.csv")
laboratory_file = pd.read_csv("../data/interim/laboratory_subset_final.csv")
mcq_file = pd.read_csv("../data/interim/mcq_subset.csv")
questionnaire_file = pd.read_csv("../data/interim/questionnaire_subset_final.csv")

# Merge datasets on SEQN and Cycle
merged_df = demographics_file.merge(dietary_file, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(examination_file, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(laboratory_file, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(questionnaire_file, on=['SEQN', 'Cycle'], how='outer')
merged_df = merged_df.merge(mcq_file, on=['SEQN', 'Cycle'], how='outer')

# Save the merged dataset
output_path = "../data/interim/merged_dataset.csv"
merged_df.to_csv(output_path, index=False)
print("Merged dataset saved successfully!")