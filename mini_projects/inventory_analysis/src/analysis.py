import pandas as pd
pd.options.display.float_format='{:,.0f}'.format

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
# print(df.columns)
# info
print(df.info())

# filtering to the latest week // latest week in the dataset
latest_week=df["Week End"].max()
print("\nLatest Week End:",latest_week)

# keep only latest week
df_latest = df[df["Week End"]==latest_week].copy()
print("Latest Week Shape:", df_latest.shape)
print(df_latest[["Week Start","Week End"]].drop_duplicates().head())

# top 10 items by DTC Netsales
top_items = (
    df.groupby(["SKU","Item"],as_index=False)["DTC Netsales $s"]
    .sum()
    .sort_values("DTC Netsales $s", ascending=False)
    .head(10)
)
print("\nTop 10 Items by DTC Netsales:")
print(top_items)

# category level summary
category_summary = (
    df.groupby(["Dept","Class","Subclass"],as_index=False)
    .agg(
        dtc_netsales=("DTC Netsales $s","sum"),
        dtc_netsales_ly=("DTC Netsales $s LY","sum"),
        dtc_demand=("DTC Gross Demand Us","sum"),
        sku_count=("SKU","nunique")
    )
    .sort_values("dtc_netsales",ascending=False)
)

print("\nCategory Summary:")
print(category_summary.head(10))

# sales YoY percentage
category_summary["sales_yoy_pct"]=(
    (category_summary["dtc_netsales"]-category_summary["dtc_netsales_ly"])
    .div(category_summary["dtc_netsales_ly"].replace(0,pd.NA))
    *100
)
print("\nCategory Summary with YoY %:")
print(category_summary.head(10))