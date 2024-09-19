import copy

#Creamos la lista de Frutas

frutasList = ["Manzana","Pera","Platano","Fresa"]

#Copiamos la lista de frutas
shadowCopy = copy.copy(frutasList)

#Añadimos un elemento a la lista con append
frutasList.append("Cereza")

#Hacemos una copia profunda de la lista de Frutas
deepCopy = copy.deepcopy(frutasList)

def imprimirLista(lista, nombreLista:str ):
    print(nombreLista)
    for l in lista:
        print("\t",l)
#Aquí vemos la diferencia entre ShadowCopy y DeepCopy
print("Vemos la diferencia entre Shadow Copy y DeepCopy")
imprimirLista(shadowCopy,"Shadow List:")

imprimirLista(deepCopy,"Deep Copy:")

#Remover elemento de la lista
frutasList.remove("Manzana")

imprimirLista(frutasList,"Prueba")

