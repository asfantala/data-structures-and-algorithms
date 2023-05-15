from stack_queue.Queue import Queue
from abc import ABC, abstractmethod



class Animal(ABC):
    @abstractmethod
    def __init__(self, name ,species)->None:
        self.name = name
        self.species = species

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
      self.animals = []  


  def enqueue(self, animal):
    if isinstance (animal,(Cat,Dog)):
        
       self.animals.append(animal)

    
  def dequeue(self, pref):
       for animal in  self.animals :
         if animal.species == pref :
            self.animals.remove(animal)
            return animal
        
  
  # def dequeueCat(self):
  #   if len(self.cats) == 0: return None
  #   cat = self.cats[0]
  #   self.cats = self.cats[1:]
  #   return cat
    
  # def dequeueDog(self):
  #   if len(self.dogs) == 0: 
  #      return None
  #   dog = self.dogs[0]
  #   self.dogs = self.dogs[1:]
  #   return dog
