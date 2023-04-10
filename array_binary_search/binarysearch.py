def BinarySearch(list, search_key):
    first_index = 0
    size = len(list)
    last_index = size - 1
    
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        mid_element = list[mid_index]
        
        if mid_element == search_key:
            return mid_index
        elif mid_element < search_key:
           first_index = mid_index + 1
        else:
            last_index = mid_index - 1

    return -1
  
    
