magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print(n," is magic number")
        break
    else:
        print(n)

for n in range(101):
    if n%4 is 0:
        print(n," is divisible by 4.")
