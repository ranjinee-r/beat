#list
dir(list)
fruits=["apple","banana","mango","cherry","banana","banana"]
vegetables=["onion","tomato","brinjal","potato"]
fruits[0]="watermelon"
fruits
fruits[0:4:2]
fruits
fruits.append("kiwi")
fruits
fruits.clear()
fruits
fruits_copy=fruits.copy()
fruits_copy
fruits.count("banana")
fruits.append(vegetables)
fruits
fruits.extend(vegetables)
fruits
fruits.index("banana")
fruits.insert(5,"watermelon")
fruits
fruits.pop(0)
fruits
fruits.remove("banana")
fruits
fruits.reverse()
fruits
fruits.sort()
fruits
fruits.reverse()
fruits.pop()



#examples of for loop without range
for fruit in fruits:
    print(fruit)


#examples of for loop with range
for fruit in range(0,len(fruits)):
    print(fruits[fruit])


