#Question 1. WAP to print the length of a list(list is the parameter)
citis = ["delhi","gurgaon","pune","mumbai","chennai"]
def print_len(list):
    print(len(list))
print_len(citis)

#Question 2. WAP to print the list in a single line (list is the parameter)
def print_list(list):
    for item in list:
        print(item,end=" ")


print_list(citis)

print("\n")
#Wap to find factorail number of n 
def factorial_num(n):
    num=1
    for i in range(1,n+1):
        num = num*i     
    return num 
check = factorial_num(5)
print("The factorial :",check ,end ="\n")


#wap to convert usd in npr
def usd_to_npr(usd):
    npr_val = usd * 132
    print(usd , "USD = ", npr_val,"NPR")

usd_to_npr(100)

#WAP to find given number is 
def check(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
num = int(input("Enter any random number :"))
check(num)


