# Insertion Sort

### Introduction:
- In this article, we will embark on a journey to explore the insertion sort algorithm. We will begin by understanding the pseudocode, converting it into actual code, and meticulously analyzing each step to comprehend how the algorithm functions. Furthermore, we will incorporate comprehensive test cases to verify the correctness of our implementation. Through visualizations and detailed explanations, we aim to provide a comprehensive understanding of insertion sort.

### Pseudocode :
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

```

### Code implementation :
```python   
def insertion_sort(input):
    sorted = []
    sorted.append(input[0])

    for i in range(1, len(input)):
        insert(sorted, input[i])

    return sorted

def insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i += 1

    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i += 1

    sorted.append(value)
``` 

### Step-by-Step Explanation and Visualization:

- The input array is [8, 4, 23, 42, 16, 15].
1. The sorted array is initially empty.
2. The first element of input, which is 8, is appended to the sorted array. 
      - sorted: [8]
3. Starting from the second element (4) of input, the insert function is called.
      - value: 4
      - The while loop compares value (4) with the elements in sorted until it finds the correct position to insert.
      - Since 4 is less than 8, the loop condition fails, and i remains 0.
      - The second while loop swaps the elements to make space for the insertion.
      - sorted remains unchanged as there is no need to swap elements.
      - sorted: [8]
      - The value (4) is appended to the sorted array.
      - sorted: [8, 4] 
4. The next element in input is 23.
      - value: 23
      - The first while loop finds the correct position for 23, which is between 4 and 8.
      - i becomes 1.
      - The second while loop swaps the elements to make space for the insertion.
      - sorted: [8, 8, 4]
      - The value (23) is inserted at the correct position.
      -  sorted: [8, 23, 4]
5. The process continues for the remaining elements of input.
      - input[3] = 42:
      - sorted: [8, 23, 4]
      - sorted: [8, 23, 42, 4]
      -  input[4] = 16:
      - sorted: [8, 23, 42, 4]
      -  sorted: [8, 16, 23, 42, 4]
      -  input[5] = 15:
      -  sorted: [8, 16, 23, 42, 4]
      -  sorted: [8, 15, 16, 23, 42, 4]
      -  The final sorted array is [4, 8, 15, 16, 23, 42].


### Test Cases:
In this article i tested these :
- Reverse-sorted: [20,18,12,8,5,-2]
- Few uniques: [5,12,7,5,5,7]
- Nearly-sorted: [2,3,5,7,13,11]

```python 
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
```


### Complexity 
- insertion sort has a time complexity of O(n^2)
- space complexity of insertion sort is O(1)