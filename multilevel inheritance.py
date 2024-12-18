class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id=",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age,Id)
        self.Salary=Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary=",self.Salary)

man=Manager("Harini",18,2613,10000)
man.displayManager()


#hierarchical inheritance
"""class Student:
    def __init__(self,name):
        self.name=name
    def displayStudent(self):
        print("Name=",self.name)

class Mark(Student):
    def __init__(self,name,mark):
        super().__init__(name)
        self.mark=mark
    def displayMark(self):
        self.displayStudent()
        print("Mark=",self.mark)

class Grade(Student):
    def __init__(self,name,mark,grade):
        super().__init__(name,mark)
        self.grade=grade
    def displayGrade(self):
        self.displayMark()
        print("Grade=",self.grade)

mar=Mark("Harini",98)
mar.displayMark()

gra=Grade("Harini",98,"A")
gra.displayGrade()"""


class Student:
    def __init__(self, name):
        self.name = name

    def displayStudent(self):
        print("Name =", self.name)

class Mark(Student):
    def __init__(self, name, mark):
        super().__init__(name)
        self.mark = mark

    def displayMark(self):
        self.displayStudent()
        print("Mark =", self.mark)

class Grade(Mark):
    def __init__(self, name,mark, grade):
        super().__init__(name,mark)
        self.grade = grade

    def displayGrade(self):
        self.displayMark()
        print("Grade =", self.grade)

# Correct usage:
mar = Mark("John", 98)  # Name and mark provided
mar.displayMark()

gra = Grade("John",98,"A")  # Name, mark, and grade provided
gra.displayGrade()
