# This is a testing ground for Python code

# Practice with functions

def hello(person, age):
    print(f"Hello, {person}. You are {age} years old!")


names = {"Jordan": 23, "Brice": 22, "LeBron": 39}

for name, age in names.items():
    hello(name, age)
