"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 
"""

my_name = '      Hi there, I am Leandro ,and I am nineteen years'

# concatenate strings 
print('Hola ' + my_name)

# access to substrings by indexation
print(my_name[0])

#i get the index of the first character 'o'
print(my_name.index('o'))

#i count the number of characters in the string that are repeated
print(my_name.count(','))

# i replace the character '.' by '.' 
print(my_name.replace(',', '.'))

# i find the substring in the string
print(my_name.find('Leandro'))

# i convert the string to uppercase 
print(my_name.upper())

# i convert the string to lowercase 
print(my_name.lower())

# i divide the string in substring by a 'character' and i convert all in a list
my_list_strings = my_name.split(',')
print(my_list_strings)

# removed all characters ' ' from the string at the start and  end  
print(my_name.strip())

# i join strings from a list of strings
my_new_string=''
print(my_new_string.join(my_list_strings))

# i make the first character uppercase
my_other_string= 'pedro'
print(my_other_string.capitalize())

# i measure the length of the string
print(len(my_other_string))

# interpolation
nombre = "Juan"
edad = 25
saludo = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(saludo)