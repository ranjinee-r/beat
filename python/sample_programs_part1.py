# 1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# Write a Python program which accepts the radius of a circle from the user and compute the area. Sample Output : r = 1.1 Area = 3.8013271108436504
def area(r):
    area=3.14*r**2
    return area
radius=float(input("Enter the radius: "))
area(radius)

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name=input("Enter the first name: ")
last_name=input("Enter the last name: ")
print(last_name+" "+first_name)

def reverse_first_last(first_name,last_name):
    return last_name+" "+first_name
first_name=input("Enter the first name: ")
last_name=input("Enter the last name: ")
reverse_first_last(first_name,last_name)

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
def comma_seperated(num):
    list1=num.split(",")
    n=tuple(list1)
    return n,list1
num=input("Enter a comma seperated number sequence: ")
new=comma_seperated(num)
for i in new:
    print(i)


# Write a Python program to accept a filename from the user and print the extension of that.
filename=input("Enter a filename: ")
index_dot=filename.index(".")
print("Extension of the filename is: ")
for i in range(index_dot+1,len(filename)):
    print(filename[i],end="")


def extension_find(filename):
    index_dot=filename.index(".")
    extension=''
    print("Extension of the filename is: ")
    for i in range(index_dot+1,len(filename)):
        extension=extension+filename[i]
    return extension
filename=input("Enter a filename: ")
extension_find(filename)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def computation(n):
    return n+n*n+n*n*n
n=5
computation(n)

# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum_three_numbers(a,b,c):
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
sum_three_numbers(a,b,c)

# Write a Python program to test whether a passed letter is a vowel or not.
def vowel_or_not(letter):
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        return "It is vowel."
    else:
        return "It is not a vowel"
letter=input("Enter a letter: ")
vowel_or_not(letter)

# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
def last_program(a,b,c):
    if a==b or a==c or b==c:
        return 0
    else:
        return a+b+c
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
last_program(a,b,c)

