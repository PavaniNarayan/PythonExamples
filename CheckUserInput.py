def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")

try:
    input1 = input("Enter your Age ")
except NameError:
    input1 = raw_input("Enter your Age ")
check_user_input(input1)

try:
    input2 = input("Enter any number ")
except NameError:
    input1 = raw_input("Enter any number ")
check_user_input(input2)

try:
    input2 = input("Enter the last number ")
except NameError:
    input2 = raw_input("Enter the last number ")
check_user_input(input2)

