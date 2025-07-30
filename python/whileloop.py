value=1
while value<6:
    print(value)
    #value+=1
    value=value+1

value=1
while value<6:
    print(value)
    value+=1

value=5
while value>0:
    print(value)
    value-=1

fruits=['apple','banana','cherry']
length=len(fruits)
value=0
while value<length:
    print(fruits[value])
    value+=1

fruits=['apple','banana','cherry']
length=len(fruits)-1
while length>=0:
    print(fruits[length])
    length-=1

row=0
while row<6:
    col=0
    while col<row:
        print("*",end=" ")
        col+=1
    print()
    row+=1

row=0
while row<6:
    col=0
    while col<row:
        print("*",end=" ")
        col+=1
    print()
    row+=1

number=[]
value=int(input("enter a number"))
while value!=0:
    number.append(value)
    value=int(input("enter a number"))
number

number=[]
sum=0
value=int(input("enter a number"))
while value!=0:
    if sum+value>100:
        break
    number.append(value)
    sum=sum+value
    value=int(input("enter a number"))
print(sum)
number

num=[0,0,1,9,0,5,3,0,4,9,8]
num1=num.copy()
num1
i=0
len(num)
while i<len(num):
    if num[i]==0:
       num1.remove(num[i])
       num1.append(num[i])
    i+=1
num1








