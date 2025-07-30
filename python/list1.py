dir(list)
fruits=["apple","mango","orange","apple","kiwi","watermelon"]
fruits.append("jackfruit")
fruits
copy_fruits=fruits.copy()
copy_fruits
fruits.count("cherry")
vegetables=("onion","tomato")
fruits.extend(vegetables)
fruits
fruits.index("kiwi")
fruits.insert(2,"kiwi")
fruits
fruits.pop(7)
fruits
fruits.remove("kiwi")
fruits

for i in fruits:
    print(i,end=",")
fruits

for i in range(0,len(fruits)):
    print(fruits[i])


list1=[("Iphone","15",200000),("Poco","M4 Pro",20000)]
brand="Iphone"
model="15"
if zip(brand,model) in list1:
    print("Yes it is in")
else:
    print("no")