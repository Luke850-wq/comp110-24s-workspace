pets: list[str] = ["Louie", "Bo", "Bear"]
for pet in pets:
    print(f"Good boy, {pet}!")

"""Practice with for loops + functions"""

def even_words(inp_list: list[str]) -> list[str]:
    """What it does is a mystery! ;)"""
    even_list: list[str] = []
    for elem in inp_list:
        if len(elem) % 2 == 0:
            even_list.append(elem)
    return even_list
a: list[str] = ["Alysssa", "Katie", "Anusha"]
even_words(a)