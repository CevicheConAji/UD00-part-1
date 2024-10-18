'''Uso de Lambda.
Empezamos con una función fácil de entender. 
Las expresiones lambda. 
Como podemos ver a continuación:
Esta función suma los valores de a y b. 
'''
from functools import reduce

def suma(a,b):
    return a+b
'''Como vemos, lambda no tiene nombre. 
Por lo tanto, salvo que se asigne a una variable,
es totalmente inútil.
'''
suma_lambda = lambda a,b : a+b

print(suma_lambda(2,4))

lista = []

numeros_str = str(input('Ingresa los numeros\n'))
#Separamos por espacios la lista con el método slit()
lista = numeros_str.split(" ")
print(lista)

#función que convierte cadena a enteros
def convertirEntero(x):
    return int(x)
'''
La función map toma dos entradas:

Una lista o iterable que será modificado en una nueva.
Una función, que será aplicada a cada uno de los elementos 
de la lista o iterable anterior.
Nos devuelve una nueva lista donde todos y cada uno de los elementos
de la lista original han sido pasados por la función.
map(funcion_a_aplicar, entrada_iterable)'''
#Convertimos la lista de cadenas de caracteres 
# a enteros para poder reutilizarla después. 
lista_enteros = list(map(lambda x: int(x),lista))

print(lista_enteros)

def es_menor_diez(x):
    return x < 10

#Filtramos los números menores de 10 
# se convierte en una lista antes de imprimir

lista_menores_diez = list(filter(lambda x: x < 10,lista_enteros))

print(lista_menores_diez)

#Reducimos la lista a un valor con una función acumuladora. 
#Tenemos que importar:
#from functools import reduce

lista_multi = reduce(lambda x,val:x*val,lista_menores_diez)

print(lista_multi)