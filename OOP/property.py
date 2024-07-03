class Student:
    def __init__(self, phy, chem, math):
        self.phy= phy
        self.chem = chem
        self.math = math
        # self.percentage = str(self.phy + self.chem + self.math

    @property
    def percentage(self):
      return str((self.phy + self.chem + self.math)/3) + "%"
stu1 = Student(67,89,90)
print(stu1.percentage)

stu1.phy= 70
print(stu1.percentage)