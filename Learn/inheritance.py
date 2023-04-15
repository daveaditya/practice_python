class Parent:

    def last_name(self):
        print("dave")


class Child(Parent):

    def first_name(self):
        print("aditya")

    def last_name(self):
        print("changed")

i = Child()
i.last_name()
i.first_name()
print(type(i))
