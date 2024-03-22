"""Splitting a dictionary into two lists"""

__author__ = "730647363"
def get_keys(input_keys: dict[str, int]) -> list[str]:
    output_list: list[str] = []
    for key in input_keys:
        output_list.append(key)
    return output_list
def get_values(input_keys: dict[str, int]) -> list[int]:
    output_list: list[int] = []
    for key in input_keys:
        output_list.append(input_keys[key])
    return output_list
