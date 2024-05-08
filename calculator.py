num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
def calculate(x, y, operator):
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    elif operator == '*':
        return x*y
    elif operator == '/':
        return x/y
    else:
        return "Invalid operator"
