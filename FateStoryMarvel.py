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

# Start the story
chapter_1()
