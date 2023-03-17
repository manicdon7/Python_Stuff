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
    
    story1 = f"Once upon a time, {name1} went to the {place} and {action} {name2}'s {item}. But when {name1} got home, they realized that they were missing one of their {item}! They searched everywhere, but the missing {item} was nowhere to be found. They even went back to the {place} to look for it, but it was gone.\n\nThe end."
    story2 = f"Rumors are swirling around town that the wealthy businessman, {name1}, has been spotted out and about with a much younger woman. Some say she's a model, while others claim she's his personal assistant. Witnesses have reported seeing the two of them {action} at fancy restaurants and attending high-end events together.  Some even claim they've seen them holding hands and whispering sweet nothings to each other.{name1}, the businessman's wife, is said to be devastated by the rumors. She's been seen looking pale and withdrawn in public, and some have even reported that she's been seen {action} alone at night. No one knows for sure what's really going on between{name1} and the mystery woman, but one thing is certain - this scandal is the talk of the town, and everyone is eagerly waiting to see how it will all play out."
    story3 = f"There's a juicy rumor going around that the popular actress, Rachel Stevens, is set to star in a new movie alongside her ex-boyfriend, the handsome and talented actor, {name1}. According to sources close to the pair, Rachel and {name1} had a messy breakup several years ago, and their on-set reunion is sure to be tense. Some even say that there's still unresolved feelings between the two, and that the movie's steamy love scenes might reignite their old flame. But others claim that the two are true professionals, and that they'll be able to put their past behind them and deliver an incredible performance on screen. Either way, this news has everyone in Hollywood buzzing, and fans are eagerly anticipating the release of the movie to see how it all plays out."
    story4 = f"There's a hilarious rumor going around town that the new manager at the local supermarket has a secret obsession with bananas. According to sources, the manager has been seen sneaking into the store's produce section late at night and whispering sweet nothings to the bunches of bananas. Some even claim that the manager has taken to carrying a banana around with them at all times, and can often be seen absent-mindedly stroking it during meetings and conversations. While some employees find the manager's behavior odd, others are simply amused by it, and have taken to leaving silly notes and jokes about bananas around the store for the manager to find. Either way, this quirky rumor has everyone talking, and the supermarket has become the talk of the town - all thanks to a little harmless banana obsession."
    story5 = f"Rumor has it that socialite and fashionista, {name1}, was spotted at a high-end {place} wearing mismatched{item}. Apparently, {name1} was in such a rush to make her reservation that she accidentally grabbed two different {item} from her closet without {action} it. But rather than let the fashion faux pas ruin her evening, {name1} reportedly owned the look and told everyone who asked that it was her latest fashion statement. Who knows, maybe mismatched {name1} will become the next big trend thanks to {name1}!"
    stories = [story1,story2,story3,story4,story5]
    
    story = random.choices(stories)
    
    
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
    
  
