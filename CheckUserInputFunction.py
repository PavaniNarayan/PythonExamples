#   Use string isdigit() method to check user input is number or string
def check_is_digit(ins):
    if ins.strip().isdigit():
        print("User Input is number")
    else:
        print("User Input is String")


num1 = raw_input("Enter the number and hit Enter")
check_is_digit(num1)

num2 = raw_input("Enter the number and hit Enter")
check_is_digit(num2)

if num2.isdigit():
    print("The return value of isdigit is True : Because all characters in a given string are digits")
else:
    print("The return value of isdigit is False : Because all characters in a given string are not digits")

# Use the isinstance() function to check if a python varible in num or string
num = 24.2
print("THE", isinstance(num, (int, float)))
