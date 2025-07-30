def add():
    a=5
    b=10
    return a+b

add()

def pattern(x=5):
    for i in range(x):
        print((x-i)*" ",i*"* ")

pattern(6)

def sum(*list1):
    print(list1)
    sum1=0
    for i in list1:
        sum1+=i
    return sum1
list1=[1,2,3,4,5]
sum(1,2,3,4)

def upper(names):
    upper_names=[]
    for words in names:
        upper_names.append(words.upper())
    return upper_names

names=["ranjinee","nahva","kamaru","nadiya"]
upper(names)

def upper(**names):
    upper_names=[]
    for words in names:
        upper_names.append(words.upper())
    return upper_names


upper("ranjinee","nahva","kamaru","nadiya")

details={"Name":"Ranjinee",
         "Age":21,
         "Gender":"Female"}
key=details.keys()
details.items()
key
for k,v in details.items():
    print(k,":",v)

dir(dict)


def dictionary(**details):
    details
    for k,v in details.items():
        print(k,":",v)

dictionary(name="ranjinee",age=21,gender="female")


#Python program to count the total number of digits in a number.
def count_digit(num):
    number=str(num)
    count=0
    for i in number:
        count+=1
    return count

num=int(input("Enter the Number: "))
print("Total no of digits in a given number: ",count_digit(num))

# Python program to check if the given string is a palindrome.
def palindrome(word):
    rev_word=word[::-1]
    if word==rev_word:
        return "The given string is palindrome."
    else:
        return "The given string is not palindrome"

word=input("Enter a string: ")
print("Palindrome of the given string is: ",palindrome(word))


def palindrome(word):
    rev_word=""
    for i in range(len(word)-1,-1,-1):
        rev_word+=(word[i])
    if word==rev_word:
        return "The given string is palindrome."
    else:
        return "The given string is not palindrome"
    
word=input("Enter a string: ")
print("Palindrome of the given string is: ",palindrome(word))

# Python program to display all numbers within a range except the prime numbers
def prime(a,b):
    for i in range(a,b+1):
        for j in range(2,i//2+1):
            if i%j==0:
                print(i)
                break
prime(1,20)

# Python program that accepts a string and calculates the number of digits and letters.
def count_letters_digits(sample_string):
    letter_count=0
    number_count=0
    for i in sample_string:
        if i.isalpha():
            letter_count+=1
        elif i.isnumeric():
            number_count+=1
    return letter_count,number_count
sample_string=input("Enter a string: ")
count_letters_digits(sample_string)

# Python program to convert the month name to a number of days.
def month_name_to_days(month_name):
    month_days={"january":31,
                "february":28,
                "march":31,
                "april":30,
                "may":31,
                "june":30,
                "july":31,
                "august":31,
                "september":30,
                "october":31,
                "november":30,
                "december":31}
    return month_days[month_name]

month_name=input("Enter the month name: ")
print("No of days in this month is: ",month_name_to_days(month_name))
dir(str)

# Count the number of vowels in a string using a for loop
def no_of_vowels(sentence):
    count_of_vowel=0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u':
            print(i)
            count_of_vowel+=1
    return count_of_vowel
sentence=input("Enter a string: ")
print("No of vowels in a given string is: ",no_of_vowels(sentence.lower()))

# Print numbers in a list until a negative number is encountered using a while loop
def number_printing(list_of_numbers):
    for i in list_of_numbers:
        if i>=0:
            print(i)
        else:
            break
list_of_numbers=[2,8,0,9,9,7,5,-2]
number_printing(list_of_numbers)

# Print numbers from 1 to 10. If a number is even, skip it using a for loop and else clause
def skip_even(n):
    for i in range(n):
        if i%2==1:
            print(i)
        else:
            continue
n=int(input("Enter the range: "))
skip_even(n)

# Write a Python program to sum all the items in a list.
def sum_of_items_in_list(items_in_list):
    sum=0
    for i in items_in_list:
        sum+=i
    return sum
items_in_list=[1,2,3,4,5]
print("Sum of items in the list: ",sum_of_items_in_list(items_in_list))

# Write a Python program to get the largest number from a list.
def largest_number(numbers):
    largest=numbers[0]
    for i in numbers:
        if i>largest:
            largest=i
    return largest
        
numbers=[10,20,5,6,60,100,7,900,4,100,30]
largest_number(numbers)

def largest_number(numbers):
    numbers.sort()
    return numbers[-1]
numbers=[10,20,5,6,60,100,7,900,4,100,30]
largest_number(numbers)


# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a 
# given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_of_string(sample_list):
    count_string=0
    for i in sample_list:
        if len(i)>=2 and i[0]==i[len(i)-1]:
            count_string+=1
    return count_string
sample_list=['abc', 'xyz', 'aba', '1221','12','abcd','baab']
count_of_string(sample_list)

# Write a Python program to remove duplicates from a list.
def remove_duplicates(duplicate_list):
    new_list=[]
    for i in duplicate_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
duplicate_list=["apple","banana","apple","mango","kiwi"]
remove_duplicates(duplicate_list)

def remove_duplicates(duplicate_list):
    for i in duplicate_list:
        if duplicate_list.count(i)>=2:
            duplicate_list.remove(i)
    return duplicate_list
duplicate_list=["apple","banana","apple","mango","kiwi"]
remove_duplicates(duplicate_list)

def remove_duplicates(duplicate_list):
    list_set=set(duplicate_list)
    return list(list_set)
duplicate_list=["apple","banana","apple","mango","kiwi"]
remove_duplicates(duplicate_list)



# Python program to check if a given number is an Armstrong number
def amstrong(num):
    num_str=str(num)
    amstrong_number=0
    for i in num_str:
        amstrong_number+=int(i)**len(num_str)
    if amstrong_number==num:
        return "It is amstrong"
    else:
        return "It is not an amstrong"
num=int(input("Enter a number: "))
amstrong(num)

# Write a Python program to check a list is empty or not.
def check_empty(list1):
    if len(list1)==0:
        return "The list is empty"
    else:
        return "The list is not empty"
list1=[1,2,3,4]
check_empty(list1)

# Write a Python program to clone or copy a list.
def copy_list(list2):
    new_list=list2.copy()
    return new_list
list2=[1,2,3,4,5]
copy_list(list2)

def copy_list(list2):
    new_list=[]
    for i in list2:
        new_list.append(i)
    return new_list
list2=[1,2,3,4,5]
copy_list(list2)

# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)
def square():
    square_list=[]
    for i in range(1,31):
        if i<=5 or 26<=i<=30:
            square_list.append(i**2)
    return square_list
square()

def square(a,b):
    square_list=[]
    for i in range(a,b+1):
        if i<=a+5 or b-5<i<=b:
            square_list.append(i**2)
    return square_list
square(1,30)

# Write a Python program access the index of a list.
def index_list(list3,word):
    return list3.index(word)
list3=[1,2,3,4]
index_list(list3,3)

# Write a Python program to get unique values from a list.
def unique(list4):
    unique_list=[]
    for i in list4:
        if list4.count(i)==1:
            unique_list.append(i)
    return unique_list
list4=["apple","mango","kiwi","apple","apple","mango","watermelon","papaya"]
unique(list4)

# Write a Python program to find common items from two lists
def common_items(first,second):
    return list(set(first).intersection(set(second)))
first=["apple","mango","kiwi","apple","apple","mango","watermelon","papaya"]
second=["apple","banana","apple","mango","kiwi"]
common_items(first,second)

def common_items(first,second):
    common=[]
    for i in first:
        for j in second:
            if i==j:
                common.append(j)
                if common.count(i)>=2:
                    common.remove(i)
    return common
first=["apple","mango","kiwi","apple","apple","mango","watermelon","papaya"]
second=["apple","banana","apple","mango","kiwi"]
common_items(first,second)






