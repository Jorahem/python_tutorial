# names = []
# for _ in range(3):
#     names.append(input("What's your name?: "))

# for name in sorted(names):
#     print(f"hello ,{name}")
    

# name = input("What's your name?")
# file = open("names.txt","a")
# # with open("names.txt","a") as file:
# file.write(f"{name}\n")
# # file.wirte(name, "\n")
# file.close()



# #read
# with open("names.txt","r") as file:
#     for line in file:
#         print("hello,",line.rstrip())
    
names = []
with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello ,{name}")