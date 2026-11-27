# Lists — Mutable
# A list is a collection in which you can store multiple values, and can also change them later.

num = [10, 20, 30.12, 40, 12.5]
num.append(50)
num.insert(2,70)
num.remove(20)

print(num[2])
print(num)
print(num.pop())
print(num)
num.sort()
num.append("Rahul")
print(num)

print(20 not in num)
print(20 in num)

# nums.sort()       # Modifies the original list and returns nothing (None);
# sorted(nums)      # Returns a new sorted list.