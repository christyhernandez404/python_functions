# Addition
def addition(a, b):
    return a + b

# Subtraction


def subtraction(a, b):
    return a - b

# Multiplication


def multi(a, b):
    return a * b

# Division


def divi(a, b):
    return a / b

# Modulus


def modu(a, b):
    return a % b

# Exponentiation


def expo(a, b):
    return a ** b

# Floor division


def fl_divi(a, b):
    return a // b


def user_input1():
    return float(input("Input first number:"))


def operation():
    return input(
        "Input operation (addition, subtraction, multi, divi, expo, modu, floor divi):")


def user_input2():
    return float(input("Input second number:"))


def calculator():
    num1 = user_input1()
    op = operation()
    num2 = user_input2()

    if op == 'addition':
        print(f"The result is:, {addition(num1, num2)}")
    elif op == 'subtraction':
        print(f"The result is:, {subtraction(num1, num2)}")
    elif op == 'multi':
        print(f"The result is:, {multi(num1, num2)}")
    elif op == 'divi':
        print(f"The result is:, {divi(num1, num2)}")
    elif op == 'expo':
        print(f"The result is:, {expo(num1, num2)}")
    elif op == 'modu':
        print(f"The result is:, {modu(num1, num2)}")
    elif op == 'floor divi':
        print(f"The result is:, {fl_divi(num1, num2)}")
    else:
        print("Invalid data entry. Try again.")


calculator()
