def square(n):
    return n * n


# map -map(function_name, listOrTuple)
list_Items = [1, 2, 3, 4, 5]
map_object = map(square, list_Items)
print(map_object)
print(list(map_object))

# list comprehension
# [experession/result for item in list if conditional]

x = [i * 2 for i in list_Items]
print(x)
x = [i for i in list_Items if i % 2 == 0]
print(x)

