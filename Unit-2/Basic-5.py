# Inheritance

class Animal:
    def speak(self):
        print("Some Sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

a = Animal()
b = Dog()

a.speak()
# a.bark()
b.speak()
b.bark()