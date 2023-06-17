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

-The input array is [8, 4, 23, 42, 16, 15].

- Iteration 1:

- i = 1, value = 4
- The while loop is skipped since 8 is not greater than 4.
- The value 4 is inserted at the correct position.
- The array becomes [4, 8, 23, 42, 16, 15].

- Iteration 2:

- i = 2, value = 23
- The while loop is skipped since 8 is not greater than 23.
- The value 23 remains in its position.
- The array remains [4, 8, 23, 42, 16, 15].

- Iteration 3:
- i = 3, value = 42
- The while loop is skipped since 23 is not greater than 42.
- The value 42 remains in its position.
- The array remains [4, 8, 23, 42, 16, 15].

- Iteration 4:

- i = 4, value = 16
- The while loop is executed.
- Since 42 is greater than 16, we shift 42 to the right.
- The array becomes [4, 8, 23, 42, 42, 15].
- The while loop continues.
- Since 23 is greater than 16, we shift 23 to the right.
- The array becomes [4, 8, 23, 23, 42, 15].
- The while loop continues.
- Since 8 is greater than 16, we shift 8 to the right.
- The array becomes [4, 8, 8, 23, 42, 15].
- The while loop continues.
- Since 4 is greater than 16, we shift 4 to the right.
- The array becomes [4, 4, 8, 23, 42, 15].
- The while loop ends, and we insert the value 16 at the correct position.
- The array becomes [4, 8, 16, 23, 42, 15].

- Iteration 5:

- i = 5, value = 15
- The while loop is executed.
- Since 42 is greater than 15, we shift 42 to the right.
- The array becomes [4, 8, 16, 23, 42, 42].
- The while loop continues.
- Since 23 is greater than 15, we shift 23 to the right.
- The array becomes [4, 8, 16, 23, 23, 42].
- The while loop continues.
- Since 16 is greater than 15, we shift 16 to the right.
- The array becomes [4, 8, 16, 16, 23, 42].
- The while loop continues.
- Since 8 is greater than 15, we shift 8 to the right.
- The array becomes [4, 8, 8, 16, 23, 42].
- The while loop continues.
- Since 4 is greater than 15, we shift 4 to the right.
- The array becomes [4, 4, 8, 8, 16, 23].
- The while loop ends, and we insert the value 15 at the correct position.
- The array becomes [4, 8, 15, 16, 23, 42].
The final sorted array is [4, 8, 15, 16, 23, 42].

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
- The space complexity of the insertion sort algorithm is O(n) because it requires additional space for the sorted array
