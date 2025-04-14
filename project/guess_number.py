# Guess Number Code using loop and conditional statements

import random

random_number = random.randint(1,100)

while True:
    user_guess = (input("Guess a number between 1 and 100 or quit(Q):"))
    if user_guess == "Q":
        break
    user_guess = int(user_guess)
    
    if user_guess == random_number:
        print("Congratulations! You guessed the number correctly!")
        break
    
    elif user_guess < random_number:
        print("Your guess is too low. Try again!")
        
    else:
        print("Your guess is too high. Try again!")
        
print("----Game Over----")
