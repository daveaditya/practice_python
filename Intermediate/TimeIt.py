import timeit

# Runs the statement number times...
# print(timeit.timeit('1+3', number=500000000))

input_list = range(100)


def div_by_five(num):
    return num % 5 == 0

generator = (i for i in input_list if div_by_five(i))

listcomprehension = [i for i in input_list if div_by_five(i)]