#   Get a list of numbers as input from a user and calculate the sum of it
user_list = []
print("Enter the set of numbers sepearted by space")
user_list = raw_input().split()
print(user_list)

#  user_list = raw_input()
#  print(user_list)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print(user_list)
print(sum(user_list))

print("\n")
list_size = int(raw_input("Enter the size of the list"))
list_data = []
for i in range(0, list_size):
    element = int(raw_input("Number please : "))
    list_data.append(element)
print("Elements are list", list_data)


