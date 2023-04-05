# Challenge array-insert-shift
 Create a function that accept an array and added value
function has a for in range to loop through shifted array first from the first index to the middle index and push the values and second for to push values after mid index until
return shifted array with added value
## Whiteboard Process
![whiteboard](./assets/Untitled%20(2).jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O 
Time -> O(n) because it need to shift all elements in the array to the right in order to make space for the new element
Space -> O(n)we will need to create a new array to hold the shifted elements

## Solution
<!-- Show how to run your code, and examples of it in action -->
```python 
code :
def insertShiftArray(arr,value):
 array_length=len(arr)
 middle_index = (array_length // 2)+(array_length % 2)
 shifted_array=[None]*(array_length+1)

 for i in range (middle_index):
  shifted_array[i]=arr[i]
  shifted_array[middle_index]= value

 for i in range (middle_index,array_length):
    shifted_array[i+1]=arr[i]


 return shifted_array   

 
array =[2,4,6,-8]
value1 = 16

print(insertShiftArray(array,value1))
```