list=["blue","he","green","black","is","red","pink","yellow","a","b"]
one=[]
two=[]
three=[]
four=[]
five=[]
others=[]
for word in list:
    if len(word)==1:
        one.append(word)
    elif len(word)==2:
        two.append(word)
    elif len(word)==3:
        three.append(word)
    elif len(word)==4:
        four.append(word)
    elif len(word)==5:
        five.append(word)
    else:
        others.append(word)
one
two
three
four
five
others
