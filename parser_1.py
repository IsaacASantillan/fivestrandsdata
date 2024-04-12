import pandas as pd 
import matplotlib.pyplot as plt


gsheetid = "1dSOcxGzBXrQA4uzvrJ_Gt4Qm-Bq0FTWNBtj1fuUlNds"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

print(gsheet_url)

df = pd.read_csv(gsheet_url)

#Parse data
keepcol = []
for col in df.columns:
    if col == "County" or col == "District Name" or col == "District Type" or col == "Number of Schools" or col =="Student Enrollment" or col == "Size of District":
        keepcol.append(col)
    if "Score" in col:
        keepcol.append(col)
df = df[keepcol]

#Sidebar Values
sizesselection = pd.unique(df["Size of District"].values)
countiesselection = sorted(pd.unique(df["County"].values))