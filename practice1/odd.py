
def odd_number(n):
    odd_n = []
    for i in n:
        if i%2 == 1:
            odd_n.append(i)
    return odd_n


number = [1,3,4,55,66,8,9,111,222,11]
result = odd_number(number)
print(result)