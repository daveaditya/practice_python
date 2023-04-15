input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    if num % 5 == 0:
        return True
    return False

# Here xyz is a generator
xyz = (i for i in input_list if div_by_five(i))
print(type(xyz))

# One line for loops
[print(i) for i in xyz]
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)

