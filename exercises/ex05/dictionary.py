"""Dictionary"""

__author__ = "730647363"

def invert(input: dict[str, str]) -> dict[str, str]:
    output = {}
    for k, v in input.items():
        output[v] = output.get(v, [] + [k])
    return output

def favorite_color(favorite: dict[str, str]) -> str:
    output = {}
    for k, v in favorite.items():
        if v not in output:
            output[v] = 0
        else: 
            output[v] = 0
    return(max(output, k = v.get))

def count(vals: list[str]) -> dict[str, int]:
    result: dict[str,int] = {}
    if vals in result:
        vals += 1
    else:
        vals = 1
    return result

def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    print()

def update_attendance(input: dict[str, list[str]],day: str, student: str) -> dict[str, list[str]]:
    return None    





