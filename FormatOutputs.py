# Display Output by separating each value
name = raw_input('Enter Name ')
zip_code = int(raw_input('Enter zip code '))
street = raw_input('Enter street name ')
house_number = int(raw_input('Enter house number '))

# Display all values separated by hyphen
print("The House Number {0},{1} at {2} belongs to {3}".format(house_number, street, zip_code, name))
print("The House Number {House_Num},{Street} at {Zip_Code} belongs to {Name}".format(House_Num=house_number,
                                                                                     Street=street, Zip_Code=zip_code,Name=name))

# Left Justified, Right Justified, Center Justified
print("The House Number".ljust(50, "%"))
print("The House Number".rjust(50, "*"))
print("The House Number".center(50, ">"))

#
print('The House Number is {:<25}'.format(name))
print('The House Number is {:>25}'.format(name))
print('The House Number is {:^25}'.format(name))
# print("The House Number is {:d}".f)
