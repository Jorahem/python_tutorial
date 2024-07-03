#function is block of statements that perform a specific task.
#def la 
#def function_name(parameters):
    #body of function
    #return [expression]

#function definition
def add(a,b): #a,b are parameters
    sum=a + b #body of function
    print("The sum of two number :",sum) #return statement
    return sum 

#function call
add(10,20)
add(5,5)

# def love():
#     print("I love You")
# i=5
# for i in range(9):
#     love()


#built in function 
print("Hem jora is using built in function......" , end="") #sep=""
print("ok I am enjoying it")#end= "\n"
#len()
print(len("Hem jora"))

def cal_prod(a=1 , b=1):
    print(a*b)
    return a*b
cal_prod()


#*************Recursion**********************
print("\n")
print("Recursive Function")
def show(n):
    if(n == 0): # < base case vanxan yo layee >
        return 
    print(n)
    show(n-1)
show(5)    
print("\n")


#Question factorial number
print("<<< Factorial number >>>")
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n  * fact(n-1)
print(fact(5))




