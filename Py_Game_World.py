import random

def num_guess():
    number = random.randint(1, 10)

    guess = int(input("Guess the number (between 1 and 10): "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, the correct number was", number)

def RPS():
    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)

    user_choice = input("Choose rock, paper, or scissors: ")

    print("Computer chose", computer_choice)

    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")


def mad_libs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"The {adjective} {noun} {verb} {adverb} around the corner."

    print(story)

import random

def story_game():
    names = input("Enter Some Name seperated by commas:").split(",")
    items = input("Enter Some Items seperated by commas:").split(",")
    places = input("Enter Some Places seperated by commas:").split(",")
    actions = input("Enter Some Actions seperated by commas:").split(",")
    
    name1 = random.choice(names)
    name2 = random.choice(names)
    item = random.choice(items)
    place = random.choice(places)
    action = random.choice(actions)
    
    story = f"Once upon a time, {name1} went to the {place} and {action} {name2}'s {item}. But when {name1} got home, they realized that they were missing one of their {item}! They searched everywhere, but the missing {item} was nowhere to be found. They even went back to the {place} to look for it, but it was gone.\n\nThe end."
    
    print(story)
    

print("\t\tHEY! WELCOME TO THE PYTHON GAME WORLD!\n")
print("Which Game you wanna play:\n")
print("Number guessing Game!\t\tpress N")
print("Rock Paper Scissor!\t\tpress R")
print("mad libs!\t\t\tpress M")
print("Story Game!\t\t\tpress S")

choice = str(input("Enter Your Choice:"))

if choice.lower() == 'n':
    num_guess()
elif choice.lower() == 'r':
    RPS()
elif choice.lower() == 'm':
    mad_libs()
elif choice.lower() == 's':
    story_game()
else:
    print("Invalid choice!")
    
    
