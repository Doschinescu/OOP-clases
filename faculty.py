class Faculty:
    def __init__(self, name, abbreviation, studyField):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.studyField = studyField
        
    def add_student(self, student):
        self.students.append(student)
        print(f"{student.firstName} {student.lastName} has been added to the {self.name} faculty.")
        
    def graduate_student(self, email):
        for student in self.students:
            if student.email == email and not student.graduated:
                student.graduated = True
                print(f"{student.firstName} {student.lastName} has graduated from the {self.name} faculty.")
                return True
        print("Student not found in this faculty or already graduated!")
        return False

    def display_current_students(self):
        print(f"Current enrolled students in {self.name} faculty are:")
        found = False
        for student in self.students:
            if not student.graduated:
                print(f"{student.firstName} {student.lastName} ({student.email})")
                found = True
        if not found:
            print("No currently enrolled students.")

    def display_graduates(self):
        print(f"Graduates from {self.name} faculty are:")
        found = False
        for student in self.students:
            if student.graduated:
                print(f"{student.firstName} {student.lastName} ({student.email})")
                found = True
        if not found:
            print("No graduates yet.")
            
    def student_belongs(self, student_email):
        for student in self.students:
            if student.email == student_email and not student.graduated:
                return True
        return False
    
    def find_student(self, student_email):
        for student in self.students:
            if student.email == student_email:
                return True
        return False
    
    def display_study_field(self):
        return self.studyField
    
