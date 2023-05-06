# Challenge Stack and Queue 

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(10).jpg)

## Approach & Efficiency
For the Stack:

push: O(1) - this operation adds a new element to the top of the stack, which takes constant time, regardless of the size of the stack.
pop: O(1) - this operation removes the element from the top of the stack, which takes constant time, regardless of the size of the stack.
peek: O(1) - this operation accesses the element at the top of the stack, which takes constant time, regardless of the size of the stack.
is_empty: O(1) - this operation simply checks if the stack is empty, which takes constant time, regardless of the size of the stack.
For the Queue:

enqueue: O(1) - this operation adds a new element to the back of the queue, which takes constant time, regardless of the size of the queue.
dequeue: O(1) - this operation removes the element from the front of the queue, which takes constant time, regardless of the size of the queue.
peek: O(1) - this operation accesses the element at the front of the queue, which takes constant time, regardless of the size of the queue.
is_empty: O(1) - this operation simply checks if the queue is empty, which takes constant time, regardless of the size of the queue.
## Solution
<!-- Show how to run your code, and examples of it in action -->
```
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)

        #if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        #if the queue is empty
        if self.front == None:
            raise Exception("Queue is empty")
        # if the queue contains only one node
        if self.front == self.rear:
            self.rear = None
            #self.front = None
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.front == None:
            raise Exception("Queue is empty")
        return self.front.value
    
    def is_empty(self):
        return self.front is None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            raise Exception("Stack is empty")


    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise Exception("Stack is empty")

        
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.top is None        


```