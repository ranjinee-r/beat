name1="Cart"
name2="catr"
count=0
name3=name1.upper()
name4=name2.upper()
if len(name3)==len(name4):
    for i in name3:
        for j in name4:
            if i==j:
                count=count+1
                break
        
else:
    print("Not Anagram")

if count==len(name1):
    print(name1+" and "+name2+" is anagram")
else:
    print("Not Anagram")