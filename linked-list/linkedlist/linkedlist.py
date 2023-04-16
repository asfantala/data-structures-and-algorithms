from linkedlist.Node import Node

class LinkedList:
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
    

    def __str__(self):
    
        output  = ""
        
        if self.head is None:
            output  = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            output += "Null"
        return output   

    def __repr__(self):
          return self.__str__()
    
            