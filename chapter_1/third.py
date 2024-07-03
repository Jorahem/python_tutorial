name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
# name = name.title()
name = name.capitalize()

# Print the output
print(f"hello, {name}")

name = input("What's your name? ")
print("hello,", end="")
print(name)