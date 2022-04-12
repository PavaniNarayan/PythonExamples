# Given two integer numbers return their product only if the product is greater than 1000,
# else return their sum.

def multiplication_addition(number1, number2):
    product = number1 * number2
    if product > 1000:
        return product
    else:
        return number1 + number2


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

result = multiplication_addition(num1, num2)
print("The result is ", result)
