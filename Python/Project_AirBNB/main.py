from flight import Flight
from user import User 
from booking import Booking

user10221 = User('Leandro', 'Leansvae9@gmail.com')
user10222 = User('Simon', 'Oscarreyes@gmail.com')
user10223 = User('Juan', 'Juantrolo@gmail.com')
user10224 = User('Matias', 'elmatute@gmail.com')

vueloMadrid = Flight('4523134324dcqecq', 'Buenos Aires', 'Madrid')
vueloCordoba = Flight('yegy2g', 'Newbery', 'Cordoba')

ticket = Booking('jnsjdnsn')

print(ticket.reserveFlight(user10221, vueloCordoba))
