# Import random for generating random number between 1 & 100
import random

# While loop so the user is prompted for input if they input the wrong infomation the first time. 
while True:
    try:
        # User input for the guess.
        guess = int(input("Guess a number between 1 & 100: "))
        
        # if the line above succeeds, the code will continue
        break
    except ValueError:
        print("That is not a valid number. Please try again with a number like '12' and not a word.")

