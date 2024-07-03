#obj attr > class attr
#Method in python

class student:
    def __init__(self, name, address,mark):
        self.name = name
        self.address = address

    def hello(self):
        print("Hello Mr.", self.name)
        print("Address is:", self.address)
    def get_mark(self):
        return self.mark

s = student("Kishor Bhatt", "Attriya tole")
s.hello()

print(s.get_mark())



"""
Let‘s Practice
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print("The average of marks for", self.name, "is:", avg)

s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()
