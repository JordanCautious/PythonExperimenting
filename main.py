# This is a testing ground for Python code

# Practice with Exceptions

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("You can only use numbers!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(f"Your result is {result}. No exceptions have been found!")
finally:
    print("This code will always run")