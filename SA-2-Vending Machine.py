import time # Import time module
import sys  # Import sys module
import itertools # Import itertools module

# Vending Machine Products
products = {
    "A01": {"name": "Tea", "price": 1.50, "stock": 8, "flavors": ["Cinnamon", "Green", "Black", "Herbal"]},  # Tea product details
    "A02": {"name": "Coffee", "price": 2.70, "stock": 10, "flavors": ["Turkish Coffee", "Macchiato", "Espresso", "Pumpkin Spice Latte", "Cappuccino"]}, # Coffee product details
    "A03": {"name": "Soda", "price": 3.00, "stock": 12, "flavors": ["Cola", "Pepsi", "Powerade", "Sprite", "Vimto"]}, # Soda product details
    "B01": {"name": "Chocolate Bar", "price": 2.80, "stock": 7, "flavors": ["Dark Chocolate", "Tiramisu", "Hazelnut"]},  # Chocolate Bar product details
    "B02": {"name": "Chips", "price": 2.00, "stock": 5, "flavors": ["Flamin' Hot", "Cheddar Cheese", "Spicy Barbecue"]}, # Chips product details
    "B03": {"name": "Water", "price": 1.00, "stock": 15, "flavors": ["Regular", "Mineral", "Sparkling"]}, # Water product details
    "C01": {"name": "Pastries", "price": 5.25, "stock": 12, "flavors": ["Ferrero Delight", "Red Velvet", "White Forest"]}, # Pastries product details
    "C02": {"name": "Cookies", "price": 4.00, "stock": 7, "flavors": ["Chocolate Chip", "Butterscotch", "Oreo-Nutella"]}  # Cookies product details
}

def rotating_effect(message, duration=2):  # Rotating effect function
    symbols = "|/-\\" # List of rotating symbols
    end_time = time.time() + duration # Calculate end time
    while time.time() < end_time:  # Loop until time expires
        for symbol in symbols:  # Loop through symbols
            sys.stdout.write(f"\r{message} {symbol}") # Print rotating symbol
            sys.stdout.flush()  # Flush buffer to screen
            time.sleep(0.2) # Wait before next symbol
    sys.stdout.write(f"\r{message}... Done! 🎉\n") # Print final message
    sys.stdout.flush() # Flush buffer again

def display_Menu_Items(): # Function to display menu
    rotating_effect("🔄 Initializing Vending Machine Menu") # Show initializing effect
    print("\n🌟Welcome to Bath Spa's Vending Mahine🌟!") # Print welcome message
    time.sleep(2) # Short pause
    print("Choose from the following items in our vending machine: ")  # Print menu prompt
    for code, item in products.items(): # Loop through products
        if item["stock"] > 0: # If item in stock
            print(f"[{code}] {item["name"]} : £{item["price"]:.2f} ({item["stock"]} available in stock)") # Print item details
            time.sleep(0.5)  # Short pause
                  
def Flavor_Selection(flavors): # Function for flavor selection
    rotating_effect("🚀 Loading your flavor options...") # Show rotating effect
    print("\nWhat's your preferred flavor? Take your pick!") # Print flavor prompt
    time.sleep(1) # Short pause
    for i, flavor in enumerate(flavors, 1):  # Loop through flavors
        print(f"[{i}] {flavor}")  # Print flavor options
        time.sleep(0.5) # Short pause
    while True: # Loop for valid input
        try:
            options = int(input("Choose a flavor by entering its number:")) # Get flavor choice
            if 1 <= options <= len(flavors):  # If valid choice
                return flavors[options - 1]   # Return selected flavor  
            else:
                print("Oops! That's not a valid choice. Please try again. 🙁") # Invalid choice message
                time.sleep(1)  # Short pause
        except ValueError:  # Handle invalid input
            print("Please enter a number from the list. ⚠️") # Invalid number message
            time.sleep(1)  # Short pause     

def Execute_Payment(price): # Function to handle payment
    correct_password = "12345"  # Correct card PIN
    max_attempts = 3 # Maximum attempts for PIN

    while True: # Loop for payment selection
        print("\nPayment Options: 1. Cash  2. Credit Card")  # Show payment options
        time.sleep(0.5) # Short pause
        payment_method = input("Choose your payment method by entering 1 or 2: ").strip()  # Get payment choice
        time.sleep(2) # Short pause

        if payment_method == "1": # If Cash selected
            while True: # Loop for cash input
                try:
                    money = float(input(f"Insert money £{price:.2f}: ")) # Get money input
                    if money < price: # If not enough cash
                        print(f"Not enough cash! Just £{price - money:.2f} more and it's all yours! 🎉") # If not enough cash
                        time.sleep(1) # Short pause
                    else: # If enough cash
                        return money - price  # Return change
                except ValueError:  # If invalid cash input
                    print("That's not quite right. Please enter a number to continue! 🔄") # Error message
                    time.sleep(1) # Short pause
        elif payment_method == "2": # If Credit Card selected
            print("\nPlease insert your card... 🚧") # Get card inserted
            time.sleep(4) # Short pause
            rotating_effect("🔄 Card detected! Validating card details... Please wait") # Show rotating effect 
            time.sleep(2) # Short pause
            attempts = 0 # Maximum attempts for PIN
            while attempts < max_attempts:  # If attempts are less than max
                password = input("Enter the credit card PIN: ").strip() # Ask for PIN input
                if password == correct_password: # If correct PIN
                    rotating_effect("🔓 Verifying PIN...") # Show verification effect
                    time.sleep(1)  # Short pause
                    rotating_effect(f"Processing the amount £{price:.2f}... 💳") # Display card processing message
                    print("Payment successful! ✅ Transaction approved!") # Payment success message
                    return 0 # No change
                else: # If incorrect PIN
                    attempts += 1  # Increment attempts
                    attempts_left = max_attempts - attempts  # Calculate remaining attempts
                    print(f"🛑 Access denied, try again! You have {attempts_left} attempts left.")  # Error message
                    time.sleep(1)  # Short pause

            if attempts == max_attempts:  # If maximum attempts reached
                print("Maximum login attempts reached. Your card is temporarily blocked. ❌")  # Max attempts message
                continue # Continue to payment selection

        else:  # If invalid input
            print("Invalid option! Please choose 1 for Cash or 2 for Credit Card.") # Invalid input message

def Dispensing_Animation(item_name):  # Animation for dispensing item
    print("\nDispensing your item... Please wait.")  # Dispensing message
    time.sleep(2)  # Short pause
    animation = [  # Animation frames
        "🟩⬜⬜⬜⬜⬜⬜⬜⬜", # Frame 1
        "🟩🟩⬜⬜⬜⬜⬜⬜⬜", # Frame 2
        "🟩🟩🟩⬜⬜⬜⬜⬜⬜", # Frame 3
        "🟩🟩🟩🟩⬜⬜⬜⬜⬜", # Frame 4
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜", # Frame 5
        "🟩🟩🟩🟩🟩🟩⬜⬜⬜", # Frame 6
        "🟩🟩🟩🟩🟩🟩🟩⬜⬜", # Frame 7
        "🟩🟩🟩🟩🟩🟩🟩🟩⬜", # Frame 8
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩"  # Frame 9
    ]
    for frame in animation:  # Loop through animation frames
        print(frame, end="\r") # Print current frame
        time.sleep(0.3) # Short pause
    print(f"🎉 Enjoy your {item_name}! Foodie🎉") # Final message 
    time.sleep(0.5)   # Short pause       

def Collect_Feedback(): # Function to collect feedback
    while True:  # Loop for valid feedback input
        try:
            rating = int(input("\nRate your satisfaction with the purchase process of this item (1-5): "))  # Get feedback
            time.sleep(1) # Short pause
            if 1 <= rating <= 5:  # If valid rating
                print(f"We appreciate your feedback! You rated this item {rating} out of 5. 🏷️") # Feedback message
                time.sleep(1) # Short pause
                return rating # Return rating
            else:
                print("To submit your feedback, kindly enter a number between 1 and 5.") # Invalid rating message
                time.sleep(1) # Short pause
        except ValueError: # Handle invalid input
            print("Rating should be between 1 and 5. Please re-enter your rating 🔄.") # Error message
            time.sleep(1) # Short pause

def Vending_Machine(): # Main vending machine function
    while True: # Loop for user interaction
        display_Menu_Items() # Show items in the menu
        code = input("\nYour choice awaits🥰! Enter the code or 'exit' to stop! 🚀: ").strip().upper()  # Get item code

        if code.lower() == "exit": # If user wants to exit
            print("\nEnjoy your goodies🍽️! Thank you for using the BSU vending machine! 🙌🎉")  # Exit message
            time.sleep(1)  # Short pause
            break  # Exit the loop

        if code not in products:  # If invalid item code
            print("⚠️ Code not recognized. Give it another shot.") # Invalid code message
            time.sleep(1)  # Short pause
            continue # Continue the loop

        item = products[code] # Get selected item details
        if item["stock"] <= 0: # If item is out of stock
            print("That item is no longer available. Please try another option 🎯.")  # Out of stock message
            time.sleep(1)  # Short pause
            continue # Continue the loop

        selected_flavor = None # Initialize selected flavor
        if item["flavors"]:  # If item has flavors
            selected_flavor = Flavor_Selection(item["flavors"])  # Get flavor selection

        change = Execute_Payment(item["price"])  # Process payment
        if change is None: # If payment failed
            continue # Continue to next iteration

        item["stock"] -= 1  # Reduce stock by 1

        Dispensing_Animation(item['name']) # Show dispensing animation
        print(f"\nYour change💸: £{change:.2f}" if change > 0 else "No change to return. Thank you!") # Show change message
        time.sleep(1) # Short pause

        rating = Collect_Feedback() # Collect user feedback

        while True: # Ask if user wants another item
            another = input("\nWould you like to choose another item? (yes/no): ").strip().lower() # Get user input
            time.sleep(1)  # Short pause
            if another == "yes": # If yes
                print("\nTaking you back to the menu... 🛒") # Message taking bact to menu
                time.sleep(2)  # Short pause
                break # Break the loop
            elif another == "no": # If no
                print("\nThank you for using Bath Spa's Vending Machine! 🙌😊 See you soon Foodie! 🚀")  # Exit message
                return # Exit the function
            else:  # Invalid input
                print("Invalid input. Please type 'yes' to choose another item or 'no' to exit. ⚠️") # Invalid input message


Vending_Machine() # Start the vending machine program
           








