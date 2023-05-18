from trees.Node import Node

class Binary_tree:
    def __init__(self):
        self.root = None

    def pre_order(self,root):
        if root is not None:
            print(root.value)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)
    # Inorder traversal
# Left -> Root -> Right
          

    def in_order(self,root):
        if root.left is not None:
            self.in_order(root.left)
        if root is not None:
            print(root.value)
        if root.right is not None:
            self.in_order(root.right)



# pre_order(tree1.root)
# tree1 = Tree()

# node1 = Node("A")
# tree1.root = node1

# node2 = Node("B")
# tree1.root.left = node2

# node3 = Node("C")
# tree1.root.right = node3

# node4 = Node("D")
# tree1.root.left.left = node4

# node5 = Node("E")
# tree1.root.left.right = node5

# node6 = Node("F")
# tree1.root.right.left = node6