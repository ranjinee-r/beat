a=int(input("Enter a first number: "))
a
b=int(input("Enter a second number: "))
b
choice=int(input("1.Addition \n 2.Substraction \n 3.Multiplication\n 4.Division \n 5.Reminder\n"))
if choice==1:
    print("sum = ",a+b)
elif choice==2:
    print("Difference = ",a-b)
elif choice==3:
    print("Product = ",a*b)
elif choice==4:
    print("Quotient: ",a/b)
elif choice==5:
    print("Reminder = ",a%b)
else:
    print("Invalid choice")

print("a = ",a, "\nb = ",b, "\nsum = ",a+b,"\nDifference = ",a-b,"\nProduct = ",a*b,"\nQuotient = ",a/b,"\nReminder= ",a%b)
