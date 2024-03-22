"""Test my garden functions."""

__author__ = "730647363"
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
"""Some functions for my garden plan!"""
def test_add_by_kind_edge_case() -> None:
    """Test unlikely use case for add_by_kind function"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}

    add_by_kind(by_kind, "plant", "plant")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    

def test_add_by_kind_use_case() -> None:
    """Tests likely use case for add_by_kind function"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "vegetable", "eggplant")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots", "eggplant"]}

def test_add_by_date_edge_case() -> None:
    """Tests unlikely use case of add_by_date function"""
    by_date: dict[str, list[str]] = {"June": ["Red"], "May": ["Yellow"]}
    add_by_date(by_date, "May", "May")
    assert by_date == {"June": ["Red"], "May": ["Yellow"]}
def test__add_by_date_use_case() -> None:
    """Tests likely use case for add_by_date function"""
    by_date: dict[str, list[str]] = {"June": ["Red"], "May": ["Yellow"]}
    add_by_date(by_date, "May", "Orange")
    assert by_date == {"June": ["Red"], "May": ["Yellow", "Orange"]}
def test_lookup_by_kind_and_date_edge_case() -> None:
    """Tests unlikely use case of lookup_by_kind_and_date function"""
    by_date: dict[str, list[str]] = {"June": ["Red"], "May": ["Yellow"]}
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    lookup_by_kind_and_date(by_date, by_kind, "", "")
    assert by_date == {"June": ["Red"], "May": ["Yellow"]}
   


def test_lookup_by_kind_and_date_use_case() -> None:
    """Tests likely use case for lookup_by_kind_and_date function"""
    by_date: dict[str, list[str]] = {"June": ["Red"], "May": ["Yellow"]}
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    lookup_by_kind_and_date(by_date, by_kind, "April", "tree")
    assert by_date == {"June": ["Red"], "May": ["Yellow"]}