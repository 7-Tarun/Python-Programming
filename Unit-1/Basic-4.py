# Conditions and Loops

marks = int(input("Enter Your Marks: "))

if marks >= 75:
    print("Distinction")
elif marks >=50:
    print("Pass")
else:
    print("Fail")

# for loop + range(start, stop, step)
for i in range(0,6):
    print(i, end=" ")

print()

for i in range(10, 0, -2):
    print(i, end=" ")

print()

for i in range(1, 10, 2):
    print(i, end=" ")



for i in range(1, 8):
    if i == 3:
        continue   # 3 skip hoga
    if i == 6:
        break      # 6 pe loop ruk jayega (6 aur 7 print nahi honge)
    if i == 4:
        pass       # placeholder
    print(i, end=" ")
# Output: 1 2 4 5