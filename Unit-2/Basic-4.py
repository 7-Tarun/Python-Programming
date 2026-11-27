# Class, Object, Constructor (__init__) aur self

class Student:  #class
    college = "RU" #Class Variable

    def __init__(self, name):
        self.name = name    # Instance variable

    def display(self):      # Instance Method
        print(f"{self.name} {self.college}")

s1 = Student("Aman")    #object
s2 = Student("Riya")
s1.display()
print(s2.name, s2.college)


# college = "RU" → Class level pe defined—sab objects ke liye common

# class Student: → class define kar rahe hain.
# __init__() → object create hote hi automatically call hota hai;
# self.name = name → current object ke andar name variable store karta hai.
# Student("Aman") → Student class ka object create karta hai.