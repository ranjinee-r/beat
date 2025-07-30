def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()


def calc(func):
    def sum():
        list1=[1,2,3,4,5,10]
        sum1=0
        for i in list1:
            sum1+=i
        print(sum1)
        func()
    return sum

def multiply():
    list1=[1,2,3,4,5,10]
    pro=1
    for i in list1:
        pro*=i
    print(pro)
    
multiply()

multiply=calc(multiply)
multiply()

@calc
def multiply():
    list1=[1,2,3,4,5,10]
    pro=1
    for i in list1:
        pro*=i
    print(pro)





