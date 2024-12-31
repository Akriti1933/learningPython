students =[]

student1 = {
    "name":"Aaa",
    "age":22,
    "major": "math",
    
    }

student2 = {
    "name":"bb",
    "age":33,
    "major":"python"
}

students.append(student1)
students.append(student2)

students[0]["name"] = "Hari"

for student in students:
    print(f"Name : {student ['name']} age -> {student['age']} major ->{student['major']}")


