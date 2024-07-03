marks = [12,34,56,76,54,32,12,67]
print(marks)
print(type(marks))

#use can use list to store any data type
# varibe = ["shradha ",56,"jora",45.6,"singh"]
# print(varibe)

"""
-> String are immutable
-> List are mutable
"""

#list slicing

#same rule which we have study in string 
#syntax : list_name[starting_idx:ending_idx] -> ending idx is not included

# print(marks[0:6])

#list method
#append()
#insert()
#remove()
#pop()
#clear()
#copy()

#1.append
list = [5,2,4,1,7,8,9,5]
# list.append(3)
# print(list)


#2.sort
# list.sort()
# print(list)

#3.Reverse
# list.sort(reverse=True)
# print(list)

#another method
# list.reverse()
# print(list)

#4.insert
# list.insert(5,10)
# print(list)

# #remove
# list.remove(10)
# print(list)

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
list = []
n1 = input("Enter your first favorite Movie name: ")
n2 = input("Enter your second favorite Movie name: ")
n3 = input("Enter your third favorite Movie name: ")

list.append(n1)
print(list)
