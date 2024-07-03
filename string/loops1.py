# i = 5
# while i>0:
#     print("Meow")
#     i-=1
i = 0
for i in range(5):
    for j in range(i+1):
        print("*")
        j+=1
    
    i+=1
