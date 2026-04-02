import pandas as pd

# Load data
df=pd.read_csv("sales.csv")
# print(df)
# Create total column
df["total"] = df["price"] * df["quantity"]
# Group by product
summary = df.groupby("product", as_index=False)["total"].sum()
# sort highest to lowest
summary = summary.sort_values(by="total",ascending=False)
# output
print("\nSales Summary:\n")
print(summary)

