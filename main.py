# This is a testing ground for Python code

# Practice with class variables

from car import Car

car1 = Car("Tesla", "Model Y", 2024, "White")
car2 = Car("Tesla", "Model S", 2024, "Gray")

# car1.wheels = 6
# car2.wheels = 2
# Car.wheels = 8

print(f"This is a {car1.color} {car1.year} {car1.make} {car1.model}! It has {car1.wheels} wheels!")
print(f"This is a {car2.color} {car2.year} {car2.make} {car2.model}! It has {car2.wheels} wheels!")
