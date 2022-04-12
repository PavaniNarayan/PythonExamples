#   The program will stop only when the user enters the number input.

while True:

    try:
        num = int(raw_input("Enter a Int number"))
        break
    except ValueError:
        try:
            num = float(raw_input("Enter a float number"))
            break
        except ValueError:
            print("Please Enter a valid number!!, you entered a wrong number")
