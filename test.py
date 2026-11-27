class Variable:     #class
    college = "RU"      #Class variable

    def __init__(self, roll, name):
        self.roll = roll    #Instance variable
        self.name = name

    def display(self):      #Instance Method
        print(f"{self.roll} {Variable.college} {self.name}")

s1 = Variable(21,"Rohan")       #Object
s1.display()