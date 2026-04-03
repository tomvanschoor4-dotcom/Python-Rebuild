import pandas as pd
pd.options.display.float_format='{:,.0f}'.format


# load data
df = pd.read_excel("../data/dummy revenue data.xlsx")

# quick preview
# print("Original shape:",df.shape)
# print(df.head())
# remove rows where key fields are missing
df=df.dropna(subset=["Dept","SKU","Item"])
# drop fully useless column
df = df.drop(columns=["Metrics"],errors="ignore")
# optional ; reset index after cleaning
df = df.reset_index(drop=True)
# print("\nCleaned Shape:",df.shape)
# print(df.head())
# # columns
# # print(df.columns)
# # info
# print(df.info())
# filtering to the latest week // latest week in the dataset
latest_week=df["Week End"].max()
print("\nLatest Week End:",latest_week)
# keep only latest week
df_latest = df[df["Week End"]==latest_week].copy()
print("Latest Week Shape:", df_latest.shape)
print(df_latest[["Week Start","Week End"]].drop_duplicates().head())

# YoY %
category_summary_latest = (
    df_latest.groupby(["Dept","Class","Subclass"], as_index=False)
    .agg(
        dtc_netsales=("DTC Netsales $s","sum"),
        dtc_netsales_ly=("DTC Netsales $s LY","sum"),
        dtc_demand=("DTC Gross Demand $s","sum"),
        sku_count=("SKU","nunique")
    )
)
category_summary_latest["sales_yoy_pct"]=(
    (category_summary_latest["dtc_netsales"]-category_summary_latest["dtc_netsales_ly"])
    .div(category_summary_latest["dtc_netsales_ly"].replace(0,pd.NA))
    *100
)

category_summary_latest=category_summary_latest.sort_values("dtc_netsales",ascending=False)

print("\nCategory Summary - Lastest Week")
print(category_summary_latest.head(10))

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



prior_week = df[df["Week End"]< latest_week]["Week End"].max()
print("\nPrior Week:",prior_week)

df_prior = df[df["Week End"] == prior_week].copy()

print("Prior week shape:", df_prior.shape)

category_summary_prior = (
    df_prior.groupby(["Dept", "Class", "Subclass"], as_index=False)
    .agg(
        dtc_netsales_pw=("DTC Netsales $s", "sum")
    )
)

category_wow = pd.merge(
    category_summary_latest,
    category_summary_prior,
    on=["Dept", "Class", "Subclass"],
    how="left"
)

category_wow["wow_pct"] = (
    (category_wow["dtc_netsales"] - category_wow["dtc_netsales_pw"])
    .div(category_wow["dtc_netsales_pw"].replace(0, pd.NA))
    * 100
)

category_wow = category_wow.sort_values("dtc_netsales", ascending=False)

print("\nCategory WoW Summary:")
print(category_wow.head(10))

# top items for the latest week
top_items_latest = (
    df_latest.groupby(["SKU","Item"], as_index=False)["DTC Netsales $s"]
.sum()
.sort_values("DTC Netsales $s", ascending=False)
.head(10)
)

print("\nTop 10 Items by DTC Netsales - Latest Week")
print(top_items_latest)

# top 10 items by DTC Netsales
top_items = (
    df.groupby(["SKU","Item"],as_index=False)["DTC Netsales $s"]
    .sum()
    .sort_values("DTC Netsales $s", ascending=False)
    .head(10)
)
print("\nTop 10 Items by DTC Netsales:")
print(top_items)

