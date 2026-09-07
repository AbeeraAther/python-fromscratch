#creating Person class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("Hiiii my name is", self.name, "and my age is", self.age)

    def vote(self):
        if self.age >= 18:
            print("I am eligible to vote.")
        else:
            print("I am not eligible to vote.")


P1 = Person("Abeera", 19)
P2 = Person("Aisha", 17)
P1.talk()
P1.vote()
P2.talk()
P2.vote()
