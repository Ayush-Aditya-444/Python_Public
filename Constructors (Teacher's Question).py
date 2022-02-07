from unicodedata import name


class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, my name is {self.name}")
person1=Person("Ayush Aditya")
person1.talk()
person1=Person("Ragini Rani")
person1.talk()