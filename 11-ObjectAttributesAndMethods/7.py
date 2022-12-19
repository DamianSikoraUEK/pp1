class Student():
    university = "UEK Kraków"
    id = 100000

    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Student.id
        Student.id+=1

    def __str__(self):
        return f"{self.name} {self.surname} {self.id}, {self.field}, {self.university}"

student = Student("Anna","MAJ","Applied Informatics")
print(student)
print()
student1 = Student("Adrian","MAJ","Applied Informatics")
print(student1)
print()
student2 = Student("Aneta","Stanek","Applied Informatics")
print(student2)