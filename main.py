def welcome_user():
    print("Hello! Welcome to the Super Grocery Store Assistant.")
    print("I am here to assist you.")

def collect_user_info():
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f"Hello {name}, nice to meet you! You are {age} years old.")
    return name, age

def help_user():
    print("\nHow can I assist you today?")
    print("1. Check product availability")
    print("2. Update me on sales")
    print("3. View item details")
    print("4. Get products recommendation")
    print("5. Exit")

def process_user_choice():
    while True:
        choice = input("\nPlease select an option (1-5): ")

        if choice == "1":
            print("You chose to check product availability. (Please Click Here to be taken to the following tab.)")
        elif choice == "2":
            print("You chose to Update me on sales. (Feel free to check our Sales option down below!)")
        elif choice == "3":
            print("You chose to View item details. (Please feel free to search up the item to get any specific information.)")
        elif choice == "4":
            print("You chose to Get products recommendation. (Please Click Here to be taken to the following tab to help you out, or feel free to ask a woker!)")
        elif choice == "5":
            print("Goodbye! Thank you for using the Super Grocery Store Assistant. Have a great day!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

def main():
    welcome_user()
    collect_user_info()
    help_user()
    process_user_choice()

if __name__ == "__main__":
    main()
