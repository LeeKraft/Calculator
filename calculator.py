#!/usr/bin/python3

def calculate(a, b, operation):
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b
    else:
        result = "Unknown operation"
    return result

def ask_operation():
    operation = input()
    return operation

def run_calculator():
    a = int(input())
    b = int(input())
    operation = ask_operation()
    result = calculate(a, b, operation)
    print(result)

# run_calculator()
print("Hello World!")