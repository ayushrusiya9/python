#Access the value of key 'city' from a dictionary:
#    student = {'name': 'Aashu', 'age': 22, 'city': 'Bhopal'}

student = {'name': "Aashu", 'age': 22, 'city': 'Bhopal'}

print(student['city'])

#Update the value of 'age' to 23.
s = {'age': 23}
student.update(s)
print(student)

# Add a new key 'course' with value 'B.Tech'.
student.setdefault('course','B.tech')
print(student)

# Delete the key 'city' safely.
student.pop('city')
print(student)