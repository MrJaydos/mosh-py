# Import random for generating random number between 1 & 100
import random

# Generates the random number to guess against
random_number = random.randint(1, 100)

# Variable to keep the game running until the game no longer needs to be running
running = True


# While loop so the user is prompted for input if they input the wrong infomation the first time. 
while running == True:
    try:
        # User input for the guess.
        guess = int(input("Guess a number between 1 & 100: "))




    except ValueError:
        print("That is not a valid number. Please try again with a number like '12' and not a word.")

