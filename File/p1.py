#question 1. 
"""
Create a new file “practice.txt” using python. Add the following data in it:
WAF that replace all occurrences of “java” with “python” in above file.
Search if the word “learning” exists in the file or not.
Hi everyone
we are learning File I/O
using Java.
I like programming in Java
"""
# file = open("file/practice.txt","x")
# print("sucessfully created")

# file = open("file/practice.txt","w")
# data = file.write("hello everyone \n we are learning File I/O \n using Java \n I like programming in Java ")
# file = open("file/practice.txt","r")
# print(file.read())



#Question 2.WAF that replace all occurrences of “java” with “python” in above file
# file = open("file/practice.txt","r") 
# data = file.read()
# new_data = data.replace("Java","python")
# print(new_data)
# with open("file/practice","w") as f:
#     f.write(new_data)



#Question 3. Search if the word “learning” exists in the file or not.
# with open("file/practice.txt", "r") as f:
#     data = f.read()
#     if(data.find("learning")):
#         print("found")
#     else:
#         print("not found")


        


#Question 4.WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

def check_for_line():
    
        word ="learning"
        data=True
        line=1
        with open("file/practice.txt", "r") as f:
             while data:
               data = f.readlines()
               if word in data:
                 print(line)
                 return 
             line+=1
               
        return -1
            

print(check_for_line())

#Question 5. From a file containing numbers separated by comma, print the count of even numbers.

with open("file/practice.txt") as f:
    data = f.read()
    count=0
    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count+=1
    print(count)