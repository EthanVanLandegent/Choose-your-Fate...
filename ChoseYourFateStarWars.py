# Programmer: Ethan VanLandegent
# Date: 3.18.24
# Program: Choose Your Fate Game
def main():
    print("Welcome to the Star Wars Adventure Game!")
    print("You find yourself in a galaxy far, far away...")

    while True:
        print("\nWhat do you want to do?")
        print("1. Join the Rebel Alliance")
        print("2. Serve the Galactic Empire")
        print("3. Become a Smuggler")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            join_rebels()
        elif choice == '2':
            serve_empire()
        elif choice == '3':
            become_smuggler()
        elif choice == '4':
            print("May the Force be with you! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def join_rebels():
    print("\nYou have chosen to join the Rebel Alliance.")
    print("Your mission is to help overthrow the Galactic Empire.")

    while True:
        print("\nWhat will you do?")
        print("1. Infiltrate an Imperial base")
        print("2. Rescue prisoners from a Star Destroyer")
        print("3. Plan an attack on the Death Star")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nYou successfully infiltrate the Imperial base and gather valuable intel.")
        elif choice == '2':
            print("\nYou rescue prisoners from the Star Destroyer and gain allies for the Rebellion.")
        elif choice == '3':
            print("\nYou help plan an attack on the Death Star and contribute to its destruction.")
        elif choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def serve_empire():
    print("\nYou have chosen to serve the Galactic Empire.")
    print("Your loyalty lies with Emperor Palpatine and Darth Vader.")

    while True:
        print("\nWhat will you do?")
        print("1. Hunt down Rebel spies")
        print("2. Secure a rebel-controlled planet")
        print("3. Assist in building the Death Star")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nYou track down Rebel spies and eliminate them, earning praise from Darth Vader.")
        elif choice == '2':
            print("\nYou successfully secure a rebel-controlled planet, crushing the Rebellion's hopes.")
        elif choice == '3':
            print("\nYou play a crucial role in the construction of the Death Star, the Empire's ultimate weapon.")
        elif choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def become_smuggler():
    print("\nYou have chosen to become a Smuggler.")
    print("You will navigate the galaxy's underworld, avoiding both the Empire and the Rebels.")

    while True:
        print("\nWhat will you do?")
        print("1. Smuggle contraband past Imperial blockades")
        print("2. Make a deal with Jabba the Hutt")
        print("3. Pull off a heist on an Imperial cargo ship")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nYou successfully smuggle contraband past Imperial blockades, earning hefty profits.")
        elif choice == '2':
            print("\nYou strike a deal with Jabba the Hutt, gaining valuable connections in the criminal underworld.")
        elif choice == '3':
            print("\nYou pull off a daring heist on an Imperial cargo ship, securing valuable goods.")
        elif choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
