#Qestion 1.wrte a recursive function to calculate the sum of first n natural number 
def calc_sum(n):
    if(n ==0):
        return 0
    else:
        return calc_sum(n-1) + n
print(calc_sum(5))

a = [1,3,5]
b = [1,2,6,1000]
print(a>b)
print("hello" *3)