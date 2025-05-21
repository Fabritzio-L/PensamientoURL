# Fabritzio Lopez
matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(tablero):
    for fila in tablero:
        for c in fila:
            print(c, end=' ')
        print()
    print()


def contar_vecinos(matriz, fila, col):
    vecinos = 0
    for d in [-1, 1]:  
        if 0 <= col + d < len(matriz[0]):
            vecinos += matriz[fila][col + d]
    return vecinos

def siguiente_generacion(tablero):
    nueva = []
    for i in range(len(tablero)):
        fila_nueva = []
        for j in range(len(tablero[0])):
            celula = tablero[i][j]
            vecinos = contar_vecinos(tablero, i, j)

            if celula == 1:
                if vecinos < 1 or vecinos > 2:
                    fila_nueva.append(0)
                else:
                    fila_nueva.append(1)
            else:
                if vecinos == 1:
                    fila_nueva.append(1)
                else:
                    fila_nueva.append(0)
        nueva.append(fila_nueva)
    return nueva

print("Generacion 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generacion 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generacion 2:")
imprimir_tablero(generacion_2)
