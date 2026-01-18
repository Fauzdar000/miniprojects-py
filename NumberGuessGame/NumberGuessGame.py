
# Number Guessing Game 

import random

secretNumber = random.randint(1 , 10) # generates a random number

while True: # loops runs until its true
    guess = int(input("guess a number between 1 and 10 :")) # converts user input to number

    if guess == secretNumber:
        print("🎉 Correct! You guessed it.")
        break # exists loop when guess is correct
    # elif guess < secretNumber:
    #     print("Too low ! try again")
    
    # else:
    #     print("Too high ! try again")
    
    else: 
        print(" Try again !")