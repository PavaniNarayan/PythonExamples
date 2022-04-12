numbers = [1, 1, 3, 2, 4, 66, 77, 2, 3, 4, 4, 5, 5, 77, 66, 9929, ]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
