#string in python

#Basic Operation
#1.Concatenation
# fname = "Hem"
# lname = "Jora"
# print(fname + " " + lname)



# #length
# str = "My name is Hem Jora"
# print("The length of string ",len(str))


#indexing 
# A p n a _ C o l l e g e
# 0 1 2 3 4 5 6 7 8 9 10 11
# str = "Apana_College"
# print(str[0])
# print(str[5])


#Slicing
# nam = "Dhangadhi"
# print(nam[1:4]) #output->han


"""
Slicing
A p p l e
-5 -4 -3 -2 -1

str =“Apple”
str[ -3 : -1 ] is “p

"""

# String Function
#1.lower()
#2.upper()
#3.title()
#4.count()
#5.find()
#6.replace()
#7.split()

#endswith
str = "I am studying python from apna college"
print(str.endswith("ege"))


#capitalize
str = "i am studying python from apna college"
print(str.capitalize())

#replace
str = "i am studying python from apna college"
print(str.replace("python","java"))

#find
str = "I am stuying python from apana college"
print(str.find("s"))

#count
str = "I am studying python from apna college"
print(str.count("a"))



#Question
#1.WAP to input user's first name & print its length
# fname = "Kishor"
# fname = input("Enter your first name :")
# print("The lenth of user first name is :",len(fname))


# #2.WAP to find occurrence of '$' in a string
# dollar = "Yesterday my friend send me $100 from USA"
# print(dollar.find("$"))



#3.WAP to check if a number entered by the user is odd or even.
# number = int(input("Enter any number "))
# if number%2 == 0:
#     print(number , ": Is a Even number ")
# else:
#     print(number, " :Is a Odd number ")




#4.WAP to find the greatest of 3 numbers entered by the user.
# x = int(input("Enter first number "))
# y = int(input("Enter second number "))
# z = int(input("Enter third number"))
# if x>y and x>z:
#     print(x ,":is greastest number")
# elif y>x and y>z:
#     print(y,":is greastest number ")
# else:
#     print(z,":is greastest number")


    #5.
mul = int(input("Enter any number :"))
if (mul%7 == 0):
        print(mul, ":is multiple of 7")
else:
        print(mul, ":is not multiple of 7")