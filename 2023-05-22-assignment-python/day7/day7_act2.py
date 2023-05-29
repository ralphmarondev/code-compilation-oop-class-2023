# Ralph Maron Eda
# BSCPE-2A
#
# Create a calculator app
# The user will choose between 4 math operations
#       [Add, Subtract, Multiply, and Divide]
# The application will ask for 2 numbers
# Display the result
# The application will ask again if the user wants to
#       try again
# Use the appropriate Exception [ex. Invalid input such
#       as text and zero division]

def choices():
    print("A - Add")
    print("S - Subtract")
    print("M - Multiply")
    print("D - Divide")
    print("E - Exit")


def add_function():
    first_num = int(input("First Number: "))
    second_num = int(input("Second Number: "))

    print(f"Sum: {first_num + second_num}")


def subtract_function():
    first_num = int(input("First Number: "))
    second_num = int(input("Second Number: "))

    print(f"Sum: {first_num - second_num}")


def multiply_function():
    first_num = int(input("First Number: "))
    second_num = int(input("Second Number: "))

    print(f"Sum: {first_num * second_num}")



def division_function():
    melit = ValueError
    try:
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        result = 0

        try:
            result = first_num / second_num
        except ZeroDivisionError:
            print("Cannot Divide by zero!")
        finally:
            print(f"Quotient: {result}")
    except melit: # your name is here, because you're my exception!  -maron :)
        print("Please input integers only")


def main():
    while True:
        choices()
        choice = input("Choice ~$ ")

        if choice.upper() == "A":
            add_function()
        elif choice.upper() == "S":
            subtract_function()
        elif choice.upper() == "M":
            multiply_function()
        elif choice.upper() == "D":
            division_function()
        else:
            print("Please don't be stupid, is that on the choices?")

        another_one = input("Do you want to try again? [Y/N]: ")
        if another_one.upper() == "N":
            break
    print("Bye")


if __name__ == '__main__':
    main()
