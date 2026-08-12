print("Welcome to the Calculator Program!", "-----", "Enter the Value to run in the calculator", sep="\n")

def ask_for_numbers():
    try:
        input1 = int(input("Enter the first number: "))
        input2 = int(input("Enter the second number: "))

        return input1, input2
    except ValueError:
        print("Must be a number")

    return 0, 1

def calculate(variable1, variable2):
    try:
        symbol = input("Enter your operation (+ - * / // % **): ").strip()

        if not symbol.isalnum():
            print("It must be a symbol")

        if symbol == "+":
            print("\nAdd", end="\n-----\n")
            product = variable1 + variable2
            print("Answer:", product)
        elif symbol == "-":
            print("\nSubtract", end="\n-----\n")
            product = variable1 - variable2
            print("Answer:", product)
        elif symbol == "*":
            print("\nMultiply", end="\n-----\n")
            product = variable1 * variable2
            print("Answer:", product)
        elif symbol == "/":
            print("\nDivide", end="\n-----\n")
            product = variable1 / variable2
            print("Answer:", product)
        elif symbol == "//":
            print("\nInteger Divide", end="\n-----\n")
            product = variable1 // variable2
            print("Answer:", product)
        elif symbol == "%":
            print("\nModulus", end="\n-----\n")
            product = variable1 % variable2
            print("Answer:", product)
        elif symbol == "**":
            print("\nExponential", end="\n-----\n")
            product = variable1 ** variable2
            print("Answer:", product)
        else:
            print("Must be a symbol of (+ - * / // % **)")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception as e:
        print("Error Caught", e)

cont = True
while cont:
    variable1, variable2 = ask_for_numbers()
    calculate(variable1, variable2)

    print("") # print newline for spacing
    question = input("Continue? ").strip().lower()
    if question == "true" or question == "yes" or question == "t" or question == "y":
        cont = True
    else:
        cont = False
    print("") # print newline for spacing