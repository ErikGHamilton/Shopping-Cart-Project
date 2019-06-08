# SHOPPING CART PROGRAM


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
print("")

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

#print("test")
#print(products2[3]['name'], products2[3]['price']) #sorted by id, print name/price


# HIDDEN/minized- Printing all twenty - here for reference
    #remove indent if you want to use
    #print(numproducts)
    #print("")
    #
    #prod_count = 0
    #while prod_count < numproducts:    #put in a variable here later that counts the number of products
    #    print("   + ",products2[prod_count]['name'],"-",products2[prod_count]['price'])
    #    prod_count = prod_count + 1
    #
    #print("")
    #


initial_input_false = False
while not initial_input_false:
    initial_input = int(input("Please Enter The Product ID Number:"))
    if initial_input > numproducts or initial_input < 0:
        print("Please Enter a Valid ID Number:")
    else:
        initial_input_false = True


input_array = [initial_input]

finished_entering = False
while not finished_entering:
    clerk_input = input("Please Enter The Product ID Number:")
    if clerk_input == "done" or clerk_input == "DONE" or clerk_input == "Done":
        finished_entering = True
    else:
        int_clerk_input = int(clerk_input)
    if initial_input > numproducts or initial_input < 0:
        print("Please Enter a Valid ID Number:")
    else:
        input_array.append(int_clerk_input)


print(input_array)
