# Challenge Binary Tree 
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(12).jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- The Big O time complexity of a Binary Search Tree’s insertion and search operations is O(h), or O(height). In the worst case, we will have to search all the way down to a leaf, which will require searching through as many nodes as the tree is tall. In a balanced (or “perfect”) tree, the height of the tree is log(n). In an unbalanced tree, the worst case height of the tree is n.

- The Big O space complexity of a BST search would be O(1). During a search, we are not allocating any additional space.
## Solution
<!-- Show how to run your code, and examples of it in action -->

```

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



class BinarySearch(Binary_tree):
   
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
    


```