while True:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = input("Enter operator (+, -, *, /): ")

    if c == "+":
        print("Result:", a + b)
    elif c == "-":
        print("Result:", a - b)
    elif c == "*":
        print("Result:", a * b)
    elif c == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator")

    choice = input("Do you want to continue? (y/n): ")
    if choice != "y":
        break