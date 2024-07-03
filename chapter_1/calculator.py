# print("Calculator:")
# f = int(input("Enter first number:"))
# operator = input("Enter operator + , - , * , / , %, ** : ")
# s = int (input("Enter second number :"))

# if operator == "+":
#     print("Sum: ",f+s)

# elif operator == "-":
#     print("Difference: " , f-s)   

# elif operator =="*":
#     print("Multiplication:",f*s)

# elif operator == "/":
#     print("Division:",f/s)

# elif operator == "%":
#     print("Modulus:",f%s)

# elif operator == "**":
#     print("Exponent:",f**s)

# else:
#     print("Invalid operator")


    #condition statement
    #indentation ':' 
    #if , elif , else
    #if condition:
    #    statement
    #elif condition:
a, b, c = 10, 15, 5

if a > b or a > c:
    print("A is the greatest number")
elif c > a or c > b:  # Corrected the condition to compare c with a and b
    print("C is the greatest number")
else:
    print("B is the greatest number")
