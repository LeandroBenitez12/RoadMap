"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """
my_list_guests = ['Leandro', 'Julieta', 'Juana', 'Jose', 'Gabriel']

# Update elements in the list
for index , guest in enumerate(my_list_guests):
    my_list_guests[index] = 'Guest: ' + guest # access at the guest list
print(my_list_guests)

my_list_guests.append("Mariano") # Insert the element at the list of guest
print(my_list_guests)

my_list_guests.remove("Mariano") # Delete 
print(my_list_guests)

print(my_list_guests[0]) # access to the element first

# function to order by abcd
my_list_guests.sort() # by defect order abcd
print(my_list_guests)

# Tuples are immutable
my_tuple = ("German", "-", "Pablo", "+", "-", "+", "Rodrigo", "-", "+")
print(my_tuple.count("-")) # can be counted
print(my_tuple[2]) # access
my_tuple = tuple(sorted(my_tuple)) # ordering, el sorted las pasa a listas entonces hay que pasarlas a tuplas nuevamente
print(my_tuple)

# Sets / Conjuntos , no repeated elements 
my_set =  {'Leandro', 'Alejandro', 'leandro', 'Leandro'}
print(my_set) # returns set without  repeated elements

my_set.add('Leo') # Insert a new element
print(my_set)

