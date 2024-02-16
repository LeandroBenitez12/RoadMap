
""" 
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 """
# 
def function_simple():
    print('Simple function')

def function():
            print('i can use function within function_with_params')

def function_with_params(param: bool):
    print(f'function Con parametros: {param}') 
    if param == True:
        function()
        
def function_return():
    return 'Retorno algo'

# results
function_simple()
function_with_params(True)
print(function_return())

#function anonymous
function_unseen = lambda x,y : x + y
print( function_unseen(4,5) )

# variables locals and globals
my_variable_global = 'hello world'

def hello_world():
    my_variable_local = 'hello world'
    print(f'Variable Local =  {my_variable_local}' )
    print(f'Variable Global = {my_variable_global}' )

hello_world()
name = str(input('Write your name here: ')).lower() # lower is a function python that converts text to all lowercase
print(name) # print name in lowercase format