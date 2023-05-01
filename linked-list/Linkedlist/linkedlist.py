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
    

    def kth_from_end(self,k):
        '''
        Return the node's value that is k places from the tail of the linked list.
        traverse the linked list to find the length and check the conditions 
        '''
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

    def zip_lists(list1,list2):

        '''
        function called zip lists
        Arguments: 2 linked lists
        Return: New Linked List,
        Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
        
        '''
        current1 = list1.head
        current2 = list2.head

        if not current1:
            return list2
        elif not current2:
            return list1
        else:
            while current1 and current2:
                temp1 = current1.next
                temp2 = current2.next
                current1.next = current2
                current2.next = temp1
                current1 = temp1
                current2 = temp2
        if current1:
            current1.next = None
        return list1


        # return new_linkedlist        


    def __repr__(self):
          return self.to_string()
    
    def __str__(self):
        return self.to_string()        