import time
import sys
import itertools

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

def rotating_effect(message, duration=2):
    symbols = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in symbols:
            sys.stdout.write(f"\r{message} {symbol}")
            sys.stdout.flush()
            time.sleep(0.2)
    # Clear the line and replace it with a final message
    sys.stdout.write(f"\r{message}... Done! 🎉\n")
    sys.stdout.flush()

def display_Menu_Items():
    rotating_effect("🔄 Initializing Vending Machine Menu")
    print("\n🌟Welcome to Bath Spa's Vending Mahine🌟!")
    time.sleep(2)
    print("Choose from the following items in our vending machine: ")
    for code, item in products.items():
        if item["stock"] > 0:
            print(f"[{code}] {item["name"]} : £{item["price"]:.2f} ({item["stock"]} available in stock)")
            time.sleep(0.5)
                  

def Flavor_Selection(flavors):
    rotating_effect("🚀 Loading your flavor options...")
    print("\nWhat's your preferred flavor? Take your pick!")
    time.sleep(1)
    for i, flavor in enumerate(flavors, 1):
        print(f"[{i}] {flavor}")
        time.sleep(0.5)
    while True:
        try:
            options = int(input("Choose a flavor by entering its number:"))
            if 1 <= options <= len(flavors):
                return flavors[options - 1]    
            else:
                print("Oops! That's not a valid choice. Please try again. 🙁")
                time.sleep(1)
        except ValueError:
            print("Please enter a number from the list. ⚠️") 
            time.sleep(1)       


def Execute_Payment(price):
    correct_password = "12345"
    max_attempts = 3

    while True:
        print("\nPayment Options: 1. Cash  2. Credit Card")
        time.sleep(0.5)
        payment_method = input("Choose your payment method by entering 1 or 2: ").strip()
        time.sleep(2)

        if payment_method == "1":
            while True:
                try:
                    money = float(input(f"Insert money £{price:.2f}: "))
                    if money < price:
                        print(f"Not enough cash! Just £{price - money:.2f} more and it's all yours! 🎉")
                        time.sleep(1)
                    else:
                        return money - price
                except ValueError:
                    print("That's not quite right. Please enter a number to continue! 🔄")
                    time.sleep(1)
        elif payment_method == "2":
            print(f"Processing your credit card payment of £{price:.2f}... 💳")
            rotating_effect("🔄 Validating card details... Please wait")
            time.sleep(2)
            attempts = 0
            while attempts < max_attempts:
                password = input("Enter the credit card PIN: ").strip()
                if password == correct_password:
                    rotating_effect("🔓 Verifying PIN...")
                    time.sleep(1)
                    print("Payment successful! ✅ Transaction approved!")
                    return 0
                else:
                    attempts += 1
                    attempts_left = max_attempts - attempts
                    print(f"🛑 Access denied, try again! You have {attempts_left} attempts left.")
            if attempts == max_attempts:
                print("Maximum login attempts reached. Your card is temporarily blocked. ❌")
                return None
        else:
            print("Invalid option! Please choose 1 for Cash or 2 for Credit Card.")

def Dispensing_Animation(item_name):
    print("\nDispensing your item... Please wait.")
    time.sleep(1)
    animation = [
        "🟩⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟩🟩⬜⬜⬜⬜⬜⬜⬜",
        "🟩🟩🟩⬜⬜⬜⬜⬜⬜",
        "🟩🟩🟩🟩⬜⬜⬜⬜⬜",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜",
        "🟩🟩🟩🟩🟩🟩⬜⬜⬜",
        "🟩🟩🟩🟩🟩🟩🟩⬜⬜",
        "🟩🟩🟩🟩🟩🟩🟩🟩⬜",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩"
    ]
    for frame in animation:
        print(frame, end="\r")
        time.sleep(0.3)
    print(f"🎉 Enjoy your {item_name}! Foodie🎉")  
    time.sleep(0.5)          


def Collect_Feedback():
    while True:
        try:
            rating = int(input("\nRate your satisfaction with the purchase process of this item (1-5): "))
            time.sleep(1)
            if 1 <= rating <= 5:
                print(f"We appreciate your feedback! You rated this item {rating} out of 5. 🏷️")
                time.sleep(1)
                return rating
            else:
                print("To submit your feedback, kindly enter a number between 1 and 5.")
                time.sleep(1)
        except ValueError:
            print("Rating should be between 1 and 5. Please re-enter your rating 🔄.")
            time.sleep(1)


def Vending_Machine():
    while True:
        display_Menu_Items()
        code = input("\nYour choice awaits🥰! Enter the code or 'exit' to stop! 🚀: ").strip().upper()

        if code.lower() == "exit":
            print("\nEnjoy your goodies🍽️! Thank you for using the BSU vending machine! 🙌🎉")
            time.sleep(1)
            break

        if code not in products:
            print("⚠️ Code not recognized. Give it another shot.")
            time.sleep(1)
            continue

        item = products[code]
        if item["stock"] <= 0:
            print("That item is no longer available. Please try another option 🎯.")
            time.sleep(1)
            continue

        selected_flavor = None
        if item["flavors"]:
            selected_flavor = Flavor_Selection(item["flavors"])

        change = Execute_Payment(item["price"])
        if change is None:
            continue

        item["stock"] -= 1

        Dispensing_Animation(item['name'])
        print(f"\nYour change💸: £{change:.2f}" if change > 0 else "No change to return. Thank you!")
        time.sleep(1)

        rating = Collect_Feedback()

        # Ask if user wants another item
        while True:
            another = input("\nWould you like to choose another item? (yes/no): ").strip().lower()
            time.sleep(1)
            if another == "yes":
                print("\nTaking you back to the menu... 🛒")
                time.sleep(2)
                break
            elif another == "no":
                print("\nThank you for using Bath Spa's Vending Machine! 🙌😊 See you soon! 🚀")
                return
            else:
                print("Invalid input. Please type 'yes' to choose another item or 'no' to exit. ⚠️")


Vending_Machine() 
           








