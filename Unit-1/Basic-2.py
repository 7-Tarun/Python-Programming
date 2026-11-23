x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print(f"X = {x}, Y = {y}")
x, y = y, x
print(f"X = {x}, Y = {y}")

print(f"Power: {x**y}")
print(f"Floor Division: {x//y}")
print(f"Remainder: {x%y}")

num = int(input("Enter a Number: "))
print(f"{divmod(num, 2)}")

c = input("Enter a Sentence: ")
d = input("Enter a character: ")
print(f"Is '{d}' is in '{c}' ? {d in c}")


"""
~Useful Built-in Functions for Numbers: 
abs(x) -> absolute value (abs(-7) -> 7)

round(x, n) -> n decimal places tak round off (round(3.14159, 2) -> 3.14)

pow(x, y) -> same as x ** y

divmod(a, b) -> (a // b, a % b) dono ek saath deta hai

max(a, b, ...), min(a, b, ...) -> sabse bada / chhota value
"""


"""
~Membership & Identity (Python ke special operators):

in / not in: kya koi character/value kisi sequence mein hai? ("a" in "cat" -> True)

is / is not: kya do variables same memory object ko point kar rahe hain?
"""