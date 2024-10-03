#Podemos ver cómo se introducen datos por la línea 
# de comandos con la función input («Con un mensaje»).
titulo:str = input('Ingrese la que palabra que quiera subrayar \n')

#Podemos ver la sobrecarga de métodos y cómo 
#pasar un parámetro con un «valor por defecto».
def subrayarTitulo(titulo:str,caracter="*"):
    print("\t",titulo)
    print("\t",caracter*len(titulo))
    
subrayarTitulo(titulo)
subrayarTitulo("Sistema de Gestión Empresarial")
subrayarTitulo(titulo,"-")
subrayarTitulo("Sistema de Gestión Empresarial","#")