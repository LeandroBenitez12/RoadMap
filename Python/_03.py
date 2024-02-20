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
 
# structures in python
my_list_guests = ['Leandro', 'Julieta', 'Juana', 'Jose', 'Gabriel', 'Mariano', 'Pedro', 'Taiel']

# Update elements in the list
for index , guest in enumerate(my_list_guests):
    my_list_guests[index] = 'Guest: ' + guest # access at the guest list
    
print(my_list_guests)

my_list_guests.append("Mariano") # Insert the element at the list of guest
print(my_list_guests)

# Operaciones de Eliminacion en Listas de python 

# Del , palabra reservada en python para eliminar cualquier objeto , se elimina por indice o segmentos[0:2]
# No retorna nada simplemente borra y modifica lista original
del my_list_guests[0:2] 

# Pop Retorna elemento borrado, se proporciona un indice , si no lo hay elimina el ultimo 
print(my_list_guests.pop(4))
print(my_list_guests)

# Remove, Elimina solo la primera coincidencia, no retorna nada , es util cuando no se conoce el indice
my_list_guests.remove("Mariano") # Delete 
print(my_list_guests)




print("---------- INSERT ------------")

# function to order by abcd
my_list_guests.sort() # by defect order abcd
print(my_list_guests)

# reverse list 
my_list_guests.reverse()
print(my_list_guests)

print("---------- INSERT ------------")
# INSERT ELEMENT IN LIST
my_list_guests.insert(0, 'Pepe')
print(my_list_guests)

# I create element 
my_list_guests.append("Rayana")

my_other_guests = ["Elias", "Lorena", "Ramon"]

my_list_guests += my_other_guests
print(my_list_guests)

my_list_guests.extend(["Maga","Piñon"])
print(my_list_guests)
# Operaciones GET
print(f'First element: {my_list_guests[0]}') # access to the element first


# Obtenemos el indice del elemento
print(f'Indice de Rayana: {my_list_guests.index("Rayana")}')

### TUPLES ###
# this are inmutables, but you can do some operations 
# Tuples are immutable

my_tuple = ("German", "German", "Pablo", "Leandro", "German", "Leandro", "Rodrigo", "German", "Agustin")
print(f'Cantidad de "Leandro" en my_tuple: {my_tuple.count("Leandro")}') # can be counted

# the get are similars in the lists
print(my_tuple[-2]) # access
print(my_tuple[0:3])

print(len(my_tuple))# contar elementos totales

my_tuple = my_tuple*3 # multiplicar elementos
print(my_tuple)
print(len(my_tuple))
# Updates
#Slice assignment: Puedes usar la asignación de slices para actualizar varios elementos a la vez en la lista.
my_list_guests[-2:]= ["Miguel", "Agnel"]
print(my_list_guests)

#order
my_tuple = tuple(sorted(my_tuple)) # ordering, el sorted las pasa a listas entonces hay que pasarlas a tuplas nuevamente
print(my_tuple)

# Sets / Conjuntos , no repeated elements 
my_set =  {'Leandro', 'Alejandro', 'leandro', 'Leandro'}
print(my_set) # returns set without  repeated elements

# Insert
my_set.add('Leo') # Insert a new element
print(my_set)

