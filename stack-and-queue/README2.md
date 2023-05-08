# Challenge PseudoQueue
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(11).jpg)

## Approach & Efficiency
Big O -> O(1)
## Solution
<!-- Show how to run your code, and examples of it in action -->
```
class PseudoQueue:

    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, val):
        self.stack_one.push(val)

    def dequeue(self):
        if self.stack_one.is_empty() and self.stack_two.is_empty():
            raise IndexError("Is Empty")

        if self.stack_two.is_empty():
            while not self.stack_one.is_empty():
                self.stack_two.push(self.stack_one.pop())

        return self.stack_two.pop()

```