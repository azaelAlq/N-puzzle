from collections import deque

# Definimos el estado objetivo (tablero resuelto)
ESTADO_OBJETIVO = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, '_')
)

def imprimir_tablero(tablero):
    """Función para imprimir el tablero en un formato legible."""
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
    print("---")

def encontrar_posicion(tablero, elemento):
    """Busca la posición (fila, columna) de un elemento en el tablero."""
    for i, fila in enumerate(tablero):
        for j, valor in enumerate(fila):
            if valor == elemento:
                return i, j
    return None

def generar_movimientos(tablero):
    """Genera los tableros resultantes de mover el espacio vacío ('_') en cada dirección posible."""
    movimientos = []
    fila, col = encontrar_posicion(tablero, '_')
    
    # Definir desplazamientos posibles: (nombre del movimiento, desplazamiento en filas, desplazamiento en columnas)
    desplazamientos = {
        "arriba": (-1, 0),
        "abajo": (1, 0),
        "izquierda": (0, -1),
        "derecha": (0, 1)
    }
    
    for direccion, (df, dc) in desplazamientos.items():
        nueva_fila, nueva_col = fila + df, col + dc
        if 0 <= nueva_fila < 3 and 0 <= nueva_col < 3:  # Validamos que no se salga del tablero
            # Crear un nuevo tablero con el movimiento aplicado
            nuevo_tablero = [list(fila) for fila in tablero]  # Copia del tablero actual
            nuevo_tablero[fila][col], nuevo_tablero[nueva_fila][nueva_col] = nuevo_tablero[nueva_fila][nueva_col], nuevo_tablero[fila][col]
            movimientos.append((tuple(tuple(fila) for fila in nuevo_tablero), direccion))
    
    return movimientos

def buscar_solucion_bfs(estado_inicial):
    """Algoritmo de búsqueda a lo ancho (BFS) para resolver el 8-puzzle."""
    cola = deque([(estado_inicial, [])])  # Cola para BFS con (estado_actual, movimientos_realizados)
    visitados = set()
    visitados.add(estado_inicial)
    total_movimientos = 0  # Contador de movimientos
    
    while cola:
        estado_actual, camino = cola.popleft()  # Extraemos el primer estado de la cola
        print("Estado actual:")
        imprimir_tablero(estado_actual)
        
        # Si el estado actual es el objetivo, terminamos la búsqueda
        if estado_actual == ESTADO_OBJETIVO:
            print("¡Solución encontrada!")
            print("Total de movimientos realizados:", total_movimientos)
            return camino
        
        # Generar nuevos estados a partir del estado actual
        for nuevo_estado, movimiento in generar_movimientos(estado_actual):
            if nuevo_estado not in visitados:
                visitados.add(nuevo_estado)
                cola.append((nuevo_estado, camino + [movimiento]))
                total_movimientos += 1  # Incrementamos el contador por cada nuevo estado generado
                print("Movimiento:", movimiento)
                imprimir_tablero(nuevo_estado)
                
                if nuevo_estado == ESTADO_OBJETIVO:  # Si encontramos la solución, terminamos de inmediato
                    print("¡Solución encontrada!")
                    print("Total de movimientos realizados:", total_movimientos)
                    return camino + [movimiento]
    
    print("No se encontró solución.")
    return None

# Estado inicial del tablero (puede modificarse para probar distintos casos)
ESTADO_INICIAL = (
    (8, 1, 3),
    (7, '_', 5),
    (6, 2, 4)
)

# Ejecutamos la búsqueda BFS
buscar_solucion_bfs(ESTADO_INICIAL)
