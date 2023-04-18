# Challenge 07

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](assets/Untitled%20(8).jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O
|||
|-------|-----| 
|Time complexity  |   O(n)|
|space complexity |   O(1)|


Time complexity is O(n) because of the traverse and n refer to length of linked  list and the space complexity is O(1) it needs constant space in the memory 

## Solution
```
    def kth_from_end(self,k):
       
        if not self.head:
           return "Empty LinkedList"
        
        if k < 0 :
            return "k is not a positive integer"
    
        current = self.head
        length = 0
        while current:
            length +=1
            current= current.next
        if length == 1:
                return "linked list of a size 1"
        
        if k > length:
            return 'k is greater than the length of the linked list.'
        
        position = length - k - 1
        current = self.head
        for i in range(position):
            current = current.next

        return current.value    
    ```