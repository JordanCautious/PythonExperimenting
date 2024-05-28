# This gets the first and last name from the user
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your last age?: "))
height = float(input("What is your last height?: "))
human = input("Are you human?(Y/N): ")

# This combines the two variables together
full_name = f"{first_name} {last_name}"

# Converting the response to boolean
if human == "Y":
    human = True
elif human == "N":
    human = False
else:
    print("This should not be possible!")

# Converting boolean to appropriate phrase
if not human:
    outcome = "are not"
else:
    outcome = "are"

# This prints the message to the terminal
print(f"Hello, {full_name}! You are {age} years old with a height of {height}cm! You {outcome} human!")