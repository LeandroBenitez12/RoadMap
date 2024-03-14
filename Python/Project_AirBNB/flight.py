class Flight:
    def __init__(self, flight_number, origin, destination):
        self.__flight_number = flight_number
        self.__origin = origin 
        self.__destination  = destination
        
    def get_flight_number(self):
        return self.__flight_number
    
    def get_origin(self):
        return self.__origin
    
    def get_destination(self):
        return self.__destination
    
    def flight_information(self):
        return f'The flight leave from {self.__origin} and arrive in {self.__destination}'
    
    
    