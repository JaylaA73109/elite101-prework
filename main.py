import random

print("Welcome to the Elite101 Chatbot!")
name = input("What is your name?")
age = input("What is your age?")
assist = input("Hello " + name + ", how can I assist you?\n *Type menu to see the options") 
def display_menu():
    print("\n**Menu**")
    
    print("1.Browse Products")
    print("2.Check Order Status")
    print("3.Return or exchange an item")
    print("4.Deals and Promotions")
    print("5.Store Information")
    print("6.Customer Support")
    print("7.Account Help")
    print("8.Exit")
display_menu()
back = "Return to menu"


user_response = input(f'Enter a number between 1-8')

#Browse products
items = ["Galumphous seal $60","Bartholomew Bear $23", "Amuseables peach $28", "Peanut penguin $20", "Timmy turtle $50", "Bashful bunny $50"]
codes = ["3546","8753","0761","1759","0543","7826"]
#The codes above are assigned in order to the list of items. ex. the code of peanut pengiun is 1759
if user_response == "1":
    def display_items():
        print(items)
    display_items()

#Exit
if user_response == "8":
    print("Okay then, Goodbye!")

#Exchange or return
if user_response == "3":
    action = input("Would you like to return or exchange an item? (Type 'return' or 'exchange'): ")
    if action.lower() == "exchange":
        print("You are now exchanging an item")
item_returning = input("Which item are you exchanging? ") # Check the input item
#returning galumphous seal for another item
if item_returning.lower() == 'galumphous seal' :
    print("You have selected the Galumphous seal")
    GS_code = input("Please enter item code for validity: ") # Check the code, converting the input to an integer for comparison
    if GS_code == '3546' :  # Compare with a string or use 'if int(GS_code) == 3546'
        print("Okay what item would you like to obtain?")
        new_item = input("Please enter item here: ") # Compare the lowercased input string with the lowercased target string
        if new_item.lower() == 'bartholomew bear' :
            print("Your new item should be in your cart and the amount refunded to your account is $37")
        if new_item.lower() == 'amuseables peach' :
            print("Your new item should be in your cart and the amount refunded to your account is $32")
        if new_item.lower() == 'peanut penguin' :
            print("Your new item should be in your cart and the amount refunded to your account is $40")
        if new_item.lower() == 'timmy turtle' :
            print("Your new item should be in your cart and the amount refunded to your account is $10")
        if new_item.lower() == 'bashful bunny' : # Added parentheses and quotes
            print("Your new item should be in your cart and the amount refunded to your account is $10")
#returning bartholomew bear for another item
if item_returning.lower() == "bartholomew bear":
    print("You have selected the bartholomew bear")
    BB_code = input("Please enter item code for validity: ")
    if BB_code == '8753':
        print("Okay what item would you like to obtain?")
        new_item = input("Please enter item here: ")
        if new_item.lower() == "galumphous seal":
            print("Your new item should be in your cart and the amount charged to your account is $37")       
        if new_item.lower() == 'amuseables peach' :
            print("Your new item should be in your cart and the amount charged to your account is $5")
        if new_item.lower() == 'peanut penguin' :
            print("Your new item should be in your cart and the amount refunded to your account is $3")
        if new_item.lower() == 'timmy turtle' :
            print("Your new item should be in your cart and the amount charged to your account is $27")
        if new_item.lower() == 'bashful bunny' : # Added parentheses and quotes
            print("Your new item should be in your cart and the amount charged to your account is $27")
    
#returning amuseables peach for another item
if item_returning.lower() == "amuseables peach":
    print("You have selected the amuseables peach")
    AP_code = input("Please enter item code for validity: ")
    if AP_code == '0761':
        print("Okay what item would you like to obtain?")
        new_item = input("Please enter item here: ")
        if new_item.lower() == "galumphous seal":
            print("Your new item should be in your cart and the amount charged to your account is $32")       
        if new_item.lower() == 'bartholomew bear' :
            print("Your new item should be in your cart and the amount refunded to your account is $5")
        if new_item.lower() == 'peanut penguin' :
            print("Your new item should be in your cart and the amount refunded to your account is $8")
        if new_item.lower() == 'timmy turtle' :
            print("Your new item should be in your cart and the amount charged to your account is $22")
        if new_item.lower() == 'bashful bunny' : # Added parentheses and quotes
            print("Your new item should be in your cart and the amount charged to your account is $22")

#returning peanut pengiun for another item
if item_returning.lower() == "peanut pengiun":
    print("You have selected the peanut pengiun")
    PP_code = input("Please enter item code for validity: ")
    if PP_code == '1759':
        print("Okay what item would you like to obtain?")
        new_item = input("Please enter item here: ")
        if new_item.lower() == "galumphous seal":
            print("Your new item should be in your cart and the amount charged to your account is $40")       
        if new_item.lower() == 'bartholomew bear' :
            print("Your new item should be in your cart and the amount charged to your account is $3")
        if new_item.lower() == 'timmy turtle' : # Added parentheses and quotes
            print("Your new item should be in your cart and the amount charged to your account is $50")
        if new_item.lower() == 'bashful bunny' :
            print("Your new item should be in your cart and the amount charged to your account is $50 ")


