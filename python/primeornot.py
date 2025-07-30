num=2
if num==2:
    print("prime")
else:
    for i in range(2,num//2+1):
        if num%i==0:
            break

    if i==num//2:
        print("prime")
    else:
        print("not prime")