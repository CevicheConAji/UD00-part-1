# Función para leer un archivo de texto y convertirlo en una lista de listas que representa un Sudoku
def leer_sudoku(nombre_archivo):
    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, "r") as archivo:
        # Convertimos cada línea del archivo en una lista de enteros
        sudoku = [list(map(int, linea.split())) for linea in archivo]
    # Retornamos la representación del Sudoku como una lista de listas
    return sudoku

# Leyendo el archivo "Sudoku.in" y almacenando el Sudoku en una variable
sudoku = leer_sudoku("Sudoku.in")
print(sudoku)  # Imprime el Sudoku leído

# Función para validar si una fila contiene exactamente los números del 1 al 9, sin repeticiones
def validar_fila(fila):
    # Compara los elementos únicos de la fila con el conjunto {1, 2, ..., 9}
    return set(fila) == set(range(1, 10))

# Función para obtener una columna del Sudoku dada su posición
def obtener_columna(sudoku, indice_columna):
    # Retorna una lista con los elementos de la columna correspondiente
    return [fila[indice_columna] for fila in sudoku]

# Función para obtener una subcuadrícula 3x3 del Sudoku dada su posición inicial
def obtener_subcuadricula(sudoku, inicio_fila, inicio_columna):
    # Extraemos los elementos de la subcuadrícula usando dos bucles anidados
    return [sudoku[i][j] for i in range(inicio_fila, inicio_fila + 3) for j in range(inicio_columna, inicio_columna + 3)]

# Función para validar si un Sudoku es correcto
def esSudokuCorrecto(sudoku):
    # Validamos cada fila y columna del Sudoku
    for i in range(9):  # Recorremos los índices de filas y columnas
        if not validar_fila(sudoku[i]) or not validar_fila(obtener_columna(sudoku, i)):
            return False  # Si alguna fila o columna no es válida, devolvemos False
    
    # Validamos cada subcuadrícula 3x3 del Sudoku
    for i in range(0, 9, 3):  # Recorremos las filas iniciales de cada subcuadrícula
        for j in range(0, 9, 3):  # Recorremos las columnas iniciales de cada subcuadrícula
            if not validar_fila(obtener_subcuadricula(sudoku, i, j)):
                return False  # Si alguna subcuadrícula no es válida, devolvemos False
    
    # Si todas las validaciones son correctas, devolvemos True
    return True

# Verificamos si el Sudoku es correcto y mostramos el resultado
if esSudokuCorrecto(sudoku):
    print("Correcte")  # El Sudoku es válido
else:
    print("Incorrecte")  # El Sudoku es inválido

