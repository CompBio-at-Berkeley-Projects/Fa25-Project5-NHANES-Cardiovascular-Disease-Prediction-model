import pandas as pd
import numpy as np
import os

df = pd.read_csv("exam_subset.csv") 

missing_values = [
    7, 77, 777, 7777, 77777,
    9, 99, 999, 9999, 99999,
    -1, -2, -3, -4, " ", ""
]

df = df.replace(missing_values, np.nan)

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

output_path = "../data/interim/clean_exam_subset.csv"
df.to_csv(output_path, index=False)