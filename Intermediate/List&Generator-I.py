'''

List comprehension uses memory.
Generators don't use memory.

'''

# Generators
xyz = (i for i in range(5))
print(xyz)

# list comprehension
xyz = [i for i in range(5)]
print(xyz)