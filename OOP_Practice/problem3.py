"""
Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

"""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Addition(self):
        return self.num1 + self.num2
    def Subtraction(self):
        return self.num1 - self.num2
    def Multiplication(self):
        return self.num1 * self.num2
    def Division(self):
        return self.num1 / self.num2
n1 =int(input("Enter 1st number:.."))
n2 =int(input("Enter 2nd number:.."))
math = Calculator(n1,n2)
print("Addition: ",math.Addition())
print("Subtraction: ",math.Subtraction())
print("Multiplication: ",math.Multiplication())
print("Division: ",math.Division())
