def reversearray(arr):
    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = temp
    return arr

arr1 =[1,2,3,4,5,6]
print(reversearray(arr1))