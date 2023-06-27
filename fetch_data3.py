import requests

products_url = requests.get("https://dummyjson.com/products")
products = products_url.json()
pA = products["products"]
arr_len = len(pA)
res = dict()
for i in range(0,arr_len):
    category = pA[i]["category"]
    brand = pA[i]["brand"]
    title = pA[i]["title"]
    description = pA[i]["description"]
    price = pA[i]["price"]
    if category not in res:
        res[category] = {}
    if brand not in res[category]:
        res[category][brand] = []
    res[category][brand].append({"title":title, "description":description,"Price":price}) 
res 