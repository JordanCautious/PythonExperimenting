# This is a testing ground for Python code

# Practice with Multi-Level Inheritance

class Organism:
    name = "Organism"
    alive = True


class Animal(Organism):
    name = "Animal"

    def eat(self):
        print(f"This {self.name} is eating")


class Dog(Animal):
    name = "Dog"

    def bark(self):
        print(f"This {self.name} is barking")

animal = Animal()
dog = Dog()

dog.bark()
animal.eat()
dog.eat()
print(dog.alive)
