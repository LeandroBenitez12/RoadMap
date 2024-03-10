"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

"""

# Tipos de datos por valor 
# En python son todos los valores que son primitivos ( int, float, string, bool, tuple)
a = (10, 8, 9, 2)
b = a # hacemos una copia del valor del momento , luego se puede cambiar

print(b)
a = (3, 6, 8, 52)
b = (2, 2, 39, 42)
print(a,b)

# Tipos de datos por referencia
# set , list , dict (mutables)
c = [1,10,13,14,18]
d = c
print(c,d)
d.append(9) # concepto de variable por referencia, estos datos heredan la posicion de memoria no copian valor
print(c,d)

# Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
# *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.

my_int= 10
my_list = [10,9,8,7,6]

def variables_changed(num:int, my_list: list):
    num = 89
    my_list.pop(0)
    print(num)
    print(my_list)
    
variables_changed(my_int, my_list)
print(my_int, my_list)

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

valor1 = 'Carlos'
valor2 = 'Leon'
def recibo_por_valor(parametro1 , parametro2):
    temporal_value_p1 = parametro1
    parametro1 = parametro2
    parametro2 = temporal_value_p1
    return parametro1, parametro2

valor1_diferente, valor2_diferente = recibo_por_valor(valor1, valor2)

print(valor1, valor2)
print(valor1_diferente, valor2_diferente)

referencia1 = [0,1,2,4]
referencia2 = [1,8,9,3]

# esto nos sirve para hacer una copia de la referencia en memoria, ya sea conserva edad de usuario anterior
def recibo_por_referencia(parametro1 , parametro2):
    temporal_value_p1 = parametro1 # posicion en memoria
    temporal_value_p1.append(100)
    parametro1 = parametro2 
    parametro2 = temporal_value_p1
     
    return parametro1, parametro2 

referencia1_diferente, referencia2_diferente = recibo_por_referencia(referencia1, referencia2)

print(referencia1, referencia2)
print(referencia1_diferente, referencia2_diferente)

