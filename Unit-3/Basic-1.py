#Looping, Sorting & Nested Dictionaries
marks = {"Python": 80, "DSA": 85, "Maths": 95}

# 1. Looping
for sub, score in marks.items():
    print(f"{sub}: {score}")

# 2. Sorting
byKey = dict(sorted(marks.items()))
byVal = dict(sorted(marks.items(), key=lambda x: x[1]))
print(f"Sorted by Key: {byKey}")
print(f"Sorted by Value: {byVal}")

# 3. Nested Dictionary
records = {
    101: {"name": "Tarun", "marks": 85},
    102: {"name": "Lokhand", "marks": 67}
}

print(records[101]["name"])
print(records[102])