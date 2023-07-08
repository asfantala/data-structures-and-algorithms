import pytest
from hashtable import Hashtable
from hashmap_repeated import repeated_word
from tree_intersection.tree_intersection import tree_intersection

from left_join.left_join import left_join
# from trees.trees.Binary_tree import Binary_tree
# from trees.trees.Node import Node

def test_set_and_get():
    ht = Hashtable()
    ht.set("1", "1")
    assert ht.get("1") == "1"


def test_set_replaces_existing_key():
    ht = Hashtable()
    ht.set("1", "1")
    ht.set("1", "2")
    assert ht.get("1") == "2"


def test_get_nonexistent_key():
    ht = Hashtable()
    assert ht.get("1") is None


def test_has_existing_key():
    ht = Hashtable()
    ht.set("1", "1")
    assert ht.has("1") is True


def test_has_nonexistent_key():
    ht = Hashtable()
    assert ht.has("1") is False


def test_keys():
    ht = Hashtable()
    ht.set("1", "1")
    ht.set("2", "2")
    ht.set("3", "3")
    keys = ht.keys()
    assert "1" in keys
    assert "2" in keys
    assert "3" in keys
    assert len(keys) == 3


def test_collision_handling():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("1", "1")
    ht.set("2", "2")
    assert ht.get("1") == "1"
    assert ht.get("2") == "2"


def test_retrieve_collision_value():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("1", "1")
    ht.set("2", "2")
    assert ht.get("1") == "1"
    assert ht.get("2") == "2"


def test_hash():
    ht = Hashtable()
    assert ht.hash("key1") >= 0
    assert ht.hash("key1") < ht.size



def test_repeated_word():
     # Test case 1
    str = "Once upon a time, there was a brave princess who..."
    assert repeated_word(str) == "a"

    # Test case 2
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."
    assert repeated_word(input_string2) == "it"

    # Test case 3
    input_string3 = "It was a queer, sultry summer, the summer they electrocuted me, and I didn’t realize I was dead yet..."
    assert repeated_word(input_string3) == "summer"




# def test_tree_intersection():
#     tree1 = Binary_tree()
#     tree1.root = Node(1)
#     tree1.root.left = Node(2)
#     tree1.root.right = Node(3)
#     tree1.root.left.left = Node(4)
#     tree1.root.left.right = Node(5)
#     tree1.root.right.left = Node(6)
#     tree1.root.right.right = Node(7)

#     tree2 = Binary_tree()
#     tree2.root = Node(1)
#     tree2.root.left = Node(2)
#     tree2.root.right = Node(3)
#     tree2.root.left.left = Node(4)
#     tree2.root.left.right = Node(5)
#     tree2.root.right.left = Node(6)
#     tree2.root.right.right = Node(7)

#     assert tree_intersection(tree1.root, tree2.root) == {1, 2, 3, 4, 5, 6, 7}

#     tree2.root.right.right = Node(8)
#     assert tree_intersection(tree1.root, tree2.root) == {1, 2, 3, 4, 5, 6}

#     tree2.root = None
#     assert tree_intersection(tree1.root, tree2.root) == set()



def test_left_join():
    synonyms = {"diligent": "employed", "fond": "enamored", "guide": "usher", "outfit": "garb", "wrath": "anger"}
    antonyms = {"diligent": "idle", "fond": "averse", "guide": "follow", "outfit": None, "wrath": "delight"}
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]
    assert left_join(synonyms, antonyms) == expected



