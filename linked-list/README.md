# Challenge Implementation: Singly Linked Lists

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](assets/Untitled%20(7).jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O 

|insertion Time complexity: O(1)|
|included|Time complexity: O(n)|
|to_string|Time complexity: O(n)|
time and space complexity o(n) n refer to number of nodes

## Solution
```
 def __init__(self) :
        self.head= None

    def insert(self, value):
        insert_node = Node(value)
        insert_node.next = self.head
        self.head = insert_node   



    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    

    
    def to_string(self):
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while current:
                output += f"{str(current.value)} -> "
                current = current.next
            output += "Null"
        return output
    ```