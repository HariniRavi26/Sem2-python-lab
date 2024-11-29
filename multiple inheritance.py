class Employee:
    def __init__(self,name,Id,position):#to assign values during object creation
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId: {self.Id}\nposition:{self.position}")

class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressInfo(self):
        print(f"Street name:{self.street}\nState Name:{self.state}\nCountry Name:{self.country}")

class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):#constructor
        super().__init__(name,Id,position)#for immediate parent and to initialize the variables we use super()
        Address.__init__(self,street,state,country)
    def displayEmp(self):#method available-to call both methods
        self.displayEmployeeInfo()
        self.displayaddressInfo()

ed=EmployeeDetails("Harini",100,"Manager","Shenoy Nagar","Tamilnadu","India")
ed.displayEmp()
        
