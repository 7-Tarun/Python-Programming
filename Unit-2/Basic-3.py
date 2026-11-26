# Sets — Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union: All unique elements from both sets. Method: a.union(b)
print(a.union(b))
print("Union: ",a | b)

# Intersection — Common elements in both. Method: a.intersection(b)
print("Intersection: ",a & b)

# Difference — It is in A, but not in B. Method: a.difference(b)
print("Difference: ",a - b) 