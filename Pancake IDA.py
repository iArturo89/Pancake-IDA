from typing import List, Tuple, Union

def heuristic(estado: str) -> int:
    # Heurística: cuenta el número de letras que están fuera de lugar
    count = 0
    for i in range(len(estado)):
        if estado[i] != estado_objetivo[i]:
            count += 1
    return count

def successors(estado: str) -> List[Tuple[str, int]]:
    # Genera los sucesores del estado actual
    succ = []
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            nuevo_estado = estado[:i] + estado[j] + estado[i+1:j] + estado[i] + estado[j+1:]
            cost = 1
            succ.append((nuevo_estado, cost))
    return succ

def ida_star(start_estado: str, estado_objetivo: str) -> Tuple[List[str], int]:
    limite = heuristic(start_estado)
    camino = [start_estado]
    while True:
        t = search(camino, 0, limite, estado_objetivo)
        if t == "ENCONTRADO":
            return camino, limite
        if t == float('inf'):
            return [], float('inf')
        limite = t

def search(camino: List[str], g: int, limite: int, estado_objetivo: str) -> Union[str, int]:
    node = camino[-1]
    f = g + heuristic(node)
    if f > limite:
        return f
    if node == estado_objetivo:
        return "ENCONTRADO"
    min_cost = float('inf')
    for succ, cost in successors(node):
        if succ not in camino:
            camino.append(succ)
            t = search(camino, g+cost, limite, estado_objetivo)
            if t == "ENCONTRADO":
                return "ENCONTRADO"
            if t < min_cost:
                min_cost = t
            camino.pop()
    return min_cost

# Ejemplo de uso:
estado_inicial = "dbca"
estado_objetivo = "abcd"
camino, costo = ida_star(estado_inicial, estado_objetivo)
print("Pasos:", len(camino) - 1)
print("Camino:", camino)
print("Costo:", costo)
