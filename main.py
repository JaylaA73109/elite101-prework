print("Welcome to the Elite101 Chatbot!")
name = input("What is your name?")
age = input("What is your age?")
assist = input("Hello " + name + ", how can I assist you?\n *Type menu to see the options") 
def display_menu():
    print("\n**Menu**")
    print("1.Browse Products")
    print("2.Check Order Status")
    print("3.Deals and Promotions")
    print("4.Store Information")
    print("5.Customer Support")
    print("6.Account Help")
    print("7.Exit")
display_menu()
user_response = input(f'Enter a number between 1-7')

if user_response == "7":
    print("Okay then, Goodbye!")


