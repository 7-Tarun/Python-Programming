# Polymorphism — Method Overriding
# Polymorphism ka basic practical example: same method name, different behaviour.


class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):  # Overriding
        print("Bark")

a = Animal()
d = Dog()

a.speak()
d.speak()
