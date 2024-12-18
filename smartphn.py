#1.
class Camera:
    def __init__(self, resolution): #self-current instance of an object 
        self.resolution = resolution  #camera quality

    def take_photo(self):
        print(f"Photo taken with {self.resolution}MP resolution.")

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number 

    def make_call(self, number):
        print(f"Calling {number} from {self.phone_number}.")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

class Smartphone(Camera, Phone):
    def __init__(self, resolution, phone_number, brand, model):
        Camera.__init__(self, resolution)  
        Phone.__init__(self, phone_number)  
        self.brand = brand 
        self.model = model  

    def display_device_info(self):
        print(f"Smartphone Brand: {self.brand}, Model: {self.model}, Resolution: {self.resolution}MP")


smartphone = Smartphone(resolution=48, phone_number="8148120234", brand="oppo", model="F11pro")


smartphone.take_photo()  
smartphone.make_call("7305232123") 
smartphone.send_message("8148120234", "Hello!")  
smartphone.display_device_info()


#2.
class Student:
    def __init__(self, name, course):
        self.name = name  
        self.course = course  

    def studentInfo(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")



class StudentAthlete(Student):
    def __init__(self, name, course, sport):
        super().__init__(name, course)
        self.sport = sport  

    def displayAthleteInfo(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Sport: {self.sport}")



student_athlete = StudentAthlete(name="Harini", course="AI", sport="Basketball") 

student_athlete.studentInfo()  
print("Athlete Info: ")
student_athlete.displayAthleteInfo() 

