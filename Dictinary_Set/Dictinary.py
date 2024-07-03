"""

Dictionaries are used to store data values in key:value pairs
“key” : value
They are unordered, mutable(changeable) & don’t allow duplicate keys
dict[”name”], dict[”cgpa”], dict[”marks”]
dict[”key”] = “value” #to assign or add new

"""

info = {
    "name":"Hem Jora",
    "Age":21,
    "class":"BIM",
    "Email":"Jorahem3@gmail.com"
}
# info["name"] = "smritty kc"
# print(info)


#nested dictionary
teacher_name = {
    "name ": "Yub Raj Hamal",
    "age":39,
    "Subject":{
        "Class_8":"Optional Math",
        "Class_9":"Mathematic",
        "Class_10":"Geometry"
    },
    "Address":"Santosh_tole"
}


# print(teacher_name)
# print(list(teacher_name))
# print(teacher_name.keys())
# print(teacher_name.values())

# info.update({"name":"smritty kc"})
# print(info)


#set
# num1 = set()
# num1.add(1)
# num1.add(2)
# num1.add(2)
# print(num1)
# num = {1,2,3,4,5,"Hem ", "jora","Hem"}
# print(num)
# print(len(num))
# print(type(num))

# 1. Sets - They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed
{'orange', 'banana', 'pear', 'apple'}
a = set('abracadabra')
print(a) # unique letters in a {'a', 'r', 'b', 'c', 'd'}
a.add('z')
print(a) 
# {'a', 'c', 'r', 'b', 'z', 'd'}
# 2. Frozen Sets - They are immutable and new elements cannot added after its defined.
b = frozenset('asdfagsa')
print(b)
frozenset({'f', 'g', 'd', 'a', 's'})
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)
frozenset({'Frankfurt', 'Basel', 'Freiburg'})