import random

compliments = [
    "You have a beautiful smile.",
    "Your hair looks amazing.",
    "You have a great sense of humor.",
    "You're incredibly kind.",
    "You have a contagious laugh.",
    "You're a great listener.",
    "You always make people feel welcome.",
    "You have a heart of gold.",
    "You're an amazing friend.",
    "You have a unique and special talent."
]

print("Random Compliment Generator\n")

while True:
    input("Press Enter to get a compliment, or 'q' to quit: ")
    compliment = random.choice(compliments)
    print("\n" + compliment + "\n")
    
    if input("Press 'y' to get another compliment, or any other key to quit: ").lower() != "y":
        break
        
print("Thanks for playing!")
