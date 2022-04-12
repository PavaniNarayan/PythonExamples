#  Check user input is a positive number or negative
def check_number_status(number):
    if number >= 0:
        print("The Number Entered is Positive")
    else:
        print("The Number Entered is Negative")


try :
    numb = int(raw_input("Enter a number"))
except ValueError:
    numb = float(raw_input("Enter a float number"))

check_number_status(numb)
