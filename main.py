from collections import deque
import copy

def encontrar_posicion_vacia(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                return i, j

def intercambiar(tablero, x1, y1, x2, y2):
    nuevo_tablero = copy.deepcopy(tablero)
    nuevo_tablero[x1][y1], nuevo_tablero[x2][y2] = nuevo_tablero[x2][y2], nuevo_tablero[x1][y1]
    return nuevo_tablero

def resolver_puzzle(tablero_inicial):
    tablero_meta = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    cola = deque([(tablero_inicial, [])])
    visitados = set()
    intentos = 0
    
    while cola:
        tablero, camino = cola.popleft()
        clave = str(tablero)
        
        if clave in visitados:
            continue
        visitados.add(clave)
        intentos += 1
        
        if tablero == tablero_meta:
            print(f"¡Solución encontrada en {intentos} intentos!")
            print("Pasos:")
            for idx, paso in enumerate(camino, 1):
                print(f"Paso {idx}:")
                for fila in paso:
                    print(" ".join(map(str, fila)))
                print()
            return
        
        x, y = encontrar_posicion_vacia(tablero)
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nuevo_tablero = intercambiar(tablero, x, y, nx, ny)
                cola.append((nuevo_tablero, camino + [nuevo_tablero]))
    
    print(f"No se encontró solución después de {intentos} intentos.")

tablero_inicial = [
    [8, 1, 3],
    [7, 0, 5],
    [6, 2, 4]
]

resolver_puzzle(tablero_inicial)