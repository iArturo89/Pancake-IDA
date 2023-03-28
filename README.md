# Pancake-IDA

Este es un código en Python que utiliza el algoritmo IDA* para resolver el problema de reorganización de letras. 
Dado un estado inicial de una cadena de caracteres y un estado objetivo, 
el programa encuentra el camino más corto para reorganizar los caracteres en el estado inicial para llegar al estado objetivo.

Funciones

El programa incluye las siguientes funciones:

heuristic(estado: str) -> int: Esta función toma un estado de la cadena de caracteres y devuelve un valor entero que representa la heurística para ese estado. En este caso, la heurística es el número de caracteres que están fuera de lugar en comparación con el estado objetivo.

successors(estado: str) -> List[Tuple[str, int]]: Esta función genera los sucesores del estado actual. Para cada par de caracteres en la cadena, intercambia su posición y genera una nueva cadena. El costo para cada movimiento es 1.

ida_star(start_estado: str, estado_objetivo: str) -> Tuple[List[str], int]: Esta función toma el estado inicial y el estado objetivo y devuelve el camino más corto y su costo.

search(camino: List[str], g: int, limite: int, estado_objetivo: str) -> Union[str, int]: Esta función realiza una búsqueda en profundidad en la cadena de estados hasta que se alcanza el límite o se encuentra el estado objetivo. Devuelve "ENCONTRADO" si se encuentra el estado objetivo, el costo mínimo si no se encuentra el estado objetivo y el límite se actualiza con el costo mínimo.
