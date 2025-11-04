import pandas as pd

# load the raw NHANES  file
exam_android_2003 = pd.read_sas("../data/raw/exam_android_2003_2004.xpt")  # path to your raw XPT file
exam_android_2005 = pd.read_sas("../data/raw/exam_android_2005_2006.xpt")
exam_android_2011 = pd.read_sas("../data/raw/exam_android_2011_2012.xpt")
exam_android_2013 = pd.read_sas("../data/raw/exam_android_2013_2014.xpt")
exam_android_2015 = pd.read_sas("../data/raw/exam_android_2015_2016.xpt")
exam_android_2017 = pd.read_sas("../data/raw/exam_android_2017_2018.xpt")

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


# make a column for the cycle
exam_android_2003["Cycle"] = "2003-2004"
exam_android_2005["Cycle"] = "2005-2006"
exam_android_2011["Cycle"] = "2011-2012"
exam_android_2013["Cycle"] = "2013-2014"
exam_android_2015["Cycle"] = "2015-2016"
exam_android_2017["Cycle"] = "2017-2018"
exam_bp_2017["Cycle"] = "2017-2018"
exam_bp_2015["Cycle"] = "2015-2016"
exam_bp_2013["Cycle"] = "2013-2014"
exam_bp_2011["Cycle"] = "2011-2012"
exam_bp_2009["Cycle"] = "2009-2010"
exam_bp_2007["Cycle"] = "2007-2008"
exam_bp_2005["Cycle"] = "2005-2006"
exam_bp_2003["Cycle"] = "2003-2004"
exam_bp_2001["Cycle"] = "2001-2002"
exam_bp_1999["Cycle"] = "1999-2000"
exam_bodym_2017["Cycle"] = "2017-2018"
exam_bodym_2015["Cycle"] = "2015-2016"
exam_bodym_2013["Cycle"] = "2013-2014"
exam_bodym_2011["Cycle"] = "2011-2012"
exam_bodym_2009["Cycle"] = "2009-2010"
exam_bodym_2007["Cycle"] = "2007-2008"
exam_bodym_2005["Cycle"] = "2005-2006"
exam_bodym_2003["Cycle"] = "2003-2004"
exam_bodym_2001["Cycle"] = "2001-2002"
exam_bodym_1999["Cycle"] = "1999-2000"

# only the variables you want (dropped Hip Circumference, Android to gynoid ratio, and Fourth readings)
keep_vars = [
    "SEQN",       # Respondent ID
    "Cycle",    # Cycle
    "BPXPLS",   # 60 sec. pulse
    "BMXBMI",   # BMI
    "BMXWAIST",    # Waist Circumference (cm)
    "BPXDI1",   # Diastolic: Blood pressure (first reading) mm Hg
    "BPXDI2",   # Diastolic: Blood pressure (second reading) mm Hg
    "BPXDI3",   # Diastolic: Blood pressure (third reading) mm Hg
    "BPXSY1",   # Systolic: Blood pressure (first reading) mm Hg
    "BPXSY2",   # Systolic: Blood pressure (second reading) mm Hg
    "BPXSY3",   # Systolic: Blood pressure (third reading) mm Hg
]

# vertically concatenate
exam_all = pd.concat([exam_bodym_2017, exam_bodym_2015,exam_bodym_2013,exam_bodym_2011,exam_bodym_2009,
            exam_bodym_2007,exam_bodym_2005,exam_bodym_2003,exam_bodym_2001,exam_bodym_1999,
            exam_bp_2017,exam_bp_2015,exam_bp_2013,exam_bp_2011,exam_bp_2009,exam_bp_2007,exam_bp_2005,
            exam_bp_2003,exam_bp_2001,exam_bp_1999,exam_android_2003,exam_android_2005,exam_android_2011,
            exam_android_2013,exam_android_2015,exam_android_2017], axis=0, ignore_index=True)

# create a subset dataframe with only the variables you want
exam_subset = exam_all[keep_vars]

# rename columns
df = exam_subset.rename(columns = {
    "RIDAGEYR": "Age",
    "RIAGENDR": "Sex",
    "RIDRETH1": "Race/Ethnicity",
    "WTMEC2YR": "MEC exam weight",
    "SDMVPSU": "Pseudo PSU",
    "SDMVSTRA": "Pseudo stratum",
    "SEQN": "Respondent ID",
    "BPXPLS":  "60 sec. pulse",
    "BMXBMI":  "BMI",
    "DXXAGRAT":  "Android to gynoid ratio",
    "BMXHIP":   "Hip Circumference (cm)",
    "BMXWAIST":    "Waist Circumference (cm)",
    "BPXDI1":   "Diastolic: Blood pressure (first reading) mm Hg",
    "BPXDI2":   "Diastolic: Blood pressure (second reading) mm Hg",
    "BPXDI3":   "Diastolic: Blood pressure (third reading) mm Hg",
    "BPXDI4":   "Diastolic: Blood pressure (fourth reading if necessary) mm Hg",
    "BPXSY1":   "Systolic: Blood pressure (first reading) mm Hg",
    "BPXSY2":   "Systolic: Blood pressure (second reading) mm Hg",
    "BPXSY3":   "Systolic: Blood pressure (third reading) mm Hg",
    "BPXSY4":   "Systolic: Blood pressure (fourth reading if necessary) mm Hg"
})

# averaging bp
df["Avg_Diastolic_BP"] = df[["Diastolic: Blood pressure (first reading) mm Hg", 
                             "Diastolic: Blood pressure (second reading) mm Hg",
                             "Diastolic: Blood pressure (third reading) mm Hg"]].mean(axis=1, skipna=True)
df["Avg_Systolic_BP"] = df[["Systolic: Blood pressure (first reading) mm Hg",
                            "Systolic: Blood pressure (second reading) mm Hg",
                            "Systolic: Blood pressure (third reading) mm Hg"]].mean(axis=1, skipna=True)


# remove leading/trailing spaces
df.columns = df.columns.str.strip()  

# removing duplicates
df = df.drop_duplicates(keep='first')

# drop rows only if ALL key measurements are missing
measure_cols = [
    "60 sec. pulse", "BMI", "Waist Circumference (cm)",
    "Avg_Diastolic_BP", "Avg_Systolic_BP"
]

df = df.dropna(subset=measure_cols, how='all')

# Save the cleaned dataset
df.to_csv("../data/interim/exam_subset.csv", index=False)

print("Examination data subset saved successfully!")