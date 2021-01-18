# this is a calculator


def main():
    menu_choice = ""
    initial_value = float(input("Enter an initial operand: "))
    solution = initial_value
    print()

    while menu_choice != "Q" and menu_choice != "q":
        menu_choice = menuChoice(menu_choice)
        if menu_choice == "1":
            solution = addition(solution)
        elif menu_choice == "2":
            solution = subtraction(solution)
        elif menu_choice == "3":
            solution = multiplication(solution)
        elif menu_choice == "4":
            solution = division(solution)
        elif menu_choice == "5":
            solution = modulus(solution)
        elif menu_choice == "6":
            solution = raiseToPower(solution)
        elif menu_choice == "7":
            solution = root(solution)
        print()
        print("=================================")
        print("Solution: " + str(solution))
        print("=================================")

    print()
    print("-------Program Terminated-------")


def menuChoice(menu_choice):
    print()
    print("--------------Menu---------------")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Root")
    print("Q. Quit")
    print()

    menu_choice = input("Choose an operator: ")
    print()
    return menu_choice


def addition(solution):
    operand = float(input("What value would you like to add? "))
    solution += operand
    print()
    return solution


def subtraction(solution):
    operand = float(input("What value would you like to subtract? "))
    solution -= operand
    print()
    return solution


def multiplication(solution):
    operand = float(input("What value would you like to multiply? "))
    solution *= operand
    print()
    return solution


def division(solution):
    operand = float(input("What value would you like to divide? "))
    solution /= operand
    print()
    return solution


def modulus(solution):
    operand = float(input("What value would you like to find the remainder with? "))
    solution %= operand
    print()
    return solution


def raiseToPower(solution):
    exponent = float(input("What power would you like to raise to? "))
    solution **= exponent
    print()
    return solution


def root(solution):
    exponent = float(input("Which root would you like to take? "))
    solution = solution ** (1 / exponent)
    print()
    return solution


main()
