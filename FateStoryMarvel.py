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
    print("You are taken to a secret training facility where experienced heroes teach you the ways of combat and heroism.")
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
        choice = input("Do you want to go back and accept the offer (1) or help the civilians without powers (2)?: ")
        if choice == '1':
            print("\nYou go back and accept the offer, determined to become a hero and save the city.")
            chapter_2a()
            break
        elif choice == '2':
            print("\nYou help the civilians using your own abilities and resources, proving that heroes come in many forms.")
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
            print("\nCongratulations! You defeat the villain and save the city single-handedly, becoming a legendary hero.")
            break
        elif choice == '2':
            print("\nYou find a stealthy approach, sneaking past the guards and surprising the villain.")
            # End of the story
            print("\nCongratulations! Your cunning and strategy lead to victory, earning you the title of a masterful hero.")
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
            print("\nCongratulations! With the combined strength of heroes, you defeat the mastermind and save the world.")
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
    print("You encounter a former villain seeking redemption, torn between their past and a desire for a new beginning.")
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
        choice = input("Do you want to confront the villain head-on (1) or devise a strategy with other heroes (2)?: ")
        if choice == '1':
            print("\nYou confront the villain head-on, ready to face the ultimate challenge.")
            # End of the story
            print("\nCongratulations! Your courage and determination save the city from destruction, making you a true legend.")
            break
        elif choice == '2':
            print("\nYou devise a strategy with other heroes, combining your strengths to defeat the villain.")
            # End of the story
            print("\nCongratulations! With teamwork and perseverance, you emerge victorious, ensuring peace and justice.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def chapter_6():
    print("\nChapter 6: The Legacy")
    print("Your heroic deeds have inspired others, and the city honors you as its greatest protector.")
    print("As you look back on your journey, you realize that being a hero is more than just having powers—it's about making a difference.")
    print("What will you do now?")

    while True:
        choice = input("Do you want to continue protecting the city (1) or pass the mantle to a new generation (2)?: ")
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
