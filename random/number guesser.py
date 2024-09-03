import random

number = int(input("Guess a number between 0 to 5! "))

# Generate a random number between 0 and 5
right = random.randint(0, 5)

# Compare the user's guess with the random number
if number == right:
    print("You guessed correct!")
else:
    print(f"You guessed wrong! The correct number was {right}.")