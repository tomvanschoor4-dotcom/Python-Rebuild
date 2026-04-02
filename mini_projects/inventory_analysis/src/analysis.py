import pandas as pd

# load data
df = pd.read_excel("../data/914_fiscal_recap_data_dump.xlsx")

# preview
print(df.head())

# columns
print(df.columns)

# info
print(df.info())