#Dictionary Operations
student = {"name":"Jaanhavi",
           "age":18,
           "branch":"Computer Engineering"}
print("Original Dictionary:",student)

student["college"]="ABC College"
print("After adding an element:",student)

student["age"]=19
print("After updating age:",student)

student.pop("branch")
print("After removing branch:",student)

student.popitem()
print("After popitem():",student)

print("Keys:",student.keys())
print("Values:",student.values())

#Tuple Operations
numbers=(10,20,30,40,50)
print("\nOriginal Tuple:",numbers)

print("First element:",numbers[0])

numbers=numbers + (60,)
print("After adding an element:",numbers)

temp=list(numbers)
temp.remove(30)
numbers=tuple(temp)
print("After removing 30:",numbers)

print("length of tuple:",len(numbers))

print("Maximum:", max(numbers))
print("Minimum:",min(numbers))
