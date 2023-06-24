import requests  # imported module to make https requests
import json      # imported module to work on json files
product_url = requests.get("https://dummyjson.com/products") #hitting api
products = product_url.json()# storing json object in products variable
file_path = "store.json" #assigning store.json file to a variable file_path
file_path2 = "orderbook.json"#assigning assigning "orderbook.json"file to a varibale file_path2
def initialiseorderbook(products): #declared function to initialise the products to 0
    
    sold_item={} #created an empty dict and stored in variable "sold_item"
    products = products.get("products")# reading products array from "products" object
    for product in products:#iterating each product in the array in the products array
        sold_item[product["title"]] = 0 # for each product, set product title as key in the sold_item variable and initialise to 0.
        
    save_file(sold_item,file_path2) #calling save file to save the sold_item dict to "orderbook.json"(file_path2) file   
#initialiseorderbook(products)
        
def save_file(data, file_path): #declaring a function with two parameter, data and file_path
    with open(file_path, 'w') as file: #opens "store.json" in 'w' mode
        json.dump(data, file)  # writing to json objects
#save_file(products,file_path)
def buyProduct(product_name): #delaring a function with "product_name" parameter
    try:
        
        with open(file_path,"r") as file: #reading "store.json"file
            data = json.load(file)# loads the json data from the file into the data variable
            products = data.get("products")#reading products array from data object
            
            for product in products:   #parsing each product in products
                if product["title"]==product_name:   #checking condition if product title match with product_name
                    if product["stock"]>0:   #checking if product stock is >0
                        product["stock"]-=1  # if ture, then decrement stock by 1
                        save_file(data,file_path)  # calling save_file function to save the data to "store.json"
                        with open(file_path2, 'r') as file1:   #reading "orderbook.json"
                            data1 = json.load(file1)           #loads json data to "data1" variable
                            data1[product_name]+=1             # increments the purchased product
                            save_file(data1,file_path2)        #saves to orderbook.json file
                            
                            
                        print("found product")  #printing statment
                        break 
                    else:
                        print("out of stock") #printing statement
    except FileNotFoundError: #raising exception
        print("file not found") #printing statement
def numofproductsinstock(product_name): #decalring a func to check the num of products present in the stock
    with open(file_path,"r") as file: #reading file from store.json
        prdcts = json.load(file)# loading the json data from the file and stores ro "prdcts"variable
        prdcts = prdcts.get("products")    #reading array products from prdcts object
        for prdct in prdcts: #parsing each product in prdcts
            if prdct["title"]==product_name: #check condition if the prdct title match with product_name
                return prdct["stock"]                #returns the count of the product
        
        
buyProduct("iPhone X")
nps = numofproductsinstock("iPhone X")
print(nps)        
