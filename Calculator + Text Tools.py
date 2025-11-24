def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose + - * / : ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operation")

calculator()




