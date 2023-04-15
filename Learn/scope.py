a = 1234

def first():
    b = 789
    print(a)
    print(b)

def second():
    print(a)
    # Variable b is not accessible as it is not in the scope of the function
    # print(b)

first()
second()
