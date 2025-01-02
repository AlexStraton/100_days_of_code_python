from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

functions = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    continue_to = True
    number = int(input('Type a number: '))

    while continue_to:
        operator = input('Choose an operator. Type +, -, *, or /: ')
        second_number = int(input('Type a second number: '))
        result = functions[operator](number, second_number)
        print(f"{number:.2f}", operator, f"{second_number:.2f}", '=', result)
        continue_to = input("Continue with previous result? y or n: ").lower()

        if continue_to == 'y':
            number = result
        else:
            continue_to = False
            clear_screen()
    calculator()
    
calculator()
    