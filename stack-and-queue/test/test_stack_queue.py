import pytest
from stack_queue.Stack import Stack
from stack_queue.Queue import Queue
from stack_queue.Stack_queue_pseudo import PseudoQueue
from stack_queue.AnimalShelter import AnimalShelter
from stack_queue.AnimalShelter import Cat
from stack_queue.AnimalShelter import Dog

def test_stack():
    s = Stack()
    assert s.is_empty() == True

def test_push():
    s = Stack()
    s.push(1)
    assert s.peek() == 1


def test_push_multiple_values():
    s= Stack() 
    s.push(1)
    s.push(2)
    assert s.peek() == 2


def test_pop_off():
    s= Stack() 
    s.push(1)
    s.push(2)
    s.pop()
    assert s.peek() == 1


def test_is_empty():
    s= Stack()
    assert s.is_empty() == True

def test_peek():
    s= Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    assert s.peek() == 4   



def test_instantiate_empty_stack():
    s= Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.is_empty() == True

def test_raise_exception():

    s= Stack()
    try:
        s.pop()
    except Exception as e:
        assert str(e) == "Stack is empty"
   

def test_queue():
    q = Queue()
    assert q.is_empty() == True

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    assert q.peek() == 1

def test_enqueue_multiple():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
   
    assert q.peek() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3  

def test_peek_queue():     
    q=Queue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.peek() == 2

def test_queues_empty():
    q= Queue() 
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty() == True

def test_excep():
    q= Queue() 
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty() == True    
    try:
        q.dequeue()
    except Exception as e:
        assert str(e) == "Queue is empty"

def test_pseudo_queue_happy_path():
        queue = PseudoQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.dequeue() == 6


def test_pseudo_queue_empty():
    queue = PseudoQueue()
    with pytest.raises(IndexError):
        queue.dequeue()    
    
def test_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))
    assert(str(shelter.dequeue('cat')), "Hanzack")
    assert(str(shelter.dequeue('cat')), "Garfield")
    assert(str(shelter.dequeue('dog')), "Pluto")
    assert(str(shelter.dequeue('dog')), "Clifford")
    assert(str(shelter.dequeue('cat')), "Tony")
    assert(str(shelter.dequeue('cat')), "None")
    assert(str(shelter.dequeue('dog')), "Blue")
    assert(str(shelter.dequeue('dog')), "None")


