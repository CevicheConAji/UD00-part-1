'''Define la clase Caro en Python 3. La clase tendrá como atributos “matrícula” (numérica) 
y “color”
.
Crea un método imprimir, y además dos métodos que quieras.
En segundo lugar, hiciera que el programa pido un número “n” por teclado y se crean “n”
 instancias de la
clase, donde cada instancia:
● Cada “matrícula” tendrá un número consecutivo desde 1 hasta “n”.
● El “color” será para cada instancia un color aleatorio obtenido de este listado 
[“red” , “white” ,“black” , “pink” , “blue”]
Finalmente, el programa tendrá que imprimir los valores de las 10 primeras instancias. 
En caso de que “n”
sea menor que 10, solo imprimirá “n” instancias.'''
import random
color = ["red","white","black","pink","blue"]
class Car:
    def __init__(self,matricula,color):
        self.matricula = matricula
        self.color = color
        
    def imprimirInfo(self):
        print(f"MATRICULA: {self.matricula} \nCOLOR: {self.color}")

nCars = int(input("Ingrece la cantidad de coches que desea tener"))
if nCars <= 10:
    for n in range(1,nCars+1):
        numero:str = n
        c = Car(numero,random.choice(color))
        c.imprimirInfo()
else: print("Demasiados coches quieres tener")

