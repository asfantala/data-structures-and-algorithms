# Merge Sort
### Introduction:
- In this article, we will dive into the inner workings of the Merge Sort algorithm and provide a step-by-step analysis of its execution using the sample array [8, 4, 23, 42, 16, 15]. We will also discuss the time complexity of Merge Sort and why it is an efficient choice for sorting large datasets.

### Pseudocode:

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
        DECLARE mid <-- n / 2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
     
```

### Code implementation :
       ```
        def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right,arr)

def merge (left,right,arr):
    i = 0
    j = 0
    k = 0
    

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    
       ```
### Steps:

1. Begin with the given array [8, 4, 23, 42, 16, 15].
2. Call the Mergesort function on the entire array.
3. During the divide phase, calculate the midpoint of the array as 6 / 2 = 3.
4. Split the array into two subarrays: left (from index 0 to mid-1) and right (from index mid to end).
5. Recursively call Mergesort on both the left and right subarrays.
6. Continue dividing the subarrays until they reach a length of 1.
7. During the merge phase, merge the sorted left and right subarrays together using the Merge function.
8. Compare elements from the left and right subarrays and place them in the original array in sorted order.
9. Repeat the merging process until the original array is fully sorted.
10. The resulting sorted array is [4, 8, 15, 16, 23, 42].


### Test :
- Test the code by running pytest
```
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

```
### Time Complexity:
- Merge Sort has a time complexity of O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into halves during the divide phase and merges them together during the merge phase. Each division takes O(log n) time, and each merge operation takes O(n) time. Overall, Merge Sort exhibits efficient performance, especially for large datasets, making it a preferred choice for sorting applications.
- The space complexity of Merge Sort is O(n), where n is the number of elements in the array