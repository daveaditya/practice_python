class Girl:
    gender = "female"   # class variable. It is not unique among objects

    def __init__(self, name):
        self.name = name    # instance variable. Unique among objects

    def get_name(self):
        print(self.name)


g1 = Girl("hel")
g1.get_name()
print(g1.gender)