import requests
import json
product_url = requests.get("https://dummyjson.com/products")
products = product_url.json()
file_path = "store.json"
def save_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)  
def BuyProduct(product_name):    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            products = data.get("products")
            
            for product in products:
                if product["title"] == product_name:
                    if product["stock"]>0:
                        product['stock']-=1
                        save_file(data,file_path)
                        #update_sold_data(product_name, sold_file_path)
                        print("purchased successfully.")
                        return
                    else:
                        print("is out of stock.")
                        return

            print("Product not found.")
#def sold_data(product_name):
    
    
    except FileNotFoundError:
        print("File not found.")
BuyProduct("Handcraft Chinese style")
