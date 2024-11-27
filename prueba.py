# # Este código crea un puente utilizando bucles for

# # Definir el ancho y la altura del puente
# ancho = 10
# altura = 5

# # Crear la parte superior del puente
# for i in range(ancho):
#     print("#", end="")
# print()

# # Crear los pilares del puente
# for i in range(altura):
#     print("#" + " " * (ancho - 2) + "#")

# # Crear la parte inferior del puente
# for i in range(ancho):
#     print("#", end="")
# print()

ancho = 10
alto = 5

for i in range(ancho):
    print("#" , end="")
print()

for i in range(alto):
    print("#" , " " * (ancho - 2) , "#" , sep="")
    #print("#"+" "*(10 - 2)+"#")

for i in range(ancho):
    print("#" , end="")
print()