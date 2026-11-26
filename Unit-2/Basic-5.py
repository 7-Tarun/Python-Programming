# Inheritance

class Animal:
    def speak(self):
        print("Some Sound")
        print(self.name)

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Bark")
        # print(self.name)

    def __init__(self, name):
        super().__init__(name)

a = Animal("Murti")
b = Dog("Pandayan")

a.speak()
# a.bark()
b.speak()
b.bark()