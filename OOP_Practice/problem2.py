"""
 Write a  Python program to create a person class. 
 Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def age(self , age):
        print(f"\nMy Name is {self.name}")
        print(f"I am from {self.country}")
        print(f"I am {age} years old")
        print(f"I was born on {self.dob}")


name = input("Enter your name : ")
country = input("Enter your country : ")
dob = input("Enter your date of birth : ")
age = int(input("Enter your age : "))
info = Person(name,country,dob)
info.age(age)