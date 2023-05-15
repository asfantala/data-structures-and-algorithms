# Challenge Animal Shelter 
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](Untitled(12).jpg)

## Approach & Efficiency
Big O -> O(1)
## Solution
<!-- Show how to run your code, and examples of it in action -->
```
class Animal:
    def __init__(self, name ,species):
        self.name = name
        self.species = species


class AnimalShelter:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal: Animal):
        if animal.species == 'Dog':
            self.dog.enqueue(animal)
        elif animal.species == 'Cat':
            self.cat.enqueue(animal)
    def dequeue(self, pref=None):
       
        if pref == "Dog":
            return self.dog.dequeue()
        elif pref == "Cat":
            return self.cat.dequeue()
        else:
            return None
```