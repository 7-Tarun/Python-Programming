#Dictionaries (Code Essentials) Dictionary key: value pairs store karti hai { } ke andar.

student = {"name": "Tarun", "roll": 20, "sem": 5}

#Access
print(student["name"])
print(student.get("branch","BCA"))

#Add / Update / Delete
student["city"] = "Jaipur"      #Add
student["roll"] = 21            #Existing update
removed = student.pop("sem")    #Deletes the key and returns the value.
print(removed)
print(student)