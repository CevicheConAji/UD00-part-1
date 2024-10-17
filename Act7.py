import random

color = ["red","white","black","pink","blue"]
class Car:
    def __init__(self,matricula,color):
        self.matricula = matricula
        self.color = color
        
    def imprimirInfo(self):
        print(f"MATRICULA: {self.matricula} \nCOLOR: {self.color}")

nCars = int(input("Ingrece la cantidad de coches que desea tener"))

for n in range(1,nCars+1):
    numero:str = n
    c = Car(numero,random.choice(color))
    c.imprimirInfo()


