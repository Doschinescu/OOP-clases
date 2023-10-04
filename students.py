class Student:
    def __init__(self, firstName, lastName, email, enrollmentDate, dateOfBirth):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.enrollmentDate = enrollmentDate
        self.dateOfBirth = dateOfBirth

    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.email})"

