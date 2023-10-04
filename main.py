from faculty import Faculty
from students import Student


def main():
    faculties = {}
    
    while True:
        print("1. Create and assign a student to a faculty")
        print("2. Graduate a student from a faculty")
        print("3. Display current enrolled students")
        print("4. Display graduates")
        print("5. Tell or not if a student belongs to this faculty.")
        print("6. Create a new faculty.")
        print("7. Search what faculty a student belongs to by email.")
        print("8. Display University faculties.")
        print("9. Display all faculties belonging to a field.")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        
        if choice == '1':
            faculty_name = input("Enter the name of the Faculty: ")
            if faculty_name not in faculties:
                abbreviation = input("Enter the abbreviation of the Faculty: ")
                study_field = input("Enter the study field of the Faculty: ")
                faculties[faculty_name] = Faculty(faculty_name, abbreviation, study_field)

            student_info = input("Enter Student Info as firstName, lastName, email, enrollmentDate, dateOfBirth: ").split(',')
            student = Student(*student_info)
            faculties[faculty_name].add_student(student)
        
        elif choice == '2':
            faculty_name = input("Enter the name of the Faculty: ")
            if faculty_name in faculties:
                graduate_email = input("Enter the email of the student to graduate: ")
                faculties[faculty_name].graduate_student(graduate_email)
            else:
                print("Faculty not found!")

        elif choice == '3':
            faculty_name = input("Enter the name of the Faculty: ")
            if faculty_name in faculties:
                faculties[faculty_name].display_current_students()
            else:
                print("Faculty not found!")
                
        elif choice == '4':
            faculty_name = input("Enter the name of the Faculty: ")
            if faculty_name in faculties:
                faculties[faculty_name].display_graduates()
            else:
                print("Faculty not found!")
                
        elif choice == '5':
            faculty_name = input("Enter the name of the Faculty: ")
            if faculty_name in faculties:
                student_email = input("Enter the email of the student to check: ")
                if faculties[faculty_name].student_belongs(student_email):
                    print(f"The student with email {student_email} belongs to {faculty_name} faculty.")
                else:
                    print(f"No student with email {student_email} belongs to {faculty_name} faculty.")
            else:
                print("Faculty not found!")
                
        elif choice == '6':
            faculty_name = input("Enter the name of the new Faculty: ")
            if faculty_name in faculties:
                print("Faculty already exists!")
            else:
                abbreviation = input("Enter the abbreviation of the Faculty: ")
                study_field = input("Enter the study field of the Faculty: ")
                faculties[faculty_name] = Faculty(faculty_name, abbreviation, study_field)
                print(f"Faculty {faculty_name} has been created!")
                
        elif choice == '7':
            student_email = input("Enter the email of the student to search: ")
            found = False
            for faculty_name, faculty in faculties.items():
                if faculty.find_student(student_email):
                    print(f"The student with email {student_email} belongs to {faculty_name} faculty.")
                    found = True
                    break
            if not found:
                print(f"No student with email {student_email} found in any faculty.")
                
        elif choice == '8':
            if faculties:
                print("University Faculties are:")
                for faculty_name in faculties.keys():
                    print(faculty_name)
            else:
                print("No faculties have been created yet.")
                
        elif choice == '9':
            field = input("Enter the field (e.g. FOOD_TECHNOLOGY) to display all faculties belonging to it: ")
            found = False
            for faculty in faculties.values():
                if faculty.display_study_field() == field:
                    print(faculty.name)
                    found = True
            if not found:
                print(f"No faculties found belonging to {field}.")
                
        elif choice == '10':
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()