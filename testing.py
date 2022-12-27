import json

f = open("122722.json")
data = json.load(f)
# print(data

for i in data:
    print(i["customer_phone"])