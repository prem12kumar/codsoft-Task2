"operator funtion"
def add(x, y):
    return x +y
def subtract(x, y):
    return x -y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

#  calculator 
while True:
    "inputs giving to system"

    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    
    choice = input("Enter your choice: ")
    
    '''if your  leaving without using any operation'''
    if choice == 'leave':
        break
    
    '''checking operators are valid'''
    if choice not in ['add', 'subtract', 'multiply', 'divide']:
        print("Invalid input")
        continue
    
    '''enter two inputs'''
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    "chosen operator is being performed"
    if choice == 'add':
        result = add(num1, num2)
    elif choice == 'subtract':
        result = subtract(num1, num2)
    elif choice == 'multiply':
        result = multiply(num1, num2)
    elif choice == 'divide':
        result = divide(num1, num2)
    
    '''display  Result''' 
    print("Result: ", result)