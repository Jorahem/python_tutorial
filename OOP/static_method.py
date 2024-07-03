#static ma self lekhanu pardaii na nii
#methods that don't use the self parametere

class student:
    @staticmethod
    def hello():
     print("Hello world!")
s = student()
s.hello()

#Pillar of oops
#Encapsulation
#Abstraction
#Inheritance
#Polymorphism


#1.Abstraction
#Hiding the implementation detail of a class and only showing the essential feature to the  user

class car:
   def __init__(self):
      self.acc = False
      self.brake=False
      self.clutch = False
      
   def start(self):
      self.clutch = True
   def stop(self):
       self.brake = True

s = car()
s.start()


#2.Encapsulation : Wrapping data and function into a single unit (object)

#practice Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Bank:

   def __init__(self, balance, account_no):
      self.balance = balance
      self.account_no = account_no

   def debit(self, amount):
      self.balance -= amount
      print("RS", amount, "was debited")
      print("Total balance =", self.get_balance())

   def credit(self, amount):
      self.balance += amount
      print("RS", amount, "was credited")
      print("Total balance =", self.get_balance())

   def get_balance(self):
      return self.balance

acc1 = Bank(1000, 12345)
acc1.debit(1000)
acc1.credit(500)

print(acc1.get_balance())
