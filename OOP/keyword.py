#del keyword
#del s1.name
#del s1 

# class Student:
#     def __init__(self ,name):
#         self.name = name

# s1 = Student("shardhha")
# print(s1.name)
# #del keyword
# # del s1.name
# print(s1.name)


#private and protected
# private attribute & methods are meant to be used only within the class and are not accessible 
#it is not properly right to do
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass


    def reset_password(self):
        print(self.__acc_pass)

acc1 = Account("12342","0000099")
print(acc1.acc_no)
acc1.reset_password()


#<----------------------Inheritance ------------------------>
class Parent:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(self.name,self.age)

c1 = Child("prinkya chudhary",20)
c1.show()

#types of inheritance
#single inheritance
#example
class Car:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class BMW(Car):
    def __init__(self,name,color,price):
        super().__init__(name,color)
        self.price = price

    def show(self):
        print(self.name,self.color,self.price)

b1 = BMW("BMW","red",1000000)
b1.show()

#multilevel inheritance
#multiple inheritance
print("\nmultiple inheritance")
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")


class C(B):
    def show(self):
        print("in C show")


c1 = C()
c1.show()

#<----------------Super Method()------------------->
print("\nSuper Method()")
class A:
    def show(self):
        print("hey A class show")

class B(A):
    def show(self):
        super().show()
        print("Hey B class show")
        
class C(B):
    def show(self):
        super().show()
        print("Hey C class show")


c1 = C()
c1.show()


  


