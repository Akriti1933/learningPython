#Dictionary created
student = {
    "name":"furba",
    "age": 23,
    "address":"banepa",
}


#only for name print
student_name = student["name"][0]

student_age = student.get('age')

student['age']=30

#To delete 
del student["address"]

print(student)

for key,value in student.items():
    print(f"key: {key} -> value: {value}")


#To set and loop in set
names_set = {"ram","ram","hari","jhon"}
for name in names_set:
    print(name)

print('ram' in names_set)


squres = [ x for x in range(10)]
print(squres)

    


