# SHOPPING CART PROGRAM
import time
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



print("")
print("---------------------")
print("There are 20 Products")
print("---------------------")
print("Enter The Product IDs and Type 'Done' When Finished")
print("")
time.sleep(0.5)

def prod_id(product):
    return product['id']

def prod_name(product):
    return product['name']

def prod_dept(product):
    return product['department']

def prod_aisle(product):
    return product['aisle']

def prod_price(product):
    return product['price']

products2 = sorted(products, key=prod_id)
numproducts = len(products)

id_list = []
for i in products2:
    id_list.append(i['id'])

#print(id_list)
#print("test")
#print(products2[3]['name'], products2[3]['price']) #sorted by id, print name/price


#print(id_list)

#initial_input_false = False
#while not initial_input_false:
#    initial_input = int(input("Please Enter The Product ID Number:"))
#    if initial_input not in id_list:
#        print("Please Enter a Valid ID Number:")
#    else:
#        initial_input_false = True
#

input_array = []

finished_entering = False
while not finished_entering:
    clerk_input = input("Please Enter The Product ID Number:")
    if clerk_input == "done" or clerk_input == "DONE" or clerk_input == "Done":
        finished_entering = True
    else:
        pass
    if clerk_input in str(id_list):
        int_clerk_input = int(clerk_input)
        input_array.append(int_clerk_input)
    else:
        print("Please Enter A Valid ID Number")
       
        

#original function
#while not finished_entering:
#    clerk_input = input("Please Enter The Product ID Number:")
#    if clerk_input == "done" or clerk_input == "DONE" or clerk_input == "Done":
#        finished_entering = True
#    else:
#        int_clerk_input = int(clerk_input)
#    if int_clerk_input > numproducts or int_clerk_input < 0:
#        print("Please Enter a Valid ID Number:")
#    else:
#        input_array.append(int_clerk_input)


#print(input_array)
num_entered = len(input_array)
#print(num_entered)
#print(input_array[0])

current_time = datetime.datetime.now()

print("")
print("")
print("")

print("----------------------------")
print("   Erik's Awesome Bodega    ")
print(" www.eriksawesomebodega.com ")
print("----------------------------")
print(str(current_time))
print("----------------------------")
print("PRODUCTS:")
print("")

totalprice = 0
loopcount = 0
#print(input_array[loopcount])
#item = input_array[loopcount] - 1
#print(item)

while loopcount < num_entered:
    item = input_array[loopcount] - 1
    print(" + ", products2[item]['name'],"  $" + str(products2[item]['price'])) 
    loopprice = float(products2[item]['price'])
    totalprice = totalprice + loopprice

    loopcount = loopcount + 1

print("")
print("----------------------------")
totalprice = round(totalprice,2)
print("SUBTOTAL: $" + str(totalprice))
tax = round(totalprice * 0.0875,2)
print("TAX: $" + str(tax))
grandtotal = round(totalprice + tax,2)
print("GRAND TOTAL: $" + str(grandtotal))
print("----------------------------")
print("")