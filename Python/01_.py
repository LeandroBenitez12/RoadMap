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
    
    list_operators = [
        sum,subtraction,multiplication,split,split_int,module,exponentiation
    ]
    for index in list_operators:
        # print(str(index))         
        if str(operator) == str(index):
            return index 
    return 'Error'
    
print(arithmentic_operators('sum', 2, 2))
