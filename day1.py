#name = "Tom"
#age = 25
#salary = 70500
#is_analyst = True

#products = ["Crib", "Stroller", "Toy"]

#sales = {
#    "Cribs" : 1200,
#    "Stroller" : 800,
#    "Toy" : 150
#}

#for product in products:
    #print(product)

#for items, revenue in sales.items():
    #print(items,revenue)

#for item, revenue in sales.items():
#   if revenue >= 500:
#        print(f"{item} is a top performer")
#    else:
#        print(f"{item} is a low performer")

#def classify_sales(revenue):
#    if revenue > 1000:
#        return "High"
#    elif revenue > 500:
#        return "Medium"
#    else:
#        return "Low"
    
#result = classify_sales(800)
#print(result)
space = ""

weekly_sales = {
    "Crib": 1200,
    "Stroller": 800,
    "Toy": 150,
    "Monitor": 950,
    "Chair": 400
}

def analyze_sales(data):
    for product, sales in data.items():
        if sales > 900:
            print(f"{product}: Top Seller")
        elif sales > 500:
            print(f"{product}: Mid Performer")
        else:
            print(f"{product}: Low Performer")

analyze_sales(weekly_sales)

print(space)

def summarize_sales(data):
    total = sum(data.values())
    avg = total / len(data)

    print(f"Total Sales: {total}")
    print(f"Average Sales: {avg}")

summarize_sales(weekly_sales)

print(space)

import pandas as pd

df = pd.DataFrame(list(weekly_sales.items()), columns=["Product", "Sales"])
print(df)

