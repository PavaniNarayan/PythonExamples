my_details = {
    "Name": "Pavani",
    "Age": 25,
    "BirthDate": "27-May-1996",
    "Place of Birth": "Venkatagiri Kota"
}

print(my_details)
my_details["Stay"] = "Bangalore"
print(my_details)

try:
    print(my_details["Hobby"])
except KeyError:
    print(my_details.get("Hobby", "Cooking"))

#
convert_digit_to_words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

data = raw_input("Phone: ")
output = ""
for each_number in data:
    # print(each_number)
    try:
        print(convert_digit_to_words[each_number])
        output = output + convert_digit_to_words[each_number] + " "
    except KeyError:
        output = output + convert_digit_to_words.get(each_number, "!") + " "

print(output)
