class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        '''
        Arguments: value
        adds a new node with that value to the back of the  queue with an O(1) Time performance
        '''
        node = Node(value)

        #if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    # def dequeue(self):
    #     '''
    #     Arguments: none
    #     Returns: the value from node from the front of the queue
    #     Removes the node from the front of the queue
    #     Should raise exception when called on empty queue
    #     '''
    #     #if the queue is empty
    #     if self.front == None:
    #         raise Exception("Queue is empty")
    #     # if the queue contains only one node
    #     if self.front == self.rear:
    #         self.rear = None
    #         #self.front = None
    #     temp = self.front
    #     self.front = self.front.next
    #     temp.next = None

    #     return temp.value

    def dequeue(self):
        '''
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should return None when called on empty queue
        '''
        if self.front == None:
            return None
        node = self.front
        self.front = self.front.next
        if self.front == None:
            self.back = None
        return node.value
    def peek(self):
        
        '''
        peek
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        '''
        if self.front == None:
            raise Exception("Queue is empty")
        return self.front.value
    def is_empty(self):
        '''
        is empty
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        '''
        return self.front is None