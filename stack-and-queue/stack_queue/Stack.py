from stack_queue.Node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        '''
        Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance
        '''
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''
        Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack
        '''
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            raise Exception("Stack is empty")

    def peek(self):

        '''
        Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
        '''
        if self.top:
            return self.top.value
        else:
            raise Exception("Stack is empty")

        
    def get_size(self):
        return self.size

    def is_empty(self):
        '''
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty
        '''
        return self.top is None