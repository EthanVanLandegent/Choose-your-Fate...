# Programmer: Ethan VanLandegent
# Date: 3.18.24
# Program: Choose Your Fate Game

def main():
    print("Welcome to the Star Wars Adventure Game!")
    print("You find yourself in a galaxy far, far away...")

    choices = {
        '1': join_rebels,
        '2': serve_empire,
        '3': become_smuggler,
        '4': explore_tatooine,
        '5': become_bounty_hunter,
        '6': visit_jedi_temple,
        '7': quit_game
    }

    while True:
        print("\nWhat do you want to do?")
        print("1. Join the Rebel Alliance")
        print("2. Serve the Galactic Empire")
        print("3. Become a Smuggler")
        print("4. Explore Tatooine")
        print("5. Become a Bounty Hunter")
        print("6. Visit the Jedi Temple")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice in choices:
            choices[choice]()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def join_rebels():
    print("\nYou have chosen to join the Rebel Alliance.")
    print("Your mission is to help overthrow the Galactic Empire.")
    handle_rebel_choices()

def serve_empire():
    print("\nYou have chosen to serve the Galactic Empire.")
    print("Your loyalty lies with Emperor Palpatine and Darth Vader.")
    handle_empire_choices()

def become_smuggler():
    print("\nYou have chosen to become a Smuggler.")
    print("You will navigate the galaxy's underworld, avoiding both the Empire and the Rebels.")
    handle_smuggler_choices()

def explore_tatooine():
    print("\nYou have chosen to explore Tatooine.")
    print("The desert planet is full of adventures and dangers.")
    handle_tatooine_choices()

def become_bounty_hunter():
    print("\nYou have chosen to become a Bounty Hunter.")
    print("You will hunt down targets for credits and reputation.")
    handle_bounty_hunter_choices()

def visit_jedi_temple():
    print("\nYou have chosen to visit the Jedi Temple.")
    print("You will explore the ancient temple and learn about the Force.")
    handle_jedi_temple_choices()

def handle_rebel_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Infiltrate an Imperial base")
        print("2. Rescue prisoners from a Star Destroyer")
        print("3. Plan an attack on the Death Star")
        print("4. Gather allies on Mon Cala")
        print("5. Establish a Rebel outpost on Hoth")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nYou successfully infiltrate the Imperial base and gather valuable intel.")
        elif choice == '2':
            print("\nYou rescue prisoners from the Star Destroyer and gain allies for the Rebellion.")
        elif choice == '3':
            print("\nYou help plan an attack on the Death Star and contribute to its destruction.")
        elif choice == '4':
            print("\nYou travel to Mon Cala and convince its inhabitants to join the Rebel cause.")
        elif choice == '5':
            print("\nYou establish a Rebel outpost on Hoth, preparing for future battles.")
        elif choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_empire_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Hunt down Rebel spies")
        print("2. Secure a rebel-controlled planet")
        print("3. Assist in building the Death Star")
        print("4. Crush a Rebel uprising on Lothal")
        print("5. Conquer a neutral planet for the Empire")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nYou track down Rebel spies and eliminate them, earning praise from Darth Vader.")
        elif choice == '2':
            print("\nYou successfully secure a rebel-controlled planet, crushing the Rebellion's hopes.")
        elif choice == '3':
            print("\nYou play a crucial role in the construction of the Death Star, the Empire's ultimate weapon.")
        elif choice == '4':
            print("\nYou lead Imperial forces to crush a Rebel uprising on Lothal, restoring order.")
        elif choice == '5':
            print("\nYou conquer a neutral planet for the Empire, expanding its territories.")
        elif choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_smuggler_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Smuggle contraband past Imperial blockades")
        print("2. Make a deal with Jabba the Hutt")
        print("3. Pull off a heist on an Imperial cargo ship")
        print("4. Join a smuggling ring on Corellia")
        print("5. Explore the black market on Coruscant")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nYou successfully smuggle contraband past Imperial blockades, earning hefty profits.")
        elif choice == '2':
            print("\nYou strike a deal with Jabba the Hutt, gaining valuable connections in the criminal underworld.")
        elif choice == '3':
            print("\nYou pull off a daring heist on an Imperial cargo ship, securing valuable goods.")
        elif choice == '4':
            print("\nYou join a smuggling ring on Corellia, becoming a prominent figure in the underworld.")
        elif choice == '5':
            print("\nYou explore the black market on Coruscant, finding rare and valuable items.")
        elif choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_tatooine_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Visit Mos Eisley Cantina")
        print("2. Race in a podrace")
        print("3. Negotiate with Jawas for droids")
        print("4. Hunt for treasure in the Jundland Wastes")
        print("5. Visit the Lars Homestead")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nYou visit the famous Mos Eisley Cantina and meet interesting characters.")
        elif choice == '2':
            print("\nYou participate in a thrilling podrace, dodging obstacles and rival racers.")
        elif choice == '3':
            print("\nYou negotiate with Jawas and acquire useful droids for your adventures.")
        elif choice == '4':
            print("\nYou embark on a treasure hunt in the dangerous Jundland Wastes, facing Tusken Raiders.")
        elif choice == '5':
            print("\nYou visit the Lars Homestead and learn about the Skywalker family.")
        elif choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_bounty_hunter_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Hunt a target for the Hutt Cartel")
        print("2. Capture a high-value target for the Empire")
        print("3. Track down a notorious smuggler for the Rebels")
        print("4. Join a bounty hunter guild on Nar Shaddaa")
        print("5. Visit the Pit of Carkoon")
        print("6. Return to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nYou successfully hunt a target for the Hutt Cartel, earning a handsome reward.")
        elif choice == '2':
            print("\nYou capture a high-value target for the Empire, gaining favor with Imperial authorities.")
        elif choice == '3':
            print("\nYou track down a notorious smuggler for the Rebels, becoming a thorn in the Empire's side.")
        elif choice == '4':
            print("\nYou join a bounty hunter guild on Nar Shaddaa, honing your skills alongside fellow hunters.")
        elif choice == '5':
            print("\nYou visit the Pit of Carkoon, where you witness the demise of Jabba the Hutt.")
        elif choice == '6':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def handle_jedi_temple_choices():
    while True:
        print("\nWhat will you do?")
        print("1. Meditate in the Jedi Archives")
        print("2. Train with a Jedi Master")
        print("3. Investigate the Sith holocrons")
        print("4. Search for surviving Jedi artifacts")
        print("5. Return to main menu")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nYou meditate in the Jedi Archives, gaining insights into the history of the Jedi Order.")
        elif choice == '2':
            print("\nYou train with a Jedi Master, honing your connection to the Force.")
        elif choice == '3':
            print("\nYou investigate the Sith holocrons, learning about the dark side of the Force.")
        elif choice == '4':
            print("\nYou search for surviving Jedi artifacts, preserving the legacy of the Jedi.")
        elif choice == '5':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def quit_game():
    print("May the Force be with you! Goodbye.")
    exit()

if __name__ == "__main__":
    main()