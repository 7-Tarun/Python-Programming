# Sets — Methods
# Every value in a set is unique and Mutable.
s = {10,10,20,30,20,20,40,30,50}

for item in s:
    print(item, end=" ")

print()
print(20 in s)

s.add(40)          # Single element add
s.update([50, 60]) # Multiple elements add

s.remove(20)       # Remove 20
s.discard(99)      # Remove if present; no error if absent

s_copy = s.copy() # Copy the set
s.clear()         # Empty the set