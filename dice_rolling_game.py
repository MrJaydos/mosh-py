
import random


while True:
    answer = input("Would you like to roll the dice? (Y, N): ").upper()
    if answer == "Y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"The dice says: {die1} and {die2}")
        
    elif answer == "N":
        print("Thanks for playing")
        break
    else:
        print("Invalid response")    