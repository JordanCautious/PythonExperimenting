# This is a testing ground for Python code

# Practice with Object-Oriented Programming in Python

from car import Car

car1 = Car("Tesla", "Model Y", 2024, "White")
car2 = Car("Tesla", "Model S", 2024, "Gray")

print(f"This is a {car1.color} {car1.year} {car1.make} {car1.model}!")
print(f"This is a {car2.color} {car2.year} {car2.make} {car2.model}!")

car1.drive()
car2.drive()

car1.stop()
car2.stop()
