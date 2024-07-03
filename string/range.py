#Question
#1.Print numbers from 1 to 100.
# for i in range(1,101):
#  print(i)

 #2.Print numbers from 100 to 1.
# for i in range(100,0,-1): #(start, stop , step )
#   print(i)


#3.Print the multiplication table of a number n.
# n = int(input("Enter any number :"))
# i=1
# for i in range(1,11,1):
#     print(n*i)



#3.Wap to find sum of n natural number 
n = 5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum :-",sum)


#wap to find factorail number 
n = 5
fac = 1
for i in range(1,n+1):
    fac = fac * i
print("Factorial :-",fac)
