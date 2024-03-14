from flight import Flight
from user import User


class Booking(Flight, User):
    # Metodo Constructor
    def __init__(self, reserveNumber, date, seat ):
        self.__reserveNumber = reserveNumber
        self.__date = date 
        self.__seat = seat
    # reservar vuelo 
    def reserveFlight(self, User, Flight):
        return f'Se reserva vuelo para {User.__name} email: {User.__email}, para el vuelo nº {Flight.__flight_number}'

    def canceledFlight(self):
        return (f'Se Cancela el vuelo para {User.__name} email: {User.__email}, para el vuelo nº {Flight.__flight_number}')
