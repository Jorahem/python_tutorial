#read
# file = open("File/demo.txt","r")
# print(file.read())

# #readline
# file = open("File/demo.txt","r")
# print(file.readline())


#write file
# file = open("File/demo.txt","w")
# file.write("Hello World")
# file.close()



#append file
# file = open("File/demo.txt","a")
# file.write(" \n ok I am learnnig and going well thank buddy ")
# file.close()


#r+
# file = open("File/demo.txt","r+")
# file.write(" \n abc ")
# file.read()
# file.close()

# with open("file/demo.txt","r") as f:
#     data = f.read()
#     print(data)


# with open("file/demo.txt","w") as f:
#     data = f.write("Hello guys")
#     print(data)

with open("file/names.txt" ,"w") as f:
    data = f.write("jora file la")
    print(data)