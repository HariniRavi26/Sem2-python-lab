class Person:
    def __init__(self, name):
        self.name = name  # Attribute to store the name

    def show_name(self):
        print(f"Name: {self.name}")  # Method to display the name


class Student(Person):
    def __init__(self, name, student_id):
        # Calling the parent class constructor to initialize the name
        Person.__init__(self,name)
        self.student_id = student_id  # Attribute 

    def show_student_id(self):
        print(f"Student ID: {self.student_id}")  

# Create an object of the Student class
student = Student("Harini", "2612")

student.show_name()  
student.show_student_id()  
