"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730647363"
locat: str = input("Pick a secret boat location between 1 and 4: ")
if int(locat) < 1: 
    print("Error! " + locat + " too low!")
    exit()
if int(locat) > 4: 
    print("Error! " + locat + " too high!")
    exit()
guess: str = input("Guess a number between 1 and 4: ")
hit: int = 0
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
RESULT1: str = BLUE_BOX
RESULT2: str = BLUE_BOX
RESULT3: str = BLUE_BOX
RESULT4: str = BLUE_BOX
if int(guess) < 1: 
    print("Error! " + str(guess) + " too low!")
    exit()
if int(guess) > 4: 
    print("Error! " + str(guess) + " too high!")
    exit()
if locat == guess:
    if int(guess) == 1:
        RESULT1 = RED_BOX
    if int(guess) == 2:
        RESULT2 = RED_BOX
    if int(guess) == 3:
        RESULT3 = RED_BOX
    if int(guess) == 4:
        RESULT4 = RED_BOX        
    print(str(RESULT1) + str(RESULT2) + str(RESULT3) + str(RESULT4))
    print("Correct! You hit the ship.")
else:
    if int(guess) == 1:
        RESULT1 = WHITE_BOX
    if int(guess) == 2:
        RESULT2 = WHITE_BOX
    if int(guess) == 3:
        RESULT3 = WHITE_BOX
    if int(guess) == 4:
        RESULT4 = WHITE_BOX
    print(str(RESULT1) + str(RESULT2) + str(RESULT3) + str(RESULT4))
    print("Incorrect! You missed the ship.")