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

- Given Array: [8, 4, 23, 42, 16, 15]

- Call the Mergesort function on the entire array [8, 4, 23, 42, 16, 15].
- Since the length of the array is greater than 1, proceed with the sorting process.
- Calculate the midpoint of the array as mid = 6 / 2 = 3.
- Split the array into two subarrays: left [8, 4, 23] and right [42, 16, 15].
- Recursively call Mergesort on the left subarray [8, 4, 23].
- Repeat steps 2-5 for the left subarray:
   -  The length of the left subarray is greater than 1, so proceed.
    - Calculate the midpoint of the left subarray as mid = 3 / 2 = 1.
    - Split the left subarray into two subarrays: left [8] and right [4, 23].
    - Recursively call Mergesort on the left subarray [8].
    - Since the length of the left subarray is 1, return [8].
    - Recursively call Mergesort on the right subarray [4, 23].
    - The length of the right subarray is greater than 1, so proceed.
    - Calculate the midpoint of the right subarray as mid = 2 / 2 = 1.
    - Split the right subarray into two subarrays: left [4] and right [23].
    - Recursively call Mergesort on the left subarray [4].
    - Since the length of the left subarray is 1, return [4].
    - Recursively call Mergesort on the right subarray [23].
    - Since the length of the right subarray is 1, return [23].
  - Merge the sorted left and right subarrays [4] and [23] back into the original right subarray [4, 23].
    - Compare the elements at index 0: 4 <= 23, so set arr[0] = 4.
    - The right subarray is fully merged.
    - Merge the sorted left and right subarrays [8] and [4, 23] back into the original left subarray [8, 4, 23].
    - Compare the elements at index 0: 8 <= 4, so set arr[0] = 4.
    - Compare the elements at index 1: 8 > 23, so set arr[1] = 23.
    - The left subarray is fully merged.
    - Merge the sorted left and right subarrays [4, 23] and [42, 16, 15] back into the original array [8, 4, 23, 42, 16, 15].
      -  Compare the elements at index 0: 4 <= 42, so set arr[0] = 4.
      - Compare the elements at index 1: 23 <= 42, so set arr[1] = 23.
      - Compare the elements at index 2: 42 > 16, so set arr[2] = 16.
      -  Compare the elements at index 3: 42 > 15, so set arr[3] = 15.
      -  The right subarray is fully merged.
- The left subarray [8] remains unchanged.
- The resulting sorted array is [4, 8, 15, 16, 23, 42].


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