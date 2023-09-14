# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple Function
# def greet():
#     name = input("What's your name?\n")
#     print(f"Hello, your name must be {name}")
#     print("Welcome to the 100 days of code!")
# greet()

# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("Elia")

# Functions with more than 1 input
# def greet_with(name, age):
#     print(f"Hello, my name is {name}")
#     print(f"I'm {age} years old.")
# greet_with("Elia", 19)

# Functions with keywords arguments
def greet_with(name, age):
    print(f"Hello, my name is {name}")
    print(f"I'm {age} years old.")
greet_with(name="Elia", age=19)