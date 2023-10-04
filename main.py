from studyfield import StudyFields
from faculty import Faculty
from students import Student

def main():
    # Create some faculties
    faculties = {
        StudyFields.MECHANICAL_ENGINEERING: Faculty("Mechanical Engineering Faculty", "MECH", StudyFields.MECHANICAL_ENGINEERING),
        StudyFields.SOFTWARE_ENGINEERING: Faculty("Software Engineering Faculty", "SOFT", StudyFields.SOFTWARE_ENGINEERING)
    }

    # Create a student
    student1 = Student("John", "Doe", "john.doe@email.com", "2023-10-04", "2000-01-01")

    while True:
        print("\nMain Menu:")
        print("1. Faculty operations")
        print("2. General operations")
        print("3. Exit")

        choice = int(input("Enter your choice (number): "))

        if choice == 1:
            faculty_operations(faculties, student1)
        elif choice == 2:
            general_operations(faculties)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

def faculty_operations(faculties, student1):
    while True:
        print("\nFaculty Operations:")
        print("1. Assign a student to a faculty")
        print("2. Graduate a student")
        print("3. Display current enrolled students")
        print("4. Display graduates")
        print("5. Check if a student belongs to a faculty")
        print("6. Return to main menu")

        choice = int(input("Enter your choice (number): "))

        if choice == 1:
            print("\nChoose a study field for the student:")
            for field in StudyFields:
                print(f"{field.value}. {field.name.replace('_', ' ')}")

            study_choice = int(input("Enter your choice (number): "))
            
            if study_choice in faculties:
                faculties[study_choice].add_student(student1)
                print(f"\n{student1} has been assigned to {faculties[study_choice]}!")
            else:
                print("Invalid choice!")

        elif choice == 2:
            faculty_choice = int(input("From which faculty do you want to graduate the student? (Enter the number): "))
            if faculty_choice in faculties:
                faculties[faculty_choice].graduate_student(student1)
            else:
                print("Invalid choice!")

        elif choice == 3:
            faculty_choice = int(input("From which faculty do you want to display the students? (Enter the number): "))
            if faculty_choice in faculties:
                faculties[faculty_choice].display_students()
            else:
                print("Invalid choice!")

        elif choice == 4:
            faculty_choice = int(input("From which faculty do you want to display the graduates? (Enter the number): "))
            if faculty_choice in faculties:
                faculties[faculty_choice].display_graduates()
            else:
                print("Invalid choice!")

        elif choice == 5:
            faculty_choice = int(input("To which faculty do you want to check the student's belonging? (Enter the number): "))
            if faculty_choice in faculties:
                belongs = faculties[faculty_choice].student_belongs_to(student1)
                if belongs:
                    print(f"{student1} belongs to {faculties[faculty_choice]}.")
                else:
                    print(f"{student1} does not belong to {faculties[faculty_choice]}.")
            else:
                print("Invalid choice!")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
            
            
def general_operations(faculties):
    while True:
        print("\nGeneral Operations:")
        print("1. Create a new faculty")
        print("2. Search for a student's faculty by ID")
        print("3. Display University faculties")
        print("4. Display faculties by study field")
        print("5. Return to main menu")

        choice = int(input("Enter your choice (number): "))

        
        if choice == 1:
            faculty_name = input("Enter the name of the new faculty: ")
            abbreviation = input("Enter the abbreviation for the faculty: ")
            
            print("\nChoose a study field for the faculty:")
            for field in StudyFields:
                print(f"{field.value}. {field.name.replace('_', ' ')}")
            study_choice = int(input("Enter your choice (number): "))
            
            new_faculty = Faculty(faculty_name, abbreviation, study_choice)
            faculties[study_choice] = new_faculty
            print(f"Faculty '{faculty_name}' created successfully!")

        elif choice == 2:
            student_id = input("Enter the student's unique ID: ")
            student_found = False

            for faculty in faculties.values():
                for student in faculty.students:
                    if student.student_id == student_id:
                        print(f"{student} belongs to {faculty.name}.")
                        student_found = True
                        break

                if student_found: 
                    break

            if not student_found:
                print("Student not found in any faculty.")

        elif choice == 3:
            if faculties:
                print("\nList of University Faculties:")
                for faculty in faculties.values():
                    print(f"Name: {faculty.name}, Abbreviation: {faculty.abbreviation}, Study Field: {StudyFields(faculty.studyField).name.replace('_', ' ')}")
            else:
                print("No faculties have been created yet.")

        elif choice == 4:
            print("\nChoose a study field:")
            for field in StudyFields:
                print(f"{field.value}. {field.name.replace('_', ' ')}")
            
            field_choice = int(input("Enter your choice (number): "))
            if field_choice in [field.value for field in StudyFields]:
                matching_faculties = [faculty for faculty in faculties.values() if faculty.studyField == field_choice]
                
                if matching_faculties:
                    print(f"\nFaculties for {StudyFields(field_choice).name.replace('_', ' ')}:")
                    for faculty in matching_faculties:
                        print(f"Name: {faculty.name}, Abbreviation: {faculty.abbreviation}")
                else:
                    print(f"No faculties found for {StudyFields(field_choice).name.replace('_', ' ')}.")
            else:
                print("Invalid choice!")

        elif choice == 5:
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice! Please try again.")
            
if __name__ == "__main__":
    main()