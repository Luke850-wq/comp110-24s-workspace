"""Number Gussing game."""""

from random import randint
SECRET: int = randint(1,10)
correct: bool = False
while correct == False:
    guess: int = int(input("Guess a number: "))


    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number")
        correct = True
    else: 
        if guess > SECRET:
        print("Too high! Try again!")
     
    else:
        if guess < SECRET:
        print("Too low! Try again!")
    

