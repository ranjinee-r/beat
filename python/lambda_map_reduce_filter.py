# Write a Python program to find if a given string starts with a given character using Lambda.
dir(str)

def starting(name,character):
    return name.startswith(character)
name=input("Enter the name: ")
character=input("Enter the character to check it is starts with the name: ")
starting(name,character)

name=input("Enter the name: ")
character=input("Enter the character to check it is starts with the name: ")
start = lambda name,character:name.startswith(character)
start(name,character)

# Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
fruits=["Apple","mango","Orange","apple","kiwi","watermelon","123"]
from functools import reduce
list(filter(lambda a:not a[0].islower(), fruits))
reduce(lambda a,b:a+b, (map(lambda a:len(a), filter(lambda a:a[0].islower(), fruits))))

# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
values=[1,2,8,-3,4,-6]
reduce(lambda a,b:a+b, filter(lambda a:a>0, values))
reduce(lambda a,b:a+b, filter(lambda a:a<0, values))

# Write a Python program to add two given lists using map and lambda.
value1=[1,2,3,4]
value2=[1,2,3,4]
list(map(lambda a,b:a+b, value1,value2))

# Write a Python program to create Fibonacci series up to n using Lambda.
# dout
def fibonacci(n):
    fib_list=[]
    for i in range(n):
        if i==0 or i==1:
            fib_list.append(i)
        else:
            next=fib_list[i-2]+fib_list[i-1]
            fib_list.append(next)
    return fib_list
n=int(input("Enter the range: "))
fibonacci(n)

fib_series = lambda n: reduce(lambda x, _: x+[x[-1] + x[-2]], range(n - 2), [0, 1])
fib_series(5)

# Write a Python program that uses a lambda function to extract even numbers from a list.
values=[1,2,3,4,5,6,7,8,9]
list(filter(lambda a:a%2==0,values))
list(filter(lambda a:a%2==1,values))
list5=[0,7,8]
list7=[9,0,7]
list5+[8]
# Write a Python program using lambda and filter() to count how many words in a list start with a given letter.
names=["ranjinee","nahva","nadiya","kamaru"]
c=lambda a,b:a.startswith(b)
c("ranjinee",'r')
len(list(filter(lambda a:a.startswith('n'),names))) #dout how to pass character

# Write a Python program to find the longest string in a list using reduce() and a lambda function.
names=["ranjinee","nahva","nadiya","kamaru","tsrhgftr"] #dout how to find if two string have same length
reduce(lambda a,b:a if len(a)>len(b) else b, names)

# Write a Python program using a lambda function and filter() to extract all palindromes from a given list of strings.
names=["ranjinee","nahva","malayalam","nadiya","kamaru","tsrhgftr","mom"]
list(filter(lambda a:a==a[::-1], names))

# Write a Python program using map() and a lambda function to capitalize the first letter of each word in a list.
list(map(lambda a:a.capitalize(),names))

# Write a Python program using a lambda function to remove duplicates from a list of numbers and sort the result in ascending order.
numbers=[1,2,65,98,65,3,2,4,6,20,78,55,65]



# Write a Python program to filter out words from a list that have more than 5 letters using lambda and filter().



        
