from stack_queue.Queue import Queue
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, species: str, name: str) -> None:
        self.species = species
        self.name = name


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__("dog", name)


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__("cat", name)

class AnimalShelter():

  '''
  When dequeuing,iterate through the queue until you find an animal with the preferred species (pref). If found, that animal is dequeued and returned.
If the preferred species is not found, until the main animals queue is empty.
.
  
  '''
  def __init__(self):
    self.cats, self.dogs = [], []
  
  def enqueue(self, animal):
    if animal.__class__ == Cat: 
       self.cats.append(animal)

    else:                       
       self.dogs.append(animal)
  
  def dequeueAny(self):
    if len(self.cats): return self.dequeueCat()
    return self.dequeueDog()
  
  def dequeueCat(self):
    if len(self.cats) == 0: return None
    cat = self.cats[0]
    self.cats = self.cats[1:]
    return cat
    
  def dequeueDog(self):
    if len(self.dogs) == 0: 
       return None
    dog = self.dogs[0]
    self.dogs = self.dogs[1:]
    return dog
