"""EX03- Battleship proper"""
 
__author__ = "730647363"
# setup user input
import random
guess: int = 0
def input_guess(grid_size: int, specific: str) -> int:
    assert specific == "row" or specific == "column"
    guess = input("Guess a " + specific + ": ")
    while int(guess) > grid_size:
        guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    while int(guess) < 1:
        guess = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")        
    return guess
# create battleship grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    row_counter: int = 1
    while row_counter <= grid_size:
        row_string: str = ""
        column_counter: int = 1
        if int(row_guess) == row_counter:
            while column_counter <= grid_size:
                if int(column_guess) == column_counter:
                    if correct == True:
                        row_string += RED_BOX
                    else:
                        row_string += WHITE_BOX
                else:
                    row_string += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                row_string += BLUE_BOX
                column_counter += 1
        print(str(row_string))
        row_counter += 1   
# check if the user guess matches the secret boat placement
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int ) -> bool:
    if secret_row == row_guess:
        if secret_column == column_guess:
            return True
    else: 
        return False
# run all sections of program in loop until user guesses correctly or fails five times
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    turn: int = 1    
    while turn < 6:
        print(f"=== Turn {turn}/5 ===")
        row_guess: int = int(input_guess(grid_size,"row"))       
        column_guess: int = int(input_guess(grid_size,"column"))     
        correct: bool = bool(correct_guess(secret_row,secret_column,row_guess,column_guess))
        print_grid(grid_size,row_guess,column_guess,correct)
        if correct == True:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            turn = 7
        else:
            print("Miss!")
        turn += 1
    if turn == 6:
        print("X/5 - Better luck next time!")
if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))







