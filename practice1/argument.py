a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = a[::2]
print(odd_numbers)

"""
get the list of value of dict in sorted way dict = {'c': 97, 'a': 96, 'b': 98}

"""
dict = {'c': 97, 'a': 96, 'b': 98}
new_dict = sorted(dict.values())
print(new_dict)
# Creating a dictionary with integer keys
integer_keys_dict = {
    1: 'apple',
    2: 'banana',
    3: 'cherry',
    4: 'date',
    5: 'elderberry'
}

# Printing the dictionary
print(integer_keys_dict)

# print(integer_keys_dict['apple']=1)
new_integer = {value:key for key, value in integer_keys_dict.items()}
print(new_integer)