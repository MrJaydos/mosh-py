# Import to support the random.randint used for the dice roll
import random

# Declared number of dice rolled for ongoing total
number_of_dice_rolled = 0

# While loop to keep the dice rolling running unless the user says "n"
while True:
    
    # User input in the console. Also converts to a upper case to allow for less options in the if statement
    answer = input("Would you like to roll the dice? (Y, N): ").upper()
    
    # Try loop to avoid errors from users inputting the wrong data type.
    try:
        how_many = int(input("How many dice would you like to roll? "))
    except ValueError:
        print("That is not a valid integer")
    
    # Actions if the user presses "Y" - Rolls user defined amount of random integers and then prints them to the console.
    if answer == "Y":
        for i in range(how_many) :
            random_num = random.randint(1,6)
            print(f"The dice says {random_num}")
            # Increase number dice rolls based on how many times the for loop runs through
            number_of_dice_rolled += 1
            
        print(f"The dice have been rolled {number_of_dice_rolled} times! WOW!")
    
    # Actions if the user presses "N" - Thanks them for playing and then breaks the while loop and exits the program. 
    elif answer == "N":
        print("Thanks for playing")
        break
    
    # Handles any other characters being added when they aren't meant to be 
    else:
        print("Invalid response")    