"""Mutating functions."""

__author__ = "730647363"
# Part1


def manual_append(list: list[int], b: int) -> None:
    """Append."""
    list.append(b)

c: list[int] = [1, 2, 3]
manual_append(c, 2)
print(c)
# Part2-double
def double(list2: list[int]) -> None:
    """double"""

    loop: int = len(list2) - 1
    while loop >= 0:
        list2[loop] *= 2
        loop -= 1
a: list[int] = [1,2,3]
double(a)
print(a)