"""
Inserts a given value into the middle of a given array and returns a new array.

Parameters:
 arr (list): The input array to insert into.
 value: The value to be inserted into the middle of the array

it will return a new array with the given value inserted in the middle.

and if length of the array = 0 
return the value 


"""
def insertShiftArray(arr,value):

 array_length=len(arr)
 middle_index = (array_length // 2)+(array_length % 2)
 shifted_array=[None]*(array_length+1)

 for i in range (middle_index):
  shifted_array[i]=arr[i]
  shifted_array[middle_index]= value

 for i in range (middle_index,array_length):
    shifted_array[i+1]=arr[i]

 if len(arr) == 0:
        return [value]
 
 return shifted_array   

 
# array =[2,4,6,-8]
# value1 = 16

# print(insertShiftArray(array,value1))
    