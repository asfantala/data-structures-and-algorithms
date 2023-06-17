from trees.Node import Node
from trees.Queue import Queue


class Binary_tree:

    '''
    Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order
Each depth first traversal method should return an array of values, ordered appropriately.
    '''
    def __init__(self):
        self.root = None

   
    def pre_order(self, root):
     result = []  # Create an empty list to store the values

     if root is not None:
        result.append(root.value)  # Append the value to the result list
        result.extend(self.pre_order(root.left))  # Recursively traverse the left subtree
        result.extend(self.pre_order(root.right))  # Recursively traverse the right subtree

     return result


    def in_order(self, root):
     result = []  # Create an empty list to store the values

     if root is not None:
        result.extend(self.in_order(root.left))  # Recursively traverse the left subtree
        result.append(root.value)  # Append the value to the result list
        result.extend(self.in_order(root.right))  # Recursively traverse the right subtree

     return result


    def post_order(self, root):
     result = []  # Create an empty list to store the values

     if root is not None:
        result.extend(self.post_order(root.left))  # Recursively traverse the left subtree
        result.extend(self.post_order(root.right))  # Recursively traverse the right subtree
        result.append(root.value)  # Append the value to the result list

     return result

    def breadth_first(self):
        result = []
        if self.root is None:
            return result

        queue = []  # Initialize a list-based queue
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

class BinarySearch(Binary_tree):
    """
    Binary Search Tree class
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

    Add -Arguments: value ,Return: nothing, Adds a new node with that value in the correct location in the binary search tree.

    Contains -Argument: value ,Returns: boolean indicating whether or not the value is in the tree at least once
    
    """
    def add(self, value):

        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                else:
                    current = current.right
            else:
                return
    def contains(self, value):

        current = self.root
        while current:
            if current.value == value:
                return True
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right

        return False
    


