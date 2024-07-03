detail = {
    "name": "Hem Jora",
    "subject":["c","PHP","python","java"],
    "topic":("dict","set"),
    "age":21,
    "marks":90.3
}
print(detail)
#we can upate but we can not add new key
detail["name"] = "Hem Jora"
detail["subject"].append("c++")
#nested dictionary 

student = {
    "name":"Rahul sodhi",
    "subject": {
        "phy":67,
        "c":45,
        "python":44
    },
    "email":"shahnero12@gmail.com"
}
print(student["subject"])

#method 
# 1.Key
print(student.keys())

print(len(list(student.keys())))


# 2. values
print(student.values())

# 3. items
print(student.items())
#type cast
print(list(student.items()))


# 4.get
print(student.get("name"))

# 5.update
student.update({"city":"ktm"})
print(student)

#set is the collection of the unordered items
num = {1,2,3,4,3,4,5}
print(type(num))
print(len(num))
#unique value hunxan yo set ma 

col = {} #empty dictionary
col = set() #empty set 
print(num.add(9))
print(num)

num.remove(9)
print(num)

num.pop()
print(num)

#practice la
det = {
    "table":["a piece of furniture "," list of facts & figures"],
    "cat":"A small animal"
}



#2

"""
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”
,“java” ,“C++”
,“python”
,“javascript”
,“java”
,“python”
,“java”
,“C++”
,“C”
"""
subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(type(subject))
print("Total number of classrom is required ",len(subject))

