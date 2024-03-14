#Encontrar maximo y minimo 

def encontrarMaximoYMinimo(lista_de_numeros:list):
    lista_de_numeros.sort()
    return f'Numero Maximo: {lista_de_numeros[-1]} y numero Minimo: {lista_de_numeros[0]}'

my_list = [100, 200, 232 , 432, -19, 0, 29]

def findMaxandMin(list:list): 
    numero_anterior_menor = 0
    numero_anterior_mayor = 0
    for numero in list:
        if numero > numero_anterior_mayor:
            numero_anterior_mayor = numero
        if numero < numero_anterior_menor:
            numero_anterior_menor = numero
    return numero_anterior_menor, numero_anterior_mayor
    
print(encontrarMaximoYMinimo(my_list))
print(findMaxandMin(my_list))

# contar vocales y consontantes
def contadorVocalesyconsonantes(texto:str):
    vocals = ['a','e','i','o','u']
    numero_consonantes = 0
    numero_vocales = 0
    for letter in texto.lower():
        if letter != ' ':
            if letter in vocals: 
                numero_vocales += 1
            else:
                numero_consonantes+=1
    return f'El numero de vocales es : {numero_vocales} y de consonantes es : {numero_consonantes}'
            
print(contadorVocalesyconsonantes('Hola Soy Leandro'))
            