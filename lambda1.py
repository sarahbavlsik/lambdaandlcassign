remainder  = lambda num: num % 2 
print(remainder(5))

## remainder is a function object
def testfunc(num):
    print(num)
    return lambda x: x* num

result10 = testfunc(10)
result100 = testfunc(100)
#these are both function objects
print(type(result10))
print(result10(5))
print(result100(5))
#alternate way to do the above 
result10 = lambda x: x*10
result100 = lambda x: x* 100
print(result10(5))
print(result100(5))

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)
#mapped applies the expression to every item in the list
mapped_list= list(map(lambda num: num %2, numbers_list))
print(mapped_list)

def addition(n):
    return n+n
numbers = [1,2,3,4]
result = list(map(addition, numbers))
print(result)

result = list(map(lambda n: n + n, numbers))
print(result)

numbers = (1,2,3,4)
numbers2 = (5,6,7,8)
result = list(map(lambda x,y: x + y, numbers, numbers2))
print(result)

import os
clear = lambda: os.system("cls")
clear()
#clears the screen