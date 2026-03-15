 #Dictionary Operations

student = {"name" : "Nilutpal",
        "age" : 20,
        "course":"Python"}
print(student)

#Accessing Values
print(student["name"])
print(student.get("age"))

#Adding Elements
student["city"] = "Pune"
print(student)

#Updating Values
student["age"] = 21
print(student)

#Dictionary Length
print(len(student)) 

#Iterate Through Keys
for key in student:
    print(key)

#Deleting Elements
del student["course"]   #Using del (specific)
print(student)

student.pop("age")      #Using pop() ()
print(student)

student.clear()         #Using clear() (removes all items)
print(student)

#Copying Dictionary
new_dict = student.copy()
print(new_dict)
 