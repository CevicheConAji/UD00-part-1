#Ejemplo 'is' 'not' 'in' con funciones

fruta01 = "Pera"
fruta02 = "Manzana"
listaFrutas = ["Pera","Manzana"]

#El operador devuelve true si los elementos son exactamente iguales
def isExplicacion():
    if(fruta01  is fruta02):
        print("Son iguales")
    else:
        print("No son iguales")

#El operador devuelve true si un elemento se encuentra dentro de otro
def inExplicacion():
    if(fruta01 in listaFrutas):
        print(f"La fruta:{fruta01} esta en la lista")

isExplicacion()

inExplicacion()

