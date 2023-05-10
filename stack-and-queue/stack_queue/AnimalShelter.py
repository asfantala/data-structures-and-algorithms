from stack_queue.Queue import Queue

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
    # def dequeue(self, pref):
    #  if pref != 'Dog' and pref != 'Cat':
    #     return None

    #  if pref == 'Dog':
    #     return self.dog.dequeue()
    #  elif pref == 'Cat':
    #     return self.cat.dequeue()

   

   





