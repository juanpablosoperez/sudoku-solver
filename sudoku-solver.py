def encontrar_siguiente_vacio(puzzle):
    # encontrar la siguiente fila y columna en el puzzle, si no esta llena aun, reemplazar por -1
    # retornar fila, columna en una tupla o (None,None) si no hay

    # recordar que los indices van de 0-8
    for f in range(9):
        for c in range(9):
            if puzzle[f][c] == -1:
                return f, c
    return None, None   # si no hay espacios en el puzzle


def es_valido(puzzle,adivinar,fila,col):
    # retornamos verdadero si es valido, y falso en caso de que no lo sea
    #empezando por la fila
    valor_fila = puzzle[fila]
    if adivinar  in valor_fila:
        return False

    # ahora las columnas
    #valor_columna = []
    #for i in range(9):
        #valor_columna.append(puzzle[i][col])
    valor_columna = [puzzle[i][col] for i in range(9)]
    if adivinar in valor_columna:
        return False

    # ahora el cuadrado
    # iterar sobre los 3 valores en las filas y columnas
    comienzo_fila = (fila // 3) * 3 # 1//3 = 0.5//3 = 1, ...
    comienzo_col = (col // 3) * 3

    for f in range(comienzo_fila, comienzo_fila + 3):
        for c in range(comienzo_col, comienzo_col + 3):
            if puzzle[f][c] == adivinar:
                return False
    # si llegamos aqui, esto es un check pass
    return True


def resolver_sudoku(puzzle):
    # usando backtracking
    # el puzzle es una lista de listas, donde cada lista es una fila de nuestro puzzle
    # retorna solo si existe solucion

    # paso 1: elige algún lugar del rompecabezas para adivinar
    fila, col = encontrar_siguiente_vacio(puzzle)
    # paso 1.1: Si no queda ningún lugar, entonces hemos terminado porque solo permitimos entradas válidas.

    if fila is None:
        return True    # terminariamos

    # paso 2: si hay un lugar para colocar un numero, entonces haz una adivinanza de un numero entre 1 y 9
    for adivinar in range(1, 10):
        # paso 3: chekear si es una adivinanza valida
        if es_valido(puzzle, adivinar, fila, col):
            # paso 3.1: si es valido, entonces reemplazar la adivinanza en el puzzle
            puzzle[fila][col] = adivinar
            # ahora recurre usando este rompecabezas
            # paso 4: llamar recursivamente a nuestra función
            if resolver_sudoku(puzzle):
                return True

        # paso 5: si no es valido, o la adivinanza no pudo resolver el puzzle, necesitamos backtrack y probar de nuevo
        puzzle[fila][col] = -1  # resetear el juego
    # paso 6: si no encuentra solucion, el puzzle es IMPOSIBLE DE RESOLVER!!!
    return False


if __name__ == '__main__':
    ejemplo = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]
    print(resolver_sudoku(ejemplo))
    print(ejemplo)

