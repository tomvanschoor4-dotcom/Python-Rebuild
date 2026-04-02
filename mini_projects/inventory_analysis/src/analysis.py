import pandas as pd

# load data
df = pd.read_excel("../data/914_fiscal_recap_data_dump.xlsx")

# quick preview
print("Original shape:",df.shape)
print(df.head())
# remove rows where key fields are missing
df=df.dropna(subset=["Dept","SKU","Item"])
# drop fully useless column
df = df.drop(columns=["Metrics"],errors="ignore")
# optional ; reset index after cleaning
df = df.reset_index(drop=True)

print("\nCleaned Shape:",df.shape)
print(df.head())
# columns
print(df.columns)
print(df.info())
# info
print(df.info())