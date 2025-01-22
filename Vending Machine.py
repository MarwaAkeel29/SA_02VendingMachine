# Vending Machine Products
products = {
    "A01": {"name": "Tea", "price": 1.50, "stock": 8, "flavors": ["Cinnamon", "Green", "Black", "Herbal"], "ratings": []},
    "A02": {"name": "Coffee", "price": 2.70, "stock": 10, "flavors": ["Turkish Coffee", "Macchiato", "Espresso", "Pumpkin Spice Latte", "Cappuccino"], "ratings": []},
    "A03": {"name": "Soda", "price": 3.00, "stock": 12, "flavors": ["Cola", "Pepsi", "Powerade", "Sprite", "Vimto"], "ratings": []},
    "B01": {"name": "Chocolate Bar", "price": 2.80, "stock": 7, "flavors": ["Dark Chocolate", "Tiramisu", "Hazelnut"], "ratings": []},
    "B02": {"name": "Chips", "price": 2.00, "stock": 5, "flavors": ["Flamin' Hot", "Cheddar Cheese", "Spicy Barbecue"], "ratings": []},
    "B03": {"name": "Water", "price": 1.00, "stock": 15, "flavors": ["Regular", "Mineral", "Sparkling"], "ratings": []},
    "C01": {"name": "Pastries", "price": 5.25, "stock": 12, "flavors": ["Ferrero Delight", "Red Velvet", "White Forest"], "ratings": []},
    "C02": {"name": "Cookies", "price": 4.00, "stock": 7, "flavors": ["Chocolate Chip", "Butterscotch", "Oreo-Nutella"], "ratings": []}
}

def display_Menu_Items():
    print("Welcome to Bath Spa's Vending Mahine🌟!")
    print("Choose from the following items in our vending machine: ")
    for code, item in products.items():
        if item["stock"] > 0:
            print(f"[{code}] {item["name"]} : £{item["price"]:.2f} ({item["stock"]} available in stock)")
                  

def Flavor_Selection(flavors):
    print("What's your preferred flavor? Take your pick!")
    for i, flavor in enumerate(flavors, 1):
        print(f"[{i}] {flavor}")
    while True:
        try:
            options = int(input("Choose a flavor by entering its number:"))
            if 1 <= options <= len(flavors):
                return flavors[options - 1]    
            else:
                print("Oops! That's not a valid choice. Please try again. 🙁")
        except ValueError:
            print("Please enter a number from the list. ⚠️")        

def Execute_Payment(price):
    correct_password = "12345"
    max_attempts = 3

    while True:
        print("Payment Options: 1. Cash  2. Credit Card")
        payment_method = input("Choose your payment method by entering 1 or 2: ").strip()

        if payment_method == "1":
            while True:
                try:
                    money = float(input(f"Insert money £{price:.2f}: "))
                    if money < price:
                        print(f"Not enough cash! Just £{price - money:.2f} more and it's all yours! 🎉") 
                    else:
                        return money - price
                except ValueError:
                    print("That's not quite right. Please enter a number to continue! 🔄")   

        elif payment_method == "2":
            print(f"Processing your credit card payment of £{price:.2f}... 💳") 
            
        attempts = 0 
        while attempts < max_attempts:
            password = input("Enter the credit card PIN: ").strip()
            if password == correct_password:
                print("Payment successful! ✅ Transaction approved!")
                return 0 
            else:
                attempts += 1
                attempts_left = max_attempts - attempts
                print(f"🛑 Access denied, try again! You have {attempts_left} attempts left.")

        if attempts == max_attempts:
            print("Maximum login attempts reached, the card will be blocked temporarily for security reasons❌.")
            print("You may need to contact your bank to unlock it")
            return None
        
        else:
            print("Invalid option! Please choose 1 for Cash or 2 for Credit Card.")

def collect_Feedback():
    while True:
        try:
            rating = int(input("Rate your satisfaction with the purchase process of this item (1-5). "))
            if 1 <= rating <= 5:
                print(f"We appreciate your feedback! You rated this item {rating} out of 5. 🏷️")
                return rating
            else:
                print("To submit your feedback, kindly enter a number between 1 and 5")
        except ValueError:
            print("Rating should be between 1 and 5. Please re-enter your rating 🔄.") 








