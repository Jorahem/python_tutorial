#type casting


a, b = 1, 2.0
sum = a + b

#error
# a, b = 1, "2"
# sum = a + b

# a,b = 1,"5"
# c= int(b)
# sum = a + c
# print(sum)


#input
# name = input("Enter your name please:-")
# age = int(input("Enter your name:-"))
# print("Hello " + name)
# print("Age is:-",age)

#Let‘s Practice
#Write a Program to input 2 numbers & print their sum.
# a = int(input("Enter first number:-"))
# b = int(input("Enter second number:-"))
# sum = a + b
# print("Sum of two number :-",sum)




# # WAP to input side of a square & print its area.
# side = int(input("Enter the side of square"))
# area = side * side
# print("The Area of square is :-",area)



# WAP to input 2 floating point numbers & print their average.
# num1 = float(input("Enter first float number :- "))
# num2 = float(input("Enter second float number :- "))
# sum = num1 + num2
# avg = sum/2
# print("The Average of two number is :-",avg)



# WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if a > b : 
    print("True")
else:
   print("False")
