def something(first="hello",second="world",third="bye"):
    print(first + " " + second + " " + third)

# Keyword arguments allow unordered parameter passing,
# and only selected parameter specification
something()
something(second="human")
something(first="wow",third="human")
something(third="goodbye",first="human")
