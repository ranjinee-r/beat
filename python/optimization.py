def square(list1):
    square_list=[]
    for i in list1:
        square_list.append(i**2)
    return square_list
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
id(list1[0])
square(list1)

# Generator
def square1(list1):
    for i in list1:
        yield i**2

list(square1(list1))
for value in square1(list1):
    print(value)

# Iterator
name="pradeep"
a=iter(name)
next(a)

# map() function
list6=[1,2,3,4,5]
list7=[]
for value in list6:
    list7.append(value**2)
list7

def square(a):
    return a**2

list(map(square,list6))
list(map(lambda a:a**2,list6))

words=["nahva","ranjinee","nadiya","kamaru"]
list(map(lambda a:a.upper(),words))
list(map(lambda a:len(a),words))

# reduce() function
def sum(values):
    sum=0
    for i in values:
        sum+=i
    return sum
values=[1,2,3,4,5]
sum(values)

dir(__builtins__)
from functools import reduce
def result(a,b):
    return a+b

reduce(result,values)
reduce(lambda a,b:a+b,values)
def maxx(a,b):
    if a>b:
        return a
    else:
        return b
    
reduce(maxx,values)
reduce(lambda a,b:a if a>b else b,values)