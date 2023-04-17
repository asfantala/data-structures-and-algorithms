# Challenge 06

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](assets/Untitled%20(6).jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O
|||
|-------|-----| 
|append|          Time complexity: O(n)|
|insert before |  Time complexity: O(n)|
|insert_after|Time complexity: O(n)|

time and space complexity o(n) n refer to number of nodes

## Solution
```
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
           return "Empty LinkedList"

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            return "Empty LinkedList"

    def insert_after(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return "Empty LinkedList"
    ```