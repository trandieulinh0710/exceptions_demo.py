MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def C_OR_F():
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)


def Q():
    global choice
    while choice != "Q":
        C_OR_F()
        choice = input(">>> ").upper()
    print("Thank you.")


Q()