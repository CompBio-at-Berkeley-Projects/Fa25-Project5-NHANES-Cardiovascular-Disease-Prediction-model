import pandas as pd
import numpy as np
import re

# Standard Biochemistry Profile
StandardBiochemistryProfile2017 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2017-2018.xpt")
StandardBiochemistryProfile2015 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2015-2016.xpt")
StandardBiochemistryProfile2013 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2013-2014.xpt")
StandardBiochemistryProfile2011 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2011-2012.xpt")
StandardBiochemistryProfile2009 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2009-2010.xpt")
StandardBiochemistryProfile2007 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2007-2008.xpt")
StandardBiochemistryProfile2005 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2005-2006.xpt")
StandardBiochemistryProfile2003 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2003-2004.xpt")
StandardBiochemistryProfile2001 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_2001-2002.xpt")
StandardBiochemistryProfile1999 = pd.read_sas("data/raw/Lab_StandardBiochemistryProfile_1999-2000.xpt")

# Plasma Fasting Glucose
PlasmaFastingGlucose2017 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2017-2018.xpt")
PlasmaFastingGlucose2015 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2015-2016.xpt")
PlasmaFastingGlucose2013 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2013-2014.xpt")
PlasmaFastingGlucose2011 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2011-2012.xpt")
PlasmaFastingGlucose2009 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2009-2010.xpt")
PlasmaFastingGlucose2007 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2007-2008.xpt")
PlasmaFastingGlucose2005 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2005-2006.xpt")
PlasmaFastingGlucose2003 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2003-2004.xpt")
PlasmaFastingGlucose2001 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_2001-2002.xpt")
PlasmaFastingGlucose1999 = pd.read_sas("data/raw/Lab_PlasmaFastingGlucose_1999-2000.xpt")
# C-Reactive Protein (CRP)
CReactiveProtein2017 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2017-2018.xpt")
CReactiveProtein2015 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2015-2016.xpt")
CReactiveProtein2009 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2009-2010.xpt")
CReactiveProtein2007 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2007-2008.xpt")
CReactiveProtein2005 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2005-2006.xpt")
CReactiveProtein2003 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2003-2004.xpt")
CReactiveProtein2001 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_2001-2002.xpt")
CReactiveProtein1999 = pd.read_sas("data/raw/Lab_C-ReactiveProtein(CRP)_1999-2000.xpt")
# Cotinine & Hydroxycotinine - Serum
CotinineandHydroxycotinineSerum2017 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2017-2018.xpt")
CotinineandHydroxycotinineSerum2015 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2015-2016.xpt")
CotinineandHydroxycotinineSerum2013 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2013-2014.xpt")
CotinineandHydroxycotinineSerum2011 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2011-2012.xpt")
CotinineandHydroxycotinineSerum2009 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2009-2010.xpt")
CotinineandHydroxycotinineSerum2007 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2007-2008.xpt")
CotinineandHydroxycotinineSerum2005 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2005-2006.xpt")
CotinineandHydroxycotinineSerum2003 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2003-2004.xpt")
CotinineandHydroxycotinineSerum2001 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_2001-2002.xpt")
CotinineandHydroxycotinineSerum1999 = pd.read_sas("data/raw/Lab_CotinineandHydroxycotinine-Serum_1999-2000.xpt")
# Complete Blood Count with 5-Part Differential
CompleteBloodCountwith5PartDifferential2017 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2017-2018.xpt")
CompleteBloodCountwith5PartDifferential2015 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2015-2016.xpt")
CompleteBloodCountwith5PartDifferential2013 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2013-2014.xpt")
CompleteBloodCountwith5PartDifferential2011 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2011-2012.xpt")
CompleteBloodCountwith5PartDifferential2009 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2009-2010.xpt")
CompleteBloodCountwith5PartDifferential2007 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2007-2008.xpt")
CompleteBloodCountwith5PartDifferential2005 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2005-2006.xpt")
CompleteBloodCountwith5PartDifferential2003 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2003-2004.xpt")
CompleteBloodCountwith5PartDifferential2001 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_2001-2002.xpt")
CompleteBloodCountwith5PartDifferential1999 = pd.read_sas("data/raw/Lab_CompleteBloodCountwith5-PartDifferential_1999-2000.xpt")
# Cholesterol - Total
CholesterolTotal2017 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2017-2018.xpt")
CholesterolTotal2015 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2015-2016.xpt")
CholesterolTotal2013 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2013-2014.xpt")
CholesterolTotal2011 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2011-2012.xpt")
CholesterolTotal2009 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2009-2010.xpt")
CholesterolTotal2007 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2007-2008.xpt")
CholesterolTotal2005 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2005-2006.xpt")
CholesterolTotal2003 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2003-2004.xpt")
CholesterolTotal2001 = pd.read_sas("data/raw/Lab_Cholesterol-Total_2001-2002.xpt")
CholesterolTotal1999 = pd.read_sas("data/raw/Lab_Cholesterol-Total_1999-2000.xpt")
# Cholesterol - LDL
CholesterolLDL2017 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2017-2018.xpt")
CholesterolLDL2015 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2015-2016.xpt")
CholesterolLDL2013 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2013-2014.xpt")
CholesterolLDL2011 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2011-2012.xpt")
CholesterolLDL2009 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2009-2010.xpt")
CholesterolLDL2007 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2007-2008.xpt")
CholesterolLDL2005 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2005-2006.xpt")
CholesterolLDL2003 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2003-2004.xpt")
CholesterolLDL2001 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_2001-2002.xpt")
CholesterolLDL1999 = pd.read_sas("data/raw/Lab_Cholesterol-LDL_1999-2000.xpt")
# Cholesterol - HDL
CholesterolHDL2017 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2017-2018.xpt")
CholesterolHDL2015 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2015-2016.xpt")
CholesterolHDL2013 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2013-2014.xpt")
CholesterolHDL2011 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2011-2012.xpt")
CholesterolHDL2009 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2009-2010.xpt")
CholesterolHDL2007 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2007-2008.xpt")
CholesterolHDL2005 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2005-2006.xpt")
CholesterolHDL2003 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2003-2004.xpt")
CholesterolHDL2001 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_2001-2002.xpt")
CholesterolHDL1999 = pd.read_sas("data/raw/Lab_Cholesterol-HDL_1999-2000.xpt")
# Albumin & Creatinine - Urine
AlbuminCreatinineUrine2017 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2017-2018.xpt")
AlbuminCreatinineUrine2015 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2015-2016.xpt")
AlbuminCreatinineUrine2013 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2013-2014.xpt")
AlbuminCreatinineUrine2011 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2011-2012.xpt")
AlbuminCreatinineUrine2009 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2009-2010.xpt")
AlbuminCreatinineUrine2007 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2007-2008.xpt")
AlbuminCreatinineUrine2005 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2005-2006.xpt")
AlbuminCreatinineUrine2003 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2003-2004.xpt")
AlbuminCreatinineUrine2001 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 2001-2002.xpt")
AlbuminCreatinineUrine1999 = pd.read_sas("data/raw/Lab_Albumin&Creatinine-Urine_ 1999-2000.xpt")

PREFIX_TO_LABEL = {
    "StandardBiochemistryProfile": "Standard Biochemistry Profile",
    "PlasmaFastingGlucose": "Plasma Fasting Glucose",
    "CReactiveProtein": "C-Reactive Protein (CRP)",
    "CotinineandHydroxycotinineSerum": "Cotinine and Hydroxycotinine (Serum)",
    "CompleteBloodCountwith5PartDifferential": "Complete Blood Count with 5-Part Differential",
    "CholesterolTotal": "Cholesterol - Total",
    "CholesterolLDL": "Cholesterol - LDL",
    "CholesterolHDL": "Cholesterol - HDL",
    "AlbuminCreatinineUrine": "Albumin and Creatinine (Urine)",
}

pat = re.compile(rf'^({"|".join(PREFIX_TO_LABEL.keys())})(\d{{4}})$')

# tag each DF and group by domain
by_domain = {k: [] for k in PREFIX_TO_LABEL}
for name, obj in list(globals().items()):
    m = pat.match(name)
    if m and isinstance(obj, pd.DataFrame):
        prefix, start_str = m.groups()
        start = int(start_str)
        years = f"{start}-{start+1}"
        # add columns in place
        obj["Cycle"] = years
        by_domain[prefix].append(obj)

# concat each domain
domain_all = {
    k: pd.concat(v, axis=0, ignore_index=True) for k, v in by_domain.items() if v
}

StandardBiochemistryProfile_all = domain_all.get("StandardBiochemistryProfile")
PlasmaFastingGlucose_all = domain_all.get("PlasmaFastingGlucose")
CReactiveProtein_all = domain_all.get("CReactiveProtein")
CotinineandHydroxycotinineSerum_all = domain_all.get("CotinineandHydroxycotinineSerum")
CompleteBloodCountwith5PartDifferential_all = domain_all.get("CompleteBloodCountwith5PartDifferential")
CholesterolTotal_all = domain_all.get("CholesterolTotal")
CholesterolLDL_all = domain_all.get("CholesterolLDL")
CholesterolHDL_all = domain_all.get("CholesterolHDL")
AlbuminCreatinineUrine_all = domain_all.get("AlbuminCreatinineUrine")

def _latest_cycle(series: pd.Series):
    s = series.dropna().astype(str)
    if s.empty:
        return np.nan
    # expects strings like "YYYY-YYYY"
    start = s.str.extract(r'(\d{4})')[0].astype(int).max()
    return f"{start}-{start+1}"

def collapse_by_respondent_keep_cycle(df, idcol="SEQN"):
    meta = ("Cycle",)
    data_cols = [c for c in df.columns if c not in (idcol,) + meta]
    out = df.copy()
    out[data_cols] = out[data_cols].replace(0, np.nan)

    agg = {c: "max" for c in data_cols}
    if "Cycle" in out.columns:
        agg["Cycle"] = _latest_cycle

    return out.groupby(idcol, as_index=False).agg(agg)

def drop_all_nan_rows(df, ignore_cols=("SEQN","Cycle")):
    subset = [c for c in df.columns if c not in ignore_cols]
    return df.dropna(subset=subset, how="all").copy()


StandardBiochemistryProfile_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(StandardBiochemistryProfile_all))
PlasmaFastingGlucose_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(PlasmaFastingGlucose_all))
CReactiveProtein_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CReactiveProtein_all))
CotinineandHydroxycotinineSerum_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CotinineandHydroxycotinineSerum_all))
CompleteBloodCountwith5PartDifferential_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CompleteBloodCountwith5PartDifferential_all))
CholesterolTotal_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CholesterolTotal_all))
CholesterolLDL_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CholesterolLDL_all))
CholesterolHDL_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(CholesterolHDL_all))
AlbuminCreatinineUrine_all1 = drop_all_nan_rows(collapse_by_respondent_keep_cycle(AlbuminCreatinineUrine_all))

keep_vars = [
    "SEQN",  # Respondent ID
    "Cycle",
    "URDACT", # Albumin creatinine ratio (mg/g),
    "LBDHDD", # HDL 1
    "LBDHDL", # HDL 2
    "LBDLDL", # LDL
    "LBXTR", # Triglyceride
    "LBXTC", # Total Cholesterol
    "LBXHGB", # Hemoglobin
    "LBXRDW", # red cell distribution width
    "LBXWBCSI", # white blood cell count
    "LBXCOT", # cotinine
    "LBXHSCRP", # high sensitivity C-Reactive Protein
    "LBXGLU", # fasting glucose
    "LBXSCR", # creatinine
    "LBXSUA", # uric acid
    "LBXSAL", # albumin
]


laboratory_all = pd.concat([StandardBiochemistryProfile_all, PlasmaFastingGlucose_all,CReactiveProtein_all,CotinineandHydroxycotinineSerum_all,CompleteBloodCountwith5PartDifferential_all,CholesterolTotal_all,CholesterolLDL_all,CholesterolHDL_all,AlbuminCreatinineUrine_all], axis=0, ignore_index = True)
laboratory_subset = laboratory_all[keep_vars]
laboratory_subset = collapse_by_respondent_keep_cycle(laboratory_subset)
laboratory_subset = laboratory_subset.rename(columns = {
    "URDACT": "Albumin creatinine ratio (mg/g)",
    "LBDHDD": "Direct HDL-Cholesterol (mg/dL)",
    "LBDHDL": "HDL-cholesterol (mg/dL)",
    "LBDLDL": "LDL-Cholesterol, Friedewald (mg/dL)",
    "LBXTR": "Triglyceride (mg/dL)",
    "LBXTC": "Total Cholesterol (mmol/L)",
    "LBXHGB": "Hemoglobin  (g/dL)",
    "LBXRDW": "red cell distribution width (%)",
    "LBXWBCSI": "White blood cell count (1000 cells/uL)",
    "LBXCOT": "Cotinine, Serum (ng/mL)",
    "LBXHSCRP": "High-Sensitivity C-Reactive Protein (hs-CRP) (mg/L)",
    "LBXGLU": "Fasting Glucose (mmol/L)",
    "LBXSCR": "Creatinine, refrigerated serum (umol/L)",
    "LBXSUA": "Uric acid (umol/L)",
    "LBXSAL": "Albumin, refrigerated serum (g/dL)"
})

laboratory_subset.to_csv("data/interim/laboratory_subset5.csv", index=False)

print("Demographics data subset saved successfully!")
