for x in range(3):
    for y in range(2):
        print("{0},{1}".format(x, y))

numbers = [5, 2, 5, 2, 2]
for each_number in numbers:
    print(each_number * "x")


print (">>>>>>>>")


for x_count in numbers:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)
