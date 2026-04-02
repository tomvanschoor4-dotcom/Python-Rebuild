import pandas as pd

# Load data
df=pd.read_csv("sales.csv")
# print(df)
# Create total revenue column
df["total"] = df["price"] * df["quantity"]
# Build summary table
summary = df.groupby("product", as_index=False).agg({
    "total": "sum",
    "quantity": "sum"
})
# renaming columns
summary = summary.rename(columns={
    "total":"Revenue",
    "quantity":"Units Sold"
}) 
# sort highest to lowest
summary = summary.sort_values(by="Revenue",ascending=False)
# Print output to terminal
print("\nSales Summary:\n")
print(summary)
# Exporting to CSV
summary.to_csv("sales_summary.csv",index=False)
print("\nSaved file : sales_summary.csv")
