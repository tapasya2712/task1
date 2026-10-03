class Person:
   

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def displayPerson(self) -> None:
       
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")



class Student(Person):
    

    def __init__(self, name: str, age: int, rollNo: str, course: str):
        
        super().__init__(name, age)
        self.rollNo = rollNo
        self.course = course

    def displayStudent(self) -> None:
        """Displays complete student details."""
        print("--- Student Details ---")
        self.displayPerson()  
        print(f"Roll No: {self.rollNo}")
        print(f"Course : {self.course}")



class Teacher(Person):
    

    def __init__(self, name: str, age: int, employeeId: str, subject: str):
        # Initialize parent class attributes using super()
        super().__init__(name, age)
        self.employeeId = employeeId
        self.subject = subject

    def displayTeacher(self) -> None:
        """Displays complete teacher details."""
        print("--- Teacher Details ---")
        self.displayPerson()  # Reuse parent class method internally
        print(f"Employee ID: {self.employeeId}")
        print(f"Subject    : {self.subject}")



if __name__ == "__main__":
    # 1. Instantiate one object of Student class
    student1 = Student(
        name="Aarav Sharma", 
        age=20, 
        rollNo="CS2026-042", 
        course="Computer Science & Engineering"
    )

    # 2. Instantiate one object of Teacher class
    teacher1 = Teacher(
        name="Dr. Radhika Sen", 
        age=45, 
        employeeId="EMP-8091", 
        subject="Artificial Intelligence"
    )

    # 3. Display full details of student and teacher
    student1.displayStudent()
    print()
    teacher1.displayTeacher()

   
    
    print(" Direct Access to Parent Method:")
   
    
    print("\nCalling student1.displayPerson() :")
    student1.displayPerson()

    print("\nCalling teacher1.displayPerson() :")
    teacher1.displayPerson()
