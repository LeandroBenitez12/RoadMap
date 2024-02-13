"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Aritmetics 
def arithmentic_operators(operator: str , n1: float, n2: float) -> float:
    sum = n1 + n2
    subtraction = n1 - n2
    multiplication = n1 * n2
    split = n1 / n2
    split_int = n1 // n2
    module = n1 % n2
    exponentiation = n1 ** n2
    
    # Utilizo operadores de comparacion, y estructuras de control condicionales
    if operator == '+':
        return sum
    elif operator == '-':
        return subtraction 
    elif operator == '*':
        return multiplication 
    elif operator == '/':
        return split 
    elif operator == '//':
        return split_int 
    elif operator == '%':
        return module 
    elif operator == '**':
        return exponentiation 
    else:
        return 'Error: The operator not exist'
    
print(arithmentic_operators('%', 13, 2))

def arithmentic_operators2(operator: str , n1 : float, n2: float ) -> float:
    operators_dict = {
        "+": n1 + n2,
        "-": n1 - n2,
        "*": n1 * n2,
        "/": n1 / n2,
        "//": n1 // n2,
        "%": n1 % n2,
        "**": n1 ** n2,
    } 
    return operators_dict.get(operator, 'Error')

print(arithmentic_operators2('//', 99, 5))

#Operators comparison , return = > True / False

def operator_comparison(operator, n1,n2) -> bool:
    operators= {
        "==": n1 == n2,
        "!=": n1 != n2,
        ">=": n1 >= n2,
        "<=": n1 <= n2,
        "<": n1 < n2,
        ">": n1 > n2,
    }
    return operators.get(operator, 'Error')
print(operator_comparison('!=', 4, 5))

# logical operators
print(f'AND 14 >= 18 and 19 >= 18: {17 >= 18 and 22 >= 18}')
print(f'OR 14 >= 18 and 19 >= 18: {14 >= 18 or 19 >= 18}')
print(f'NOT 18 >= 18: {not 18 == 18}')

# Assigment Operators
my_num = 18 # '=' asignacion 
print(my_num)
my_num -= 1 #substract and assigment
print(my_num)
my_num *= 2 #multiply and assigment
print(my_num)
my_num /= my_num #substract and assigment
print(my_num)

# Identity Operators 
my_new_num= 1.0

print(f' My_num es == a my_new_numb {my_num is my_new_num}') # no tienen la misma posicion en memoria , es lo que compara

my_new_num = my_num 
print(f' My_num es == a my_new_numb {my_num is my_new_num}')

# operadores de pertenencia 
print(f'O in Leandro: {'o' in 'Leandro'}')