# This is a testing ground for Python code

# Practice with args

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(5, 5, 5, 5, 5))
