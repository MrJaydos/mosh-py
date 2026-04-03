# Import to support the random.randint used for the dice roll
import random

# While loop to keep the dice rolling running unless the user says "n"
while True:
    
    # User input in the console. Also converts to a upper case to allow for less options in the if statement
    answer = input("Would you like to roll the dice? (Y, N): ").upper()
    
    # Actions if the user presses "Y" - Rolls two random integers and then prints them to the console.
    if answer == "Y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"The dice says: {die1} and {die2}")
    
    # Actions if the user presses "N" - Thanks them for playing and then breaks the while loop and exits the program. 
    elif answer == "N":
        print("Thanks for playing")
        break
    
    # Handles any other characters being added when they aren't meant to be 
    else:
        print("Invalid response")    