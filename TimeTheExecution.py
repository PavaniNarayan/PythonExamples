import timeit

#   timeit.timeit(stmt, setup, timer, number)

mysetup = "from math import sqrt"
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement
print (timeit.timeit(setup=mysetup,
                     stmt=mycode,
                     number=10000))
mycode2='''
print("My Name is Pavani")'''
print(timeit.timeit(stmt=mycode2, setup=mysetup, number=5))
