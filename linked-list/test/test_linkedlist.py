import pytest

from linkedlist.linkedlist import LinkedList

def test_instantiate_an_empty_linked_list():
    ll = LinkedList()
    actual = ll.to_string()
    expected = "Empty LinkedList"
    assert actual == expected

def test_insertion():
    linkedlist = LinkedList()
    
    linkedlist.insert(1)
    actual = linkedlist.to_string()
    expected = "1 -> Null"
    assert actual == expected

def test_head():
    linked_list = LinkedList()
    linked_list.insert("b")
    actual = linked_list.to_string()
    expected = "b -> Null"
    assert actual == expected

def test_includes():

    linked_list = LinkedList()
    linked_list.insert('b')
    actual = linked_list.includes('b')
    expected = True
    assert actual == expected

def test_insert_multiple_node():
    ll = LinkedList()
    ll.insert('A')
    ll.insert('B')
    ll.insert('C')
    actual = str(ll)
    expected = 'C -> B -> A -> Null'
    assert actual == expected

def test_search():
    ll = LinkedList()
    ll.insert('A')
    actual = ll.includes('A')
    expected = True
    assert actual == expected


def test_search1():
    ll = LinkedList()
    ll.insert(1)
    actual = str(ll.includes('A'))
    expected = 'False'
    assert actual == expected   
    
    

def test_return():
    ll = LinkedList()
    ll.insert("Ta")
    ll.insert('La')
    ll.insert('aa')
    ll.insert('08')
        
    actual = str(ll)
    expected = '08 -> aa -> La -> Ta -> Null'
    assert actual == expected     
def test_append():
    ll = LinkedList()
    ll.append(1)
    ll.append('A')
    actual = str(ll)
    expected = '1 -> A -> Null'
    assert actual == expected

def test_multiple_node_append():
    ll = LinkedList()
    ll.append('A')
    ll.append('B')
    ll.append('C')
    actual = str(ll)
    expected = 'A -> B -> C -> Null'
    assert actual == expected


def test_insert_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 5)
    actual = ll.head.next.value
    expected = 5
    assert actual == expected

def test_insert_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_before(1, 5)
    actual = ll.head.next.value
    expected = 1
    assert actual == expected
       

def test_insert_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 5)
    actual = ll.head.next.next.value
    expected = 5
    assert actual == expected

    

    
def test_insert_after_last():
    ll = LinkedList()
    ll.insert("T")
    ll.insert("A")
    ll.insert("C")
    ll.insert_after("C", "D")
    actual = str(ll)
    expected = 'C -> D -> A -> T -> Null'
    assert actual == expected
    
@pytest.fixture
def ll():
    ll = LinkedList()
    return ll
    

