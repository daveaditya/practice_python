def can_vote(age):
    if age>18:
        return "yes"
    else:
        return "no"

print("My age is 21. Can I vote? " , can_vote(21))
