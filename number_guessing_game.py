# Import random for generating random number between 1 & 100
import random

# Generates the random number to guess against
random_number = random.randint(1, 100)

# Variable to keep the game running until the game no longer needs to be running
running = True

# Keeping track with the tries variable
tries = 0

lower_number = 0
higher_number = 0

# While loop so the user is prompted for input if they input the wrong information the first time. 
while running == True:
    try:
        number_range_lower = int(input("Please input the lower number in the range you want to guess from: "))
        number_range_upper = int(input("Please input the upper number in the range you want to guess from: "))
    except:
        print("That is not a valid number. Please try again with a number like '12' and not a word.")

    try:        
        # User input for the guess.
        guess = int(input("Guess a number between 1 & 100: "))
        
        
        # If statement to check if the number is below the the correct guess and then adds one number to tries variable
        if guess < random_number:
            tries += 1
            print(f"Sorry! {guess} is lower than the correct guess! Try again!")
        
        # If statement to check if the number is above the the correct guess and then adds one number to tries variable
        elif guess > random_number:
            tries += 1
            print(f"Sorry! {guess} is higher than the correct guess! Try again!")
            
        # If statement to check if the number is correct and then tells the lucky winner they won in x amount of tries! 
        elif guess == random_number:
            tries += 1
            print(f"WOW! You got it! It only took {tries} times to guess the correct number!")
            exit
        
    # Error handling for silly duffas that put the wrong info into the console. 
    except ValueError:
        print("That is not a valid number. Please try again with a number like '12' and not a word.")

