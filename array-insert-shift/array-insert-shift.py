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
    