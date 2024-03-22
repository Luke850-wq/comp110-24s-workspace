"""Some functions for my garden plan!"""

__author__ = "730647363"
def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    if new_plant in by_kind:
        by_kind[new_plant_kind].append[new_plant]
    else:
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)

def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Return str under date to sow seeds"""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)

def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return str with list of plants of a specific kind in specific month"""
    assert kind in plants_by_kind
    assert month in plants_by_date
    kind_list: list[str] = plants_by_kind[kind]
    #Get a list of all plants planted in a month
    month_list: list[str] = plants_by_date[month]
    #Go through both lists: find elements that appear in both
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:
                combined_list.append(other_plant)
    if len(combined_list) > 0:
        return f"kinds to plant in {month}: {combined_list}"
    else:
        return f"No plants to plant in {month}."