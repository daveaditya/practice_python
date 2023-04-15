def add_number(*nums):
    total = 0
    print(type(nums))
    for n in nums:
        total += n
    return total

print(add_number(1,2))
print(add_number(1,2,3))
print(add_number(10,2,0,30,40,50))
