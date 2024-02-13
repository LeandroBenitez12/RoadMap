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
