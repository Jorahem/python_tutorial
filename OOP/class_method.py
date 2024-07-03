class Person :
    name ="Hem"

    @classmethod
    def changeName(cls,name):
     cls.name= name

p1 = Person()
p1.changeName("anju rawal")
print(p1.name)
print(Person.name)