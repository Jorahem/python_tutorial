# class Person:
#       def __init__(self, firstname, lastname, age, country, city):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city


# p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)

# import random
# from random import choice

# coin = choice(['head','tail'])
# print(coin)

class Bachelor:
    def __init__(self, name, location,faculty):
        self.name = name
        self.location = location
        self.faculty = faculty
    def college(self):
        print("Your College name:",self.name)
        print("location:",self.location)
        print("faculty:",self.faculty)

    # def Bbs(self):
    #     print("Name:",self.name)
    #     print("location:",self.location)
    #     print("faculty:",self.faculty)

# college = spa("sudur Paschimanchal Academy","Santoshi_tole","Bachelor in Information Management")
# college.Bim()
# print("\n")
# college1 = spa("Kailali Multiple Campus","Campus road","Bachelor in Business study")
# college1.Bbs()



college_name = input("Enter your college name : ")
location = input("Enter your college loaction: ")
faculty = input("Enter your faculty name: ")
coll = Bachelor(college_name,location,faculty)
coll.college()
