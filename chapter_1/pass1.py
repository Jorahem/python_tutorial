x = int(input("enter any number :"))
y = int(input("enter any number :"))
print(x + y) #TODO: output

name = input("What's your name? ")
match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")