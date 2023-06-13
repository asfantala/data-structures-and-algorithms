import pytest
from mergesort.mergesort import mergesort

def test_merge_sort():
    # Test case 1: Random array
    arr1 = [8, 4, 23, 42, 16, 15]
    expected1 = [4, 8, 15, 16, 23, 42]
    assert mergesort(arr1) == expected1

    # Test case 2: Reverse-sorted array
    arr2 = [20, 18, 12, 8, 5, -2]
    expected2 = [-2, 5, 8, 12, 18, 20]
    assert mergesort(arr2) == expected2

    # Test case 3: Array with few unique elements
    arr3 = [5, 12, 7, 5, 5, 7]
    expected3 = [5, 5, 5, 7, 7, 12]
    assert mergesort(arr3) == expected3

    # Test case 4: Nearly-sorted array
    arr4 = [2, 3, 5, 7, 13, 11]
    expected4 = [2, 3, 5, 7, 11, 13]
    assert mergesort(arr4) == expected4

if __name__ == '__main__':
    pytest.main()
