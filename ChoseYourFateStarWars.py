# Programmer: Ethan VanLandegent
# Date: 3.18.24
# Program: Marvel fate story


def star_wars_game():
    print("Welcome to the Star Wars Adventure Game!")
    print("You find yourself in a galaxy far, far away...")
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
                print(
                    "\nYou strike a deal with Jabba the Hutt, gaining valuable connections in the criminal underworld.")
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

def marvel_game():
    print("Welcome to the Marvel Superhero Adventure!")
    print("In a world filled with chaos and danger, heroes rise to protect the innocent.")
    print("You find yourself in a bustling city, where supervillains threaten to destroy everything.")
    print("As the city's last hope, your journey begins now.")
    print("Are you ready to embrace your destiny and become a legendary superhero?\n")
    def intro():
        print("\nWelcome to the Marvel Superhero Adventure!")
        print("In a world filled with chaos and danger, heroes rise to protect the innocent.")
        print("You find yourself in a bustling city, where supervillains threaten to destroy everything.")
        print("As the city's last hope, your journey begins now.")
        print("Are you ready to embrace your destiny and become a legendary superhero?\n\n")

    def chapter_1():
        print("Chapter 1: The Superhero's Call")
        print("You find yourself in a bustling city, where chaos reigns as supervillains wreak havoc.")
        print("A mysterious figure approaches you, offering you a chance to become a superhero and save the city.")
        print("What will you do?")

        while True:
            choice = input("Do you accept the offer (1) or decline and walk away (2)?: ")
            if choice == '1':
                print("\nYou accept the offer and embrace your destiny as a superhero!")
                chapter_2a()
                break
            elif choice == '2':
                print("\nYou decline the offer, but as you walk away, you realize the city needs your help.")
                chapter_2b()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_2a():
        print("\nChapter 2a: The Training")
        print(
            "You are taken to a secret training facility where experienced heroes teach you the ways of combat and heroism.")
        print("After rigorous training, you are ready to face the challenges ahead.")
        print("What will you do?")

        while True:
            choice = input("Do you want to test your skills in the city (1) or continue training (2)?: ")
            if choice == '1':
                print("\nYou head into the city to put your training to the test and confront the villains.")
                chapter_3a()
                break
            elif choice == '2':
                print("\nYou decide to continue training, honing your abilities to become an even stronger hero.")
                chapter_3b()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_2b():
        print("\nChapter 2b: The Change of Heart")
        print("As you walk away, you witness innocent civilians in danger, pleading for help.")
        print("You realize that you can't turn your back on those in need.")
        print("What will you do?")

        while True:
            choice = input(
                "Do you want to go back and accept the offer (1) or help the civilians without powers (2)?: ")
            if choice == '1':
                print("\nYou go back and accept the offer, determined to become a hero and save the city.")
                chapter_2a()
                break
            elif choice == '2':
                print(
                    "\nYou help the civilians using your own abilities and resources, proving that heroes come in many forms.")
                # End of the story
                print("\nCongratulations! You've shown that anyone can be a hero, powers or not.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_3a():
        print("\nChapter 3a: The Battle")
        print("You find yourself in the midst of a fierce battle between heroes and villains.")
        print("The fate of the city hangs in the balance as you face off against powerful foes.")
        print("What will you do?")

        while True:
            choice = input("Do you want to join forces with other heroes (1) or face the villains alone (2)?: ")
            if choice == '1':
                print("\nYou join forces with other heroes, combining your strengths to defeat the villains.")
                # End of the story
                print("\nCongratulations! With teamwork, you save the city and become a true hero.")
                break
            elif choice == '2':
                print("\nYou face the villains alone, using your skills and determination to protect the city.")
                # End of the story
                print("\nCongratulations! Your bravery and resilience save the day, making you a legendary hero.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_3b():
        print("\nChapter 3b: The Solo Mission")
        print("You embark on a solo mission to apprehend a notorious supervillain wreaking havoc in the city.")
        print("The villain's lair is heavily guarded, and danger lurks around every corner.")
        print("What will you do?")

        while True:
            choice = input("Do you want to confront the villain head-on (1) or find a stealthy approach (2)?: ")
            if choice == '1':
                print("\nYou confront the villain head-on, engaging in an epic showdown of power and wit.")
                # End of the story
                print(
                    "\nCongratulations! You defeat the villain and save the city single-handedly, becoming a legendary hero.")
                break
            elif choice == '2':
                print("\nYou find a stealthy approach, sneaking past the guards and surprising the villain.")
                # End of the story
                print(
                    "\nCongratulations! Your cunning and strategy lead to victory, earning you the title of a masterful hero.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_4a():
        print("\nChapter 4a: The Alliance")
        print("You realize that the villain you defeated was just a pawn in a larger scheme.")
        print("To stop the mastermind behind the chaos, you must form an alliance with other heroes.")
        print("What will you do?")

        while True:
            choice = input("Do you want to seek out other heroes for help (1) or confront the mastermind alone (2)?: ")
            if choice == '1':
                print("\nYou seek out other heroes, forming a powerful alliance to take down the mastermind.")
                # End of the story
                print(
                    "\nCongratulations! With the combined strength of heroes, you defeat the mastermind and save the world.")
                break
            elif choice == '2':
                print("\nYou confront the mastermind alone, facing your greatest challenge yet.")
                # End of the story
                print("\nCongratulations! Your bravery and determination lead to victory, making you a legendary hero.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_4b():
        print("\nChapter 4b: The Redemption")
        print(
            "You encounter a former villain seeking redemption, torn between their past and a desire for a new beginning.")
        print("What will you do?")

        while True:
            choice = input("Do you want to offer them a chance for redemption (1) or confront them as a threat (2)?: ")
            if choice == '1':
                print("\nYou offer them a chance for redemption, believing in the power of second chances.")
                # End of the story
                print("\nCongratulations! Your compassion leads to their redemption, and they become a valuable ally.")
                break
            elif choice == '2':
                print("\nYou confront them as a threat, fearing their past actions may endanger others.")
                # End of the story
                print("\nCongratulations! Your vigilance protects the innocent, ensuring peace in the city.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_5():
        print("\nChapter 5: The Final Showdown")
        print("The city faces its greatest threat yet as a powerful supervillain threatens to unleash chaos.")
        print("As a seasoned hero, you are the city's last hope for salvation.")
        print("What will you do?")

        while True:
            choice = input(
                "Do you want to confront the villain head-on (1) or devise a strategy with other heroes (2)?: ")
            if choice == '1':
                print("\nYou confront the villain head-on, ready to face the ultimate challenge.")
                # End of the story
                print(
                    "\nCongratulations! Your courage and determination save the city from destruction, making you a true legend.")
                break
            elif choice == '2':
                print("\nYou devise a strategy with other heroes, combining your strengths to defeat the villain.")
                # End of the story
                print(
                    "\nCongratulations! With teamwork and perseverance, you emerge victorious, ensuring peace and justice.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def chapter_6():
        print("\nChapter 6: The Legacy")
        print("Your heroic deeds have inspired others, and the city honors you as its greatest protector.")
        print(
            "As you look back on your journey, you realize that being a hero is more than just having powers—it's about making a difference.")
        print("What will you do now?")

        while True:
            choice = input(
                "Do you want to continue protecting the city (1) or pass the mantle to a new generation (2)?: ")
            if choice == '1':
                print("\nYou continue protecting the city, ensuring its safety for generations to come.")
                # End of the story
                print("\nCongratulations! Your dedication and selflessness make you a true hero, beloved by all.")
                break
            elif choice == '2':
                print("\nYou pass the mantle to a new generation, entrusting them with the responsibility of heroism.")
                # End of the story
                print("\nCongratulations! Your legacy lives on as a symbol of hope and inspiration for future heroes.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    # Start the story
    intro()
    chapter_1()

def main():
    print("Welcome to the Adventure Game Selector!")
    print("Choose which adventure you want to embark on:")
    print("1. Star Wars Adventure")
    print("2. Marvel Superhero Adventure")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        star_wars_game()
    elif choice == '2':
        marvel_game()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()




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

