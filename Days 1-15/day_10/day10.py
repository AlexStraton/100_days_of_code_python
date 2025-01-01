from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {"+": add, "-": subtract, "*": multiply, "/": divide}


number = int(input('Type a number'))
operator = input('Choose an operator. Type +, -, *, or /')
second_number = int(input('Type a second number'))
result = functions[operator](number, second_number)


print(f"{number:.2f}", operator, f"{second_number:.2f}", '=', result)

continue_to = input("Continue with previous result? y or n").lower()

while continue_to == 'y':
    operator = input('Choose an operator. Type +, -, *, or /')
    second_number = int(input('Type a second number'))
    new_result = functions[operator](result, second_number)

    print(f"{result:.2f}", operator, f"{second_number:.2f}", '=', new_result)
    result = new_result
    continue_to = input("Continue with previous result? y or n").lower()
print('You have finished')