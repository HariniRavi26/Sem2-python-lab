class Transport:
    def __init__(self, time, destination):
        self.time = time
        self.destination = destination
    
    def display_details(self):
        print("The time for travel is:", self.time)
        print("The Destination is:", self.destination)

class Expenses:
    def __init__(self, food, stay):
        self.food = food
        self.stay = stay
    
    def display_exp(self):
        print("The food expense is:", self.food)
        print("The stay expense is:", self.stay)

class Way(Transport, Expenses):
    def __init__(self, time, destination, food, stay, flight):
        Transport.__init__(self, time, destination)
        Expenses.__init__(self, food, stay)
        self.flight = flight
    
    def display_way(self):
        print("The way of travel is through:", self.flight)


time = input("Enter the time for travel: ")
destination = input("Enter the destination: ")
food = float(input("Enter the expense for food: "))
stay = float(input("Enter the expense for stay: "))
flight = input("Enter the flight name: ")


travel = Way(time, destination, food, stay, flight)

travel.display_details()  
travel.display_exp()      
travel.display_way()      
