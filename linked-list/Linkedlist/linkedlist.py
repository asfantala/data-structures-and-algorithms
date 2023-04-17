from Linkedlist.Node import Node


class LinkedList:
    def __init__(self) :
        self.head= None

    def insert(self, value):
        '''
     Inserts a new node with the given value at the head of the linked list.

        '''
        insert_node = Node(value)
        insert_node.next = self.head
        self.head = insert_node   



    def includes(self, value):
        '''
        Returns True if a node with the given value is present in the linked list, False otherwise.

        '''
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def to_string(self):
        '''
      Returns a string representation of the linked list, with nodes separated by "->" and ending with "Null".

        
        '''
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
    
        
    def append(self, value):
        """
        
                Adds a new node with the given value to the end of the linked list.

        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        """
        Adds a new node with the given new value immediately before the first node that has the value specified.
        If no such node exists, returns "Empty LinkedList"
        """
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
        """
        Adds a new node with the given new value immediately after the first node that has the value specified.
        If no such node exists, returns "Empty LinkedList"
        """
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return "Empty LinkedList"
    


    def __repr__(self):
          return self.to_string()
    
            