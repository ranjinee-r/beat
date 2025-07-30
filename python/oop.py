class Name:
    def sum(self,a,b):
        sum=a+b
        return sum

object_name=Name()
object_name.sum(2,3)

dir(object_name)
type(object_name)

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        sum=self.a+self.b
        return sum
    def difference(self):
        difference=self.a-self.b
        return difference
    def product(self):
        product=self.a*self.b
        return product
    def division(self):
        division=self.a/self.b
        return division
    def quotient(self):
        quotient=self.a//self.b
        return quotient
    def reminder(self):
        reminder=self.a%self.b
        return reminder
    def square(self):
        square1=self.a**2
        square2=self.b**2
        return square1,square2
    def change(self,c,d):
        self.a=c
        self.b=d
calc=Calculator(10,5)
calc.sum()
calc.difference()
calc.product()
calc.division()
calc.quotient()
calc.reminder()
calc.square()
calc.change(20,10)
calc.a
calc.b
dir(calc)

class Person:
    def demo(self):
        print("Hello Person")
class Student(Person):
    def demo1(self):
        print("Hello Student")
student_obj=Student()
student_obj.demo1()
dir(student_obj)

# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("Amount Deposited: Rs. ",amount,". Current Balance: Rs. ",self.balance)
        else:
            print("Please Enter Valid Amount.")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print("Amount Withraw: Rs. ",amount,". Current Balance: Rs. ",self.balance)
        else:
            print("Insufficient Balance or Invalid Amount")
    def check_balance(self):
        print("The current balance is: Rs. ",self.balance)
    def check_account_details(self):
        print("ACCOUNT DETAILS")
        print("---------------")
        print("Account Number: ",self.account_number)
        print("Customer Name: ",self.customer_name)
        print("Date of Opening: ",self.date_of_opening)
        print("Current Balance: ",self.balance)

customer1=BankAccount(9876543298,1000,"12:04:2024","Ranjinee R")
customer1.deposit(5000)
customer1.withdraw(4000)
customer1.check_balance()
customer1.check_account_details()

customer2=BankAccount(8921876336,500,"02:04:2021","Nahva C")
customer2.deposit(7500)
customer2.withdraw(2000)
customer2.check_balance()
customer2.check_account_details()

# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def calculate_emp_salary(self,salary,hours_worked):
        if hours_worked>50:
            overtime=hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.emp_salary=overtime_amount+salary
            print("Salary of the Employee: ",self.emp_salary)
        else:
            self.emp_salary=salary
            print("Salary of the Employee: ",self.emp_salary)
    def emp_assign_department(self,department):
        self.emp_department=department
        print("The Employee with ID:",self.emp_id," Name:",self.emp_name," is Assigned to New Department: ",self.emp_department)
    def print_employee_details(self):
        print("EMPLOYEE DETAILS")
        print("-----------------")
        print("Employee Id: ",self.emp_id)
        print("Employee Name: ",self.emp_name)
        print("Employee Salary: ",self.emp_salary)
        print("Employee Department: ",self.emp_department)

employee1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee1.calculate_emp_salary(50000,55)
employee1.emp_assign_department("SALES")
employee1.print_employee_details() 

employee2=Employee("JONES", "E7499", 45000, "RESEARCH")
employee2.calculate_emp_salary(45000,48)
employee2.emp_assign_department("ACCOUNTING")
employee2.print_employee_details() 

employee3=Employee("MARTIN", "E7900", 50000, "SALES")
employee3.calculate_emp_salary(50000,60)
employee3.emp_assign_department("ACCOUNTING")
employee3.print_employee_details() 

employee4=Employee("SMITH", "E7698", 55000, "OPERATIONS")
employee4.calculate_emp_salary(55000,72)
employee4.emp_assign_department("RESEARCH")
employee4.print_employee_details() 

# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
class Restaurant:
    def __init__(self,menu_items,book_table,customer_orders):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_orders=customer_orders
        self.table_no=0
    def add_item_to_menu(self,item):
        if item not in self.menu_items:
            self.menu_items.append(item)
            print("The New Menu Items: ",self.menu_items)
        else:
            print("Item Already Exists")
    def book_tables(self,table_no):
        if table_no not in self.book_table:
            self.book_table.append(table_no)
            self.table_no=table_no
            print("Table",table_no,"is reserved.")
        else:
            print("Table",table_no,"is already reserved.")
    def customer_order(self,**orders):
        if self.table_no>0:
            self.customer_orders[self.table_no]=orders
            print("Order taken")
            print("Customer Order")
            print("---------------")
            for a,b in orders.items():
                print(a," ",b)
        else:
            print("Please book the table to place the order.")
    def display_menu_items(self):
        for i in self.menu_items:
            print(i)
order1=Restaurant(["idly","dosa","poori","ghee_roast"],[1,2],{})
order1.add_item_to_menu("biriyani")
order1.book_tables(int(input("Please enter table number for booking between 1-10: ")))
print("Please order from the menu items.")
order1.display_menu_items()
order1.customer_order(poori=1,ghee_roast=2,biriyani=6)

                    
"""def customer_order(self,**orders):
        if self.table_no>0:
            self.customer_orders[self.table_no]=orders
            for i in orders.keys():
                if i not in self.menu_items:
                    print(i," is not in menu")
                    self.customer_orders[self.table_no].pop(i)
            if self.customer_orders[self.table_no].values()!=[]:
                print("Order taken")
                print("Customer Order")
                print("---------------")
                for a,b in orders.items():
                    print(a," ",b)
            else:
                print("Please order the food which is available in the menu card.")
        else:
            print("Please book the table to place the order.")"""


# Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price
class Inventory:
    def __init__(self,item_id,item_name,stock_count,price):
        self.item_id=item_id
        self.item_name=item_name
        self.stock_count=stock_count
        self.price=price
        self.item={}
        self.item[self.item_id]={"Item Name":self.item_name,"Stock Count":self.stock_count,"Price":self.price}
    def add_item(self,id,name,stock,amount):
        if id not in self.item.keys():
            self.item[id]={"Item Name":name,"Stock Count":stock,"Price":amount}
            print("Current Items After Adding a New Item")
            print("--------------------------------------")
            print("Item Id\t\tItem Name\tStock Count\tPrice\n")
            for a,b in self.item.items():
                print(a,end="\t\t")
                for i,j in b.items():
                    print(j,end="\t\t")
                print()
        else:
            print("The item id is already exist.")
    def update_item(self,id,new_stock):
        if id in self.item.keys():
            self.item[id]["Stock Count"]+=new_stock
            print("The current stock count of an item id: ",id," item name: ",self.item[id]["Item Name"]," is: ",self.item[id]["Stock Count"])
        else:
            print("The item id is not present.")
    def check_item_details(self,id):
        if id in self.item.keys():
            print("Item Details")
            print("-------------")
            print("Item Id : ",id)
            for a,b in self.item[id].items():
                print(a,":",b)
item1=Inventory(1,"dress",3,2000)
item1.add_item(int(input("Enter a Item Id: ")),input("Enter a Item Name: "),int(input("Enter a Stock Count: ")),int(input("Enter a Price: ")))
item1.update_item(int(input("Enter a item id for adding a stock count: ")),int(input("Enter a new stock count: ")))
item1.check_item_details(int(input("Enter a Item Id to Check the Item Details: ")))


# Create a Python class Library with attributes like library_name, books, members, and methods like add_book, register_member, and issue_book. Tasks:
# Add new books to the library.
# Register new members.
# Issue books to members.
# Print the list of books.
# Print registered members.
# Track issued books.

class Library:
    def __init__(self,library_name,books,members):
        self.library_name=library_name
        self.books=books
        self.members=members
        self.issue={}
    def add_book(self,new_book):
        self.books.append(new_book)
        print("Books Present in the Library")
        print("-----------------------------")
        for i in self.books:
            print(i)
    def register_member(self,member_id,new_member):
        if member_id not in self.members.keys():
            self.members[member_id]=new_member
            print("Registered Members in the Library")
            print("----------------------------------")
            print("Member Id\tMember Name")
            for i,j in self.members.items():
                print(i,"\t\t",j)
        else:
            print("The Member id is already exists.")
    def issue_books(self,member_id,book):
        if book in self.books: 
            if member_id in self.members.keys():
                self.issue[book]=member_id
                print("The Book ",book," is issued to a member ",self.members[member_id])
            else:
                print("Member Id not Exists.")
        else:
            print("The Book is not exists.")
    def print_books(self):
        print("Books Present in the Library")
        print("-----------------------------")
        for i in self.books:
            print(i)
    def print_registered_members(self):
        print("Registered Members in the Library")
        print("----------------------------------")
        print("Member Id\tMember Name")
        for i,j in self.members.items():
            print(i,"\t\t",j)
    def print_issued_book(self):
        print("Books Issued to the members")
        print("----------------------------")
        print("Books\t\tMember Id\tMember Name\n")
        for i,j in self.issue.items():
            print(i,"\t",j,"\t\t",self.members[j],"\n")
lib1=Library("MEA Library",["wings of fire"],{1:"Ranjinee"})
lib1.add_book("alchemist")
lib1.register_member(1,"nahva")
lib1.issue_books(1,"wings of fire")
lib1.print_books()
lib1.print_registered_members()
lib1.print_issued_book()
        

#inheritance
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,course):
        super().__init__(fname,lname)
        self.course=course
    def display1(self):
        print(self.course,self.fname)
student1=Student("Ranjinee","R","CS")
student1.display1()

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,course):
        super().__init__(fname,lname)
        self.course=course
    def display1(self):
        super().display()
        print(self.course)
student1=Student("Ranjinee","R","CS")
student1.display1()

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,course):
        super().__init__(fname,lname)
        self.course=course
    def display1(self):
        print(self.course)
class Staff(Person):
    def __init__(self, fname, lname,department):
        super().__init__(fname, lname)
        self.department=department
    def display1(self):
        print(self.department)
student1=Student("Ranjinee","R","Python")
staff1=Staff("Nahva","C","CS")
student1.display()
student1.display1()
staff1.display()
staff1.display1()

"""Write a python program to Multilevel inheritance
This Python program defines a class hierarchy with multilevel inheritance in Python. 
Person (Base class): This class has a constructor _init_ that initializes the name and age attributes. It also has a display_info method that prints the name and age.
Student (Intermediate class): This class inherits from Person and adds a new attribute student_id. It has its constructor, which takes the name, age, and student_id as parameters. The constructor of the Student class calls the constructor of the Person class using super() to set the name and age. It also has a display_student_info method, which calls the display_info method from the Person class and adds the student_id information.
GraduateStudent (Derived class): This class inherits from Student and adds a new attribute research_topic. It has its constructor, which takes the name, age, student_id, and research_topic as parameters. The constructor of the GraduateStudent class calls the constructor of the Student class using super() to set the name, age, and student_id. It also has a display_graduate_info method, which calls the display_student_info method from the Student class and adds the research_topic information.
You create an instance of the GraduateStudent class with the name "Alice," age 25, student ID "STU001," and a research topic of "Machine Learning." Then, you call the display_graduate_info method on the graduate_student object, which prints out all the information from the base Person class, the Student class, and the GraduateStudent class, including the research topic"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    def display_student_info(self):
        super().display_info()
        print("Student Id: ",self.student_id)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id,research_topic):
        super().__init__(name, age, student_id)
        self.research_topic=research_topic
    def display_graduate_info_method(self):
        super().display_student_info()
        print("Research Topic: ",self.research_topic)
name=input("Enter Your Name: ")
while True:
    try:
        age=int(input("Enter Your Age: "))
    except:
        print("Please enter correct age (Age must be a number like 18, 19, or 20 — not 18.5.): ")
    else:
        break
student_id=input("Enter Your Student Id: ")
research_topic=input("Enter the Research Topic: ")
graduate1=GraduateStudent("Alice",25,"STU001","Machine Learning")
graduate2=GraduateStudent(name,age,student_id,research_topic)
graduate1.display_graduate_info_method()
graduate2.display_graduate_info_method()

"""Write a python program to manage a phone store (mobile shop) record using class
The Python code defines two classes: Phone and PhoneStore, allowing you to manage a phone inventory for a store. Here's a breakdown of the code:
The Phone class represents individual phones. Each phone has attributes for its brand, model, and price. The _init_ method initializes these attributes when a new phone object is created.
The PhoneStore class represents a store's inventory of phones. It has the following methods:
_init_: Initializes an empty list called inventory to store phone objects.
add_phone: Adds a phone object to the inventory list.
remove_phone: Removes a phone from the inventory based on its brand and model. If the phone is found and removed, a success message is printed; otherwise, a "not found" message is printed.
find_phone: Searches for a phone in the inventory based on its brand and model. If found, it returns the phone object; otherwise, it returns None.
display_inventory: Displays the current phone inventory, including brand, model, and price.
An instance of the PhoneStore class is created with the variable phone_store.
A menu is displayed to the user with the following options:
1. Add Phone to Inventory
2. Remove Phone from Inventory
3. Find Phone in Inventory
4. Display Inventory
5. Quit
The program enters a loop where the user is prompted to enter their choice (as a string).
Depending on the user's choice, the corresponding method of the PhoneStore instance is called to perform the desired operation. The user can add, remove, find, or display phone inventory, or quit the program.
If the user provides an invalid choice, they are notified with the "Invalid choice" message and prompted to try again.
The code converts brand and model inputs to uppercase using the .capitalize() method before storing them in phone objects and when searching the inventory. This ensures that case-insensitive matching is used when adding, removing, or finding phones.
The code allows you to interactively manage the phone inventory for a store and will continue running until the user chooses to quit (option 5)."""

class Phone:
    def __init__(self):
        self.brand=''
        self.model=''
        self.price=''
class PhoneStore(Phone):
    def __init__(self):
        self.inventory=[]
    def add_phone(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.inventory.append((self.brand,self.model,self.price))
        print("Phone is Successfully Added.")
    def remove_phone(self,brand,model):
        count=0
        for i in self.inventory:
            if i[0]==brand and i[1]==model:
                self.inventory.remove(i)
                count+=1
                break
        if count==0:
            print("The Phone is Not Found.")
        else:
            print("The Phone is Removed Successfully.")
    def find_phone(self,brand,model):
        count=0
        for i in self.inventory:
            if i[0]==brand and i[1]==model:
                count+=1
                break
        if count==0:
            print("The Phone is Not Found.")
        else:
            print("The Phone is Found.\nBrand: ",brand,"\nModel: ",model)
    def display_inventory(self):
        for i in self.inventory:
            print(i)
phone_store=PhoneStore()
while True:
    print("1. Add Phone to Inventory\n2. Remove Phone from Inventory\n3. Find Phone in Inventory\n4. Display Inventory\n5. Quit")
    choice=input("Enter your choice: ")
    match choice:
        case "1":
            phone_store.add_phone(input("Enter Brand: "),input("Enter Model: "),input("Enter Price: "))
        case "2":
            phone_store.remove_phone(input("Enter Brand: "),input("Enter Model: "))
        case "3":
            phone_store.find_phone(input("Enter Brand: "),input("Enter Model: "))
        case "4":
            phone_store.display_inventory()
        case "5":
            break
        case _:
            print("Enter a Valid Choice.")

#classmethods
class Person:
    @classmethod
    def demo(cls):
        return "hello"
Person.demo()

def demo():
    return "hello"

asd=demo
asd()
del demo
asd()
type(asd)
asd
a=12
b=12

# Polymorphism
class Person:
    count1=0
    def display(self,model):
        print("I am Person",self.count1,model)
        print(locals())
class Student(Person):
    def display(self):
        print("I am Student")
        print(globals())

person=Person()
student=Student()
person.display("hi")
student.display()
Person.count1
person.count1

count1=0
def display(count1):
        print("I am Person",count1)
        print(locals())
display(count1)

for value in [person,student]:
    value.display()




