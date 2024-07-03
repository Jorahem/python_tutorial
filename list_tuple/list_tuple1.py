#Wap to find given list is palindrome or not 
list = [1,2,1]
list_copy = list.copy()
list_copy.reverse()
if ( list == list_copy):
    print("the list is palindrome ")
else:
    print("list is not palindrome")



#touple Wap to count the number of students with the "A" grade in the following tuple
grade = ("c","D","A","B" ,"A", "B")
print(grade.count("A"))
# print(grade.index("A"))

grade = ["c","D","A","B" ,"A", "B"]
grade.sort()
print(grade)
