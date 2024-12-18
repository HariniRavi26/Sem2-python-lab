class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print("Name=",self.name)
        print("Age=",self.age)
class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.Id=Id
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("Id=",self.Id)

class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department=",self.dept)


class TeamLeader(Manager,Developer):
    def __init__(self,name,age,Id,dept,teamsize):
        Employee.__init__(self,name,age)
        self.Id=Id
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamInfo(self):
        self.displayEmployeeInfo()
        print("Id=",self.Id)
        print("Department=",self.dept)
        print("Team size=",self.teamsize)

Name=input("Enter the name: ")
Age=int(input("Enter the age: "))
Id=int(input("Enter the id: "))
Dept=input("Enter the department:")
Teamsize=int(input("Enter the teamsize: "))

tl=TeamLeader(Name,Age,Id,Dept,Teamsize)
tl.displayTeamInfo()
