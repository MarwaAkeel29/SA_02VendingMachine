# Vending Machine Products
products = {
    "A01": {"name": "Tea", "price": 1.50, "stock": 8, "flavors": ["Cinnamon", "Green", "Black", "Herbal"]},
    "A02": {"name": "Coffee", "price": 2.70, "stock": 10, "flavors": ["Turkish Coffee", "Macchiato", "Espresso", "Pumpkin Spice Latte", "Cappuccino"]},
    "A03": {"name": "Soda", "price": 3.00, "stock": 12, "flavors": ["Cola", "Pepsi", "Powerade", "Sprite", "Vimto"]},
    "B01": {"name": "Chocolate Bar", "price": 2.80, "stock": 7, "flavors": ["Dark Chocolate", "Tiramisu", "Hazelnut"]},
    "B02": {"name": "Chips", "price": 2.00, "stock": 5, "flavors": ["Flamin' Hot", "Cheddar Cheese", "Spicy Barbecue"]},
    "B03": {"name": "Water", "price": 1.00, "stock": 15, "flavors": ["Regular", "Mineral", "Sparkling"]},
    "C01": {"name": "Pastries", "price": 5.25, "stock": 12, "flavors": ["Ferrero Delight", "Red Velvet", "White Forest"]},
    "C02": {"name": "Cookies", "price": 4.00, "stock": 7, "flavors": ["Chocolate Chip", "Butterscotch", "Oreo-Nutella"]}
}

def display_Menu_Items():
    print("Welcome to Bath Spa's Vending Mahine🌟!")
    print("Choose from the following items in our vending machine:")
    for code, item in products.items():
        if item["stock"] > 0:
            print(f"[{code}] {item["name"]} : £{item["price"]:.2f} ({item["stock"]} available in stock)")
                  

def Flavor_Selection(flavors):
    print("What's your preferred flavor? Take your pick!")
    for i, flavor in enumerate(flavors, 1):
        print(f"[{i}] {flavor}")
    while True:
        try:
            options = int(input("Choose a flavor by its number below:"))
            if 1 <= options <= len(flavors):
                return flavors[options - 1]    
            else:
                print("Oops! That’s not a valid choice. Please try again. 🙁")
        except ValueError:
            print("Please enter a number from the list. ⚠️")        








