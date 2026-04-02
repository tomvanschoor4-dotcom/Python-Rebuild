# with    open("data.txt","r") as file:
#     content = file.read()

# print(content)

# with open("output.txt", "w") as file:
#     file.write("This is my output file\n")
#     file.write("Python is useful\n")

# import csv

# with open("sales.csv","r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# import csv

# with open("sales.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row["product"],row["price"])

import pandas as pd


space = " "
print(space)
df = pd.read_csv("sales.csv")
# print(df)
print(space)
# print(df.head())
# print(df.describe())
print(space)
# Add a New Column (VERY IMPORTANT)
df["Total"] = df["price"]*df["quantity"]
print(df)
# Aggregate Data (THIS = YOUR JOB)
totalRevenue = df["Total"].sum()
print(space)
print("Total Revenue:",totalRevenue)
# Grouping (Like Pivot Tables 👀)
# print(space)
# df.groupby("product")["Total"].sum()
# print(df.groupby("product")["Total"].sum())
df.groupby("product", as_index=False)["Total"].sum()
