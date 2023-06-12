import pytest
from insertion.insertion import insertion_sort

def test_insertion():
    input = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(input)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion2():
    input = [20, 18, 12, 8, 5, -2]
    actual = insertion_sort(input)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_insertion3():
    input = [5, 12, 7, 5, 5, 7]
    actual = insertion_sort(input)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected    


def test_insertion4():
    input = [2, 3, 5, 7, 13, 11]
    actual = insertion_sort(input)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected