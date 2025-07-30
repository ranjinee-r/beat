try:
    int(input("Enter a number: "))
except:
    print("Please enter the correct number ")
    int(input())

while True:
    try:
        int(input("Enter a number: "))
    except:
        print("Please enter the correct number ")
    else:
        break

print("CALCULATOR")
print("-----------")
while True:
    print("1. Addition.\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")
    while True:
        try:
            op=int(input("Please Enter the Operation Number: "))

            a=int(input("Enter a first number: "))
            b=int(input("Enter a Second number: "))
        except:
            print("Please Correct Number")
        else:
            break
    result=0
    match op:
        case 1:
            result=a+b
            print("The sum is: ",result)
        case 2:
            result=a-b
            print("The difference is: ",result)
        case 3:
            result=a*b
            print("The product is: ",result)
        case 4:
            while True:
                try:
                    result=a/b
                except:
                    print("Please enter a denominator greater than zero.")
                    b=int(input())
                else:
                    print("Result: ",result)
                    break
        case 5:
            break       
        case _:
            print("Please choose a valid operation.")
    
