import copy

#Recibe dos números y devuelvo una suma
def suma(num1,num2):
    print(f"La suma de {num1} + {num2} =",num1 + num2)

suma(155,34)

#Recibe una lista y dobla los valores de todos los elementos

numList = [1,2,3,4,5]

print(f"Lista original {numList}")

def doblarLista(numList):
    res = []
    for ele in numList:
        res.append(ele*2)
    return res

print(f"Lista doblada {doblarLista(numList)}")
