# This is a testing ground for Python code

# Practice with Inheritance

class Animal:
    alive = True
    animal = "Animal"

    def eat(self):
        print(f"This {self.animal} is eating")

    def sleep(self):
        print(f"This {self.animal} is sleeping")


class Rabbit(Animal):
    animal = "Rabbit"

    def run(self):
        print(f"This {self.animal} is running")


class Fish(Animal):
    animal = "Fish"

    def swim(self):
        print(f"This {self.animal} is swimming")


class Hawk(Animal):
    animal = "Hawk"

    def fly(self):
        print(f"This {self.animal} is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

rabbit.eat()
rabbit.sleep()
