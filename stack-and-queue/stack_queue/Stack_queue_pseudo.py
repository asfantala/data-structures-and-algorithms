from stack_queue.Stack import Stack


class PseudoQueue:
    """
    A class that implements a queue using two stacks.

    Methods:
    enqueue -- Adds an element to the queue
    dequeue -- Removes and returns the next element from the queue
    """
    

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