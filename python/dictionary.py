#dictionary
dir(dict)
fruits=["apple","banana","mango","cherry","banana","banana"]
dict={"name":"ranjinee","age":21}
dict.get("name")
dict.items()
dict.keys()
dict.pop("name")
dict
dict["name"]="Ranjinee"
dict["age"]=21
dict["place"]="Mannarkkad"
dict
dict.popitem()
dict
dict2={}
dict2=dict.fromkeys(fruits)
dict2
dict.update({"name":"nadiya"})
dict
dir(dict)


dict1={"name":"ranjinee","age":21}
list1=["name","age","address"]
list(dict1.keys())
if dict1.keys() in list1:
    print(dict1.keys())
dict1={1:{"idly":2,"dosa":3}} 
dict1.items()
dict1
dict1[1]["idly"]