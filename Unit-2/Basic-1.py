# Tuples — Immutable
# Tuples also store multiple values, but once created, their elements cannot be modified.

coords = (12, 24, 36)
colors = ("Red", "Green", "Blue")

#Tuple Unpacking
x,y,z = coords
print(y)

#Membership Check
print(12 in coords)
print(25 in coords)

print(colors[1])
# colors[1] = "Yellow"    -Error
print(colors)