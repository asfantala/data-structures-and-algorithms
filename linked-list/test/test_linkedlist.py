import pytest

from linkedlist.linkedlist import LinkedList

def test_instantiate_an_empty_linked_list():
    actual =  str(LinkedList())
    expected = "Empty LinkeList"
    assert actual == expected

def test_insertion():
    linkedlist= LinkedList()
    linkedlist.insert("a")
    actual = str(linkedlist)
    expected = "a -> Null"
    assert actual == expected

def test_head():

    linked_list = LinkedList()
    linked_list.insert("b")
    actual = str(linked_list.head.value)
    expected = "b"
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
    actual = str(ll.includes('A'))
    expected = "True"
    assert actual == expected

def test_search1():
    ll = LinkedList()
    ll.insert(1)
    actual = str(ll.includes('A'))
    expected = 'False'
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



@pytest.fixture
def ll():
    ll = LinkedList()
    return ll
    

