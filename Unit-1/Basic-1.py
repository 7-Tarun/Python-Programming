# Floor Division (//) and Modulo (%)

print(5 // 2)    # 2  -> Quotient
print(5 % 2)     # 1  -> Remainder

print(-5 // 2)   # -3 -> Floor towards negative infinity
print(-5 % 2)    # 1  -> Remainder follows divisor's sign

print(5 // -2)   # -3
print(5 % -2)    # -1

print(-5 // -2)  # 2
print(-5 % -2)   # -1

#Guess the output:
print(7 % -3)

#Python uses this formula: a % b = a - (a // b) * b