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

# i get the index of the first character 'o'
print(my_name.index('o'))

# i count the number of characters in the string that are repeated
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
my_new_string = ''
print(my_new_string.join(my_list_strings))

# i make the first character uppercase
my_other_string = 'pedro'
print(my_other_string.capitalize())

# i measure the length of the string
print(len(my_other_string))

# interpolation
nombre = "Juan"
edad = 25
saludo = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(saludo)

# Los palíndromos son palabras o frases que se leen igual de izquierda a derecha que de derecha a izquierda


def isPalidrome(word_1: str) -> bool:
    word_1 = word_1.lower()
    list_word_1 = []
    # cada letra de el str es pasado a una lista de los caracteres de el str para con una funcion reverse podemos dar vuelta la lista, y luego con una funcion join unimos esa lista a un str quedando la palabra dada vuelta para su comprobacion si es palidroma o no
    for letra in word_1:
        print(letra)
        list_word_1.append(letra)
    print(list_word_1)
    list_word_1.reverse()
    print(list_word_1)
    word_1_reversed = ''
    word_1_reversed = word_1_reversed.join(list_word_1)
    print(word_1_reversed)
    if word_1 == word_1_reversed:
        return True
    return False


print(isPalidrome('oso'))

#  Los isogramas son palabras o frases en las que cada letra aparece el mismo número de veces.


def isIsogram(word: str) -> bool:
    word = word.lower()
    # cada palabra la paso a minuscula , y luego la paso por un for donde cada letra del str le cuento sus repeticiones en el str con count, estos numeros de repeticiones que tiene cada letra la comparo con las repeticiones de mi primera letra x default y si existe una distincion retorno un false = no es isogramo, si lo es, dejo que termino el for y return un true
    for letter in word:
        numbers_letters = word.count(letter)
        if numbers_letters != word.count(word[0]):
            return False
    return True


words = ["murcielago", "perro", "oso", "programacion", "python",
         "ahorcado", "casa", "isla", "muralla", "computadora"]

# funcion donde recibo listas de palabras para comprobar si son o no isogramas y retorno lista, con las isogramas nomas


def listWordsIsograms(words: list) -> list:
    listWords = []
    for word in words:
        if isIsogram(str(word)):
            listWords.append(word)
    return listWords


print(listWordsIsograms(words))


def CompareAmountLettersTwoWords(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    list_letter_word1 = []
    list_letter_word2 = []
    for letter_word1 in word1:
        list_letter_word1.append(letter_word1)
    for letter_word2 in word2:
        list_letter_word2.append(letter_word2)

    list_letter_word1.sort()
    list_letter_word2.sort()

    if list_letter_word1 == list_letter_word2:
        return True
    return False
# Los anagramas son palabras o frases que se forman al cambiar el orden de las letras de otra palabra o frase


def isAnagram(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()
    if len(word1) != len(word2):
        return False
    if CompareAmountLettersTwoWords(word1, word2) == False:
        return False
    return True


print(isAnagram('roma', 'roma'))

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 
"""


def analizerTwoWords(word1: str, word2: str):
    word1 = word1.lower()
    word2 = word2.lower()
    # palíndromos
    print(f'¿{word1} y {word2} son Palindromos? {word1 == word2[::-1]}')  # Maldito Brais
    #anagramas
    print(f'¿{word1} y {word2} son Anagramas? {sorted(word1) == sorted(word2)}') 
    # isograma
    # set() me devuelve un set de las letras que contiene la palabra sin repetir letras, y desordenadas
    # con el len() puedo pedir la cantidad de letra de la palabra o elementos del set si la palabra tiene 1 letra repetida la borrara en el set y sera menos la longitud por lo que no sera un heterograma
    # print(set(word1))
    # heterograma
    print(f'¿{word1} es un heterograma? {len(word1) == len(set(word1))}')
    print(f'¿{word2} es un heterograma? {len(word2) == len(set(word2))}')
    # isograma
    print(f'¿{word1} es un Isograma? {isIsogram(word1)}')
    print(f'¿{word2} es un Isograma? {isIsogram(word2)}')
    
my_name = 'Leandro'
print(my_name[:3:-1])  # good
analizerTwoWords('RAMONRAMON', 'ROMAN')
