# QUESTION 4: A dictionary with 5 products and their stock quantities
inventory = {
    "Apples": 25,
    "Bananas": 8,
    "Oranges": 15,
    "Mangoes": 5,
    "Pineapples": 12
}

# Adding a new product and updating an existing one
# Add a new product
inventory["Grapes"] = 20

# Update quantity of an existing product
inventory["Bananas"] = 18

# Function to return products with stock less than 10
def low_stock_products(stock_dict):
    return [product for product, quantity in stock_dict.items() if quantity < 10]

# Example usage
low_stock = low_stock_products(inventory)
print("Low stock products:", low_stock)

# Delete a discontinued product and display updated dictionary
# Remove discontinued product
del inventory["Mangoes"]

# Display updated inventory
print("Updated Inventory:", inventory)

# Using .items() to loop and print each product with its quantity
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")
