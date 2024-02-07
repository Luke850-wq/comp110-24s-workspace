"""Battleship game with grid!"""

__author__ = "730647363"
"""Setup"""
gridsize: int = 4
srow: int = 3
scolumn: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
row_counter: int = 1
rowg: str = input("Guess a row: ")
while int(rowg) > gridsize:
    rowg = input(f"The grid is only {gridsize} by {gridsize}. Try again: ")
while int(rowg) < 1:
    rowg = input(f"The grid is only {gridsize} by {gridsize}. Try again: ")
columng: str = input("Guess a column: ")
while int(columng) > gridsize:
    columng = input(f"The grid is only {gridsize} by {gridsize}. Try again: ")
while int(columng) < 1:
    columng = input(f"The grid is only {gridsize} by {gridsize}. Try again: ")
"Grid output"
while row_counter <= gridsize:
    row_string: str = ""
    column_counter: int = 1
    if int(rowg) == row_counter:
        while column_counter <= gridsize:
            if int(columng) == column_counter:
                if int(columng) == scolumn:
                    row_string += RED_BOX
                else:
                    row_string += WHITE_BOX
            else:
                row_string += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= gridsize:
            row_string += BLUE_BOX
            column_counter += 1
    print(str(row_string))
    row_counter += 1
"""Response to hit/miss"""
if int(rowg) == srow:
    if int(columng) == scolumn:
        print("Hit!")
    else:
        print("Close! Correct row, wrong column.")
else:
    if int(columng) == scolumn:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")