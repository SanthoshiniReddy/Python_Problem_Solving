import requests

response = requests.get("https://dummyjson.com/products")
products= response.json()
pA = products["products"]
arrLen = len(pA)
res = dict()
for i in range(0,arrLen):
    category = pA[i]['category']
    brand = pA[i]['brand']
    title = pA[i]['title']
    if category not in res:
        res[category] = {}
    if brand not in res[category]:
        res[category][brand] = []
    res[category][brand].append(title)
print(res)  