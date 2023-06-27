import requests

products_url = requests.get("https://dummyjson.com/products")
products = products_url.json()
pA = products["products"]
arrLen = len(pA)
res = dict()
for i in range(0, arrLen):
    category = pA[i]['category']
    brand = pA[i]['brand']
    title = pA[i]['title']
    if brand not in res:
        res[brand] = []
    res[brand].append(title)
print(res)