#writing products to json file
import requests
import json

products_url = requests.get("https://dummyjson.com/products")
products = products_url.json()

file_path = "products.json"
with open(file_path, 'w') as f:
    json.dump(products,f)