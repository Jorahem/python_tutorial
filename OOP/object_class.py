#class is a blueprint for creationg objects.

class detail:
    name="Hem Jora"
s =  detail()
print(s.name)

class Car:
    color = "blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

#constuctor all classess have a function _init_() which is always executed
class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print("Creating new student")

s1 = student("Hem shahneroshah",88)
print(s1.name)
print(s1.mark)

s2 =student("Arjun",76)
print(s2.name)
print(s2.mark)