class HotelRoom:
    def __init__(self):
        self.__room_number=None
        self.__is_occupied=False
        self.__rate_per_night=None
    def get_room_number(self):
        return self.__room_number
    def set_room_number(self,room_number):
        if room_number>0:
              self.__room_number=room_number
    def get_rate_per_night(self):
        return self.__rate_per_night
    def set_rate_per_night(self,rate_per_night):
        if rate_per_night>0:
            self.__rate_per_night=rate_per_night
    def check_in(self):
        if self.__is_occupied:
            raise Error("The room is already occupied")
        self.__is_occupied=True
    def check_out(self):
        if not self.__is_occupied:
            raise Error("The room is already vacant")
        self.__is_occupied=False
    def display_details(self):
        print(f"Room Number: {self.__room_number}")
        print(f"Rate per Night: ${self.__rate_per_night}")
        print(f"Occupied: {"Yes" if self.__is_occupied else "No"}")
try:
    room = HotelRoom()
    room.set_room_number(13)
    room.set_rate_per_night(1000)
    room.display_details()
except Exception as e:
    print(e)
