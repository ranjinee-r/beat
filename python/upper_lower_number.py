#append uppercase, lowercase, numbers from a string into seperate lists
dir(str)
upper=[]
lower=[]
number=[]
others=[]
string="RaNjInEe@17"
for char in string:
    if char.isupper():
        upper.append(char)
    elif char.islower():
        lower.append(char)
    elif char.isnumeric():
        number.append(char)
    else:
        others.append(char)

upper
lower
number
others