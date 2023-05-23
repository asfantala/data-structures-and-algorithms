import pytest
from trees.Node import Node
from trees.Binary_tree import Binary_tree, BinarySearch

# Can successfully instantiate an empty tree

def test_empty_tree():
    BT = Binary_tree()
    actual = BT.root
    expected = None
    assert actual == expected

 #Can successfully instantiate a tree with a single root node
   
def test_a_tree_with_a_root_node():
    BT = Binary_tree()
    BT.root = Node(1)
    actual = BT.pre_order(BT.root)
    expected = [1]
    assert actual == expected

def test_pre_order():
    BT = Binary_tree()
    BT.root = Node(1)
    BT.root.left = Node(2)
    BT.root.right = Node(3)
    BT.root.left.left = Node(4)
    BT.root.left.right = Node(5)
    BT.root.right.left = Node(6)
    BT.root.right.right = Node(7)

    actual = BT.pre_order(BT.root)
    expected = [1, 2, 4, 5, 3, 6, 7]
    assert actual == expected
   

def test_in_order():
    binary_tree = Binary_tree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)
    binary_tree.root.left.left = Node(4)
    binary_tree.root.left.right = Node(5)
    binary_tree.root.right.left = Node(6)
    binary_tree.root.right.right = Node(7)

    actual = binary_tree.in_order(binary_tree.root)
    expected = [4, 2, 5, 1, 6, 3, 7]
    assert actual == expected



def test_post_order():
    binary_tree = Binary_tree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)
    binary_tree.root.left.left = Node(4)
    binary_tree.root.left.right = Node(5)
    binary_tree.root.right.left = Node(6)
    binary_tree.root.right.right = Node(7)

    actual = binary_tree.post_order(binary_tree.root)
    expected = [4, 5, 2, 6, 7, 3, 1]
    assert actual == expected


def test_tree_right_and_left():
    tree1 = BinarySearch()
    tree1.add(5)  
    tree1.add(4)  
    tree1.add(6)  

    actual = tree1.in_order(tree1.root)
    expected = [4, 5, 6]
    assert actual == expected


def test_contains_true():
    tree1 = BinarySearch()
    tree1.add(5)  
    tree1.add(4)  
    tree1.add(6)  
    actual = tree1.contains(4)
    expected = True
    assert actual == expected


def test_contains_false():
    tree1 = BinarySearch()
    tree1.add(5)  
    tree1.add(4)  
    tree1.add(6)  
    actual = tree1.contains(7)
    expected = False
    assert actual == expected


def test_findmax ():
    tree1 = BinarySearch()
    tree1.add(5)  
    tree1.add(4)  
    tree1.add(6)  
    actual = tree1.findMax(tree1.root)
    expected = 6
    assert actual == expected


def test_find_max1():
    tree = Binary_tree()
    
    # Create the tree nodes
    node1 = Node(24)
    node2 = Node(51)
    node3 = Node(1)
    node4 = Node(3)
    node5 = Node(70)
    node6 = Node(12)
    node7 = Node(17)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    tree.root = node1
    
    actual = tree.findMax(tree.root)
    expected = 70
    assert actual == expected    