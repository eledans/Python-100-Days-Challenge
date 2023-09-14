from art import logo
import os
# Add
def add(n1,n2):
    return n1 + n2

# Substract
def substract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

operation = {
    "+" : add, 
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True 

    while should_continue:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system("cls")
            calculator()

calculator()