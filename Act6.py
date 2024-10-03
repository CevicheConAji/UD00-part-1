#indice de masa corporal (medida,peso)
imc = [(177,57),(165,80),(177,50)]


sorted(imc, key=lambda imc:imc[0],reverse=False)
imc.sort(key=lambda imc:imc[1],reverse=False)
print(imc)


#Explicacion https://www.freecodecamp.org/espanol/news/python-ordenar-lista-con-sort-ascendente-y-descendente-explicado-con-ejemplos/