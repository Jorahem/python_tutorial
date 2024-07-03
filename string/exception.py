# try:
#     x = int(input("enter any number:"))
# except ValueError:
#     print("It's is not integer")

# else:
#     print("you entered", x)

def main():
    x =get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass
main()