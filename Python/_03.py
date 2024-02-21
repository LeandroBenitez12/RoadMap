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
my_list_guests = ['Leandro', 'Julieta', 'Juana',
                  'Jose', 'Gabriel', 'Mariano', 'Pedro', 'Taiel']

# Update elements in the list
for index, guest in enumerate(my_list_guests):
    my_list_guests[index] = 'Guest: ' + guest  # access at the guest list

print(my_list_guests)

my_list_guests.append("Mariano")  # Insert the element at the list of guest
print(my_list_guests)

# Operaciones de Eliminacion en Listas de python

# Del , palabra reservada en python para eliminar cualquier objeto , se elimina por indice o segmentos[0:2]
# No retorna nada simplemente borra y modifica lista original
del my_list_guests[0:2]

# Pop Retorna elemento borrado, se proporciona un indice , si no lo hay elimina el ultimo
print(my_list_guests.pop(4))
print(my_list_guests)

# Remove, Elimina solo la primera coincidencia, no retorna nada , es util cuando no se conoce el indice
my_list_guests.remove("Mariano")  # Delete
print(my_list_guests)


print("---------- INSERT ------------")

# function to order by abcd
my_list_guests.sort()  # by defect order abcd
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

my_list_guests.extend(["Maga", "Piñon"])
print(my_list_guests)
# Operaciones GET
print(f'First element: {my_list_guests[0]}')  # access to the element first


# Obtenemos el indice del elemento
print(f'Indice de Rayana: {my_list_guests.index("Rayana")}')

# Updates
# Slice assignment: Puedes usar la asignación de slices para actualizar varios elementos a la vez en la lista.
my_list_guests[-2:] = ["Miguel", "Agnel"]
print(my_list_guests)

# filter
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 22, 11, 93]

numbers_multiple_3 = list(filter(lambda x: x % 3 == 0 and x != 0, numbers))

print(numbers_multiple_3)
### TUPLES ###
# this are inmutables, but you can do some operations
# Tuples are immutable

my_tuple = ("German", "German", "Pablo", "Leandro", "German",
            "Leandro", "Rodrigo", "German", "Agustin")
print(f'Cantidad de "Leandro" en my_tuple: {
      my_tuple.count("Leandro")}')  # can be counted

# the get are similars in the lists
print(my_tuple[-2])  # access
print(my_tuple[0:3])

print(len(my_tuple))  # contar elementos totales

my_tuple = my_tuple*3  # multiplicar elementos
print(my_tuple)
print(len(my_tuple))

# order
# ordering, el sorted las pasa a listas entonces hay que pasarlas a tuplas nuevamente
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)

# FILTER
# my_tuple = filter()

# SETS CONJUNTOS

# Sets / Conjuntos , no repeated elements , are messy and mutables
my_set = {'Leandro', 'Alejandro', 'leandro', 'Leandro'}
print(my_set)  # returns set without  repeated elements

# Insert
my_set.add('Leo')  # Insert a new element
print(my_set)

### DICT ###
# Are elements key-value ,unique key , are mutables 'CRUD', are messy(Supposedly)
my_dict = {
    "Key": "Value",
    "user": "Leandro",
    "age": 20,
}

# GET
print(f'age: {my_dict["age"]}')

# update
my_dict["user"] = "Leandro06"
print(my_dict)

# Creo nuevos key si no estan
my_dict.update({'city': 'Buenos Aires', 'Countrie': 'Argentina'})

# si estan los actualizo con funcion update
my_dict.update({'city': 'Corrientes'})

my_dict.update({"test": 'answer'})
# DELETE
del my_dict["Key"]  # SOLO ELIMINA

# elimina introduciendo el key y retorna que se elimino
print(my_dict.pop("Countrie"))

my_dict.popitem()  # elimina ultimo key-value agregada
print(my_dict)

database_contacts = {}
DEBUG_DB = 0


def contact_book():
    def menu():
        # agenda de contactos
        options_menu = ["Search", "Insert", "Update", "Delete", 'All']
        print("-------MENU-------")
        for index, option in enumerate(options_menu):
            print(f'Option {index + 1}: Contact {option}')

        # Bloque try-except por error en caso de ingresar mal el input y no sea un int por ejemplo
        try:
            option_select = int(input("Enter option in number: "))
            return option_select
        except Exception as e:
            return print(f"Error : {e}")

    option_select = menu()
    # get key contact
    def get_key_contact():
        keys_contacts = list(database_contacts.keys())
        print(f'List of Contacts: {keys_contacts}')

    # Condicionales
    # OPERATION GET
    if option_select == 1:
        print("------Search-------")
        get_key_contact()
        try:
            key_to_search = str(input("Enter key for search it: "))
        except Exception as e:
            return print("Error : {e}")
        if key_to_search in database_contacts:
            return print(f'The key is {key_to_search} and his value is {database_contacts[key_to_search]}')
        return print("The key not exist")
    # OPERATION UPDATE
    if option_select == 2:
        print("------INSERT-------")
        try:
            key_to_insert = str(input("Enter key for insert : "))
            value_to_insert = input("Enter value for insert : ")
        except Exception as e:
            return print("Error : {e}")
        if key_to_insert in database_contacts:
            return print("Key was create")
        database_contacts.update({key_to_insert: value_to_insert})
        return print(f'contact was create succesfully: {database_contacts}')
    # OPERATION UPDATE
    if option_select == 3:
        print("------Update-------")
        get_key_contact()
        try:
            key_to_Update = str(input("Enter key for Update it: "))
        except Exception as e:
            return print("Error : {e}")
        if key_to_Update in database_contacts:
            try:
                value_update = str(
                    input(f"Enter value for Update key {key_to_Update}: "))
            except Exception as e:
                return print("Error : {e}")
            database_contacts[key_to_Update] = value_update
            return print(f'db updated: {database_contacts}')
        return print("The key not exist")
    if option_select == 4:
        print('-------DELETE--------')
        get_key_contact()
        try:
            key_to_delete = str(input('Enter the key to delete: '))
            if key_to_delete in database_contacts:
                element_deleted = database_contacts.pop(key_to_delete)
                return print(f'the element has benn deleted succesfully: {element_deleted}')
            else:
                return print(f'Element for delete not exist')

        except Exception as e:
            return print(f'Error : {e}')

    if option_select == 5:
        print('Lists of Contacts')
        print(database_contacts)


while True:
    contact_book()  # the app
    want_continue = str(input(f'you Want continue? S/N:  '))
    if want_continue.upper() is 'N':  # if is N, exit and upper is a function for to convert a variable str in all caps
        print("Exit")
        break
    # debug
    if DEBUG_DB:
        print(database_contacts)
