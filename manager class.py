class Employee:
    def __init__(self, name, salary):
        self.name = name  # Attribute to store the employee's name
        self.salary = salary  # Attribute to store the employee's salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self,name, salary)
        self.department = department  # Attribute to store the department name

    def display_department(self):
        print(f"Department: {self.department}")  

# Create an object of the Manager class
manager = Manager("Harini", 75000, "Sales")

manager.display_details()  
manager.display_department() 
