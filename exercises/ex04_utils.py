"""EX04 - Utils"""
 
__author__ = "730647363"
def all(vals: list[int], given: int) -> bool:
    check: bool = True
    for idx in range(0, len(vals)):
        if vals[idx] != given:
            check = False
    return check       
def max(vals: list[int]) -> int:
    if len(vals) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = vals[0]
    for idx in range(0, len(vals)):
        if vals[idx] > largest:
            largest = vals[idx]
    return largest
def is_equal(vals1: list[int], vals2: list[int]) -> bool:
    check: bool = True
    if len(vals1) == len(vals2):
        for idx in range(0, len(vals1)):
            if vals1[idx] != vals2[idx]:
                check = False
    else: 
        check = False
    return check
def extend(vals1: list[int], vals2: list[int]) -> None:
    if len(vals1) == 0:
        raise ValueError("max() arg is an empty List")
    if len(vals2) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        for idx in range(0, len(vals2)):
            vals1.append(vals2[idx])
