for i in range(7):
    print(i*"*")
x=7
for i in range(x):
    print((x-i)*"*")

for i in range(x):
    print((x-i)*" ",i*"*")


for i in range(x):
    print((x-i)*" ",i*"* ")

for i in range(x,0,-1):
    print((x-i)*" "+i*"*")

for i in range(x,0,-1):
    print((x-i)*" "+i*"* ")

for i in range(x):
    print(((x-i)*" "+i*"* "))

for row in range(1,6):
    for space in range(6,row-2,-1):
        print(" ",end="")
    for col in range(0,row):
        print(space,end=" ")
    print()

for row in range(1,6):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("* ",end="")
    print()

for row in range(1,7):
    for col in range(1,row):
        print(col,end=" ")
    print()

for row in range(6,0,-1):
    for col in range(0,row):
        print(row,end=" ")
    print()

for row in range(6,0,-1):
    for col in range(1,row):
        print(col,end=" ")
    print()

for row in range(1,7):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()

for row in range(5,0,-1):
    for col in range(row,6):
        print(col,end=" ")
    print()

string="python"
for row in range(1,7):
    for col in range(0,row):
        print(string[col],end=" ")
    print()

string="python"
for row in range(6,0,-1):
    for col in range(0,row):
        print(string[col],end=" ")
    print()

x=6
num=1
for row in range(1,x):
    for col in range(0,row):
        print(num,end=" ")
        num=num+1
    print()

x=6
num=1
for row in range(1,x):
    for col in range(0,row):
        print(num,end=" ")
        num=num+1
    print()
    num=1

num=0
for row in range(1,6):
    num=num+row
    for col in range(0,row):
        num1=num
        print(num1,end=" ")
        num=num-1
    print()


num=1
for row in range(0,7):
    start=num+row-1
    for col in range(0,row):
        print(start,end=" ")
        start=start-1
        num=num+1
    print()

num=2
for row in range(1,6):
    num=row+1
    for col in range(0,row):
        print(row,end=" ")
    for i in range(row+1,6):
        print(num,end=" ")
        num=num+1
    print()

for value in range(1,6):
    print(value)






    






 
    
