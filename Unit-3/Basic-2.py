# 1. File Modes & `with` Statement (Exam Favorite)
# The open(filename, mode) function is used to open a file.
#
# 'r' (Read): Default mode. Raises FileNotFoundError if the file does not exist.
# 'w' (Write): Creates a new file or overwrites existing data.
# 'a' (Append): Adds data to the end without deleting existing data.
#
# Best Practice (`with` statement):
# Automatically closes the file when the block ends.
# No need to call f.close() separately.

#Writing on a file
with open("sample.text", "w") as f:
    f.write("Python Practical Unit-3\n")
    f.writelines(["Line 2: File Handling\n", "Line 3: Learning Khatarnak"])

    print("File Name: ", f.name)
    print("Mode: ", f.mode)
    print("Is Closed inside: ", f.closed)

print("Is Closed inside: ", f.closed)       #'with' block has closed.