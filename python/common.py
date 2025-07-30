l1=[1,4,3,6,2]
l2=[2,5,4,7,8]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
l3

l1=[1,4,3,6,2]
l2=[2,5,4,7,8]
l3=[]
i=0
while i<len(l1):
    j=0
    while j<len(l2):
        if l1[i]==l2[j]:
            l3.append(l1[i])
        j+=1
    i+=1
l3

#function
def common(l1,l2):
    l3=[]
    i=0
    while i<len(l1):
        j=0
        while j<len(l2):
            if l1[i]==l2[j]:
                l3.append(l1[i])
            j+=1
        i+=1
    l3


common([1,4,3,6,2],[2,5,4,7,8])






l1=[1,2,3,4,5]
l2=[3,4,5,6,7,8]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
l3