#   import timeit


# Binary Search used Divide and Conquer method
# it is performed on sorted list
# it divides the list into half and then compares the element with middle,
# if not it-- element is less than mid, then it is researched
# if more it is searched in other half
import timeit


def binary_search(mylist, find):
    #   print("Length of mylist is", len(mylist))
    while len(mylist) > 0:  # True
        mid = (len(mylist)) // 2  # 4
        #   print("The mid value of mylist is", mid)  # 2
        if mylist[mid] == find:
            # Element found and return the index value
            return mid
        elif find < mylist[mid]:
            mylist = mylist[0:mid]
        else:
            mylist = mylist[mid + 1:]
    # Element not found
    return False


list1 = [1, 2, 3, 4, 5, 13, 14, 56, 78, 99]
elem = 2
found = binary_search(list1, elem)
print("The return value of Binary Search is {}".format(found))


# Linear Search
# Find the element by comparing with first element and then with next

def linear_search(mylist1, find1):
    print("Find {0}, in list {1} using Linear Search".format(find1, mylist1))
    for x in mylist1:
        print("Each element in X is", x)
        if find1 == x:
            return x
    return False


print("The Linear search value is", linear_search([1, 2, 3, 4, 5, 6, 7], 1))


# Compute Binary Search Time
def binary_time():
    setup_code = ('\n'
                  '    from main import binary_search\n'
                  '    from random import randint\n'
                  '    ')
    test_code = '''mylist=[x for x in range(10000)]
    find = randint(0, len(mylist))
    binary_search(mylist, find)
    '''
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=3, number=10000)

    #   printing minimum exec. time
    print('Binary search time: {}'.format(min(times)))


binary_time()
