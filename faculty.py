class Faculty:
    def __init__(self, name, abbreviation, studyField):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.graduates = []
        self.studyField = studyField

    def add_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.graduates.append(student)
            print(f"{student} has graduated from {self.name}!")
        else:
            print(f"{student} is not enrolled in {self.name}.")

    def display_students(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(student)

    def display_graduates(self):
        print(f"Graduates from {self.name}:")
        for grad in self.graduates:
            print(grad)

    def __str__(self):
        return self.name
    
    def student_belongs_to(self, student):
        if student in self.students or student in self.graduates:
            return True
        return False