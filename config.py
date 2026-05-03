N_EXECUCOES = 50
GRID_SIZE = (50, 50)
GOAL = (4, 0)  # Posição final do AGV
START = (0, 0)  # Posição inicial do AGV
MAP = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
]  # Grafo ou grid?

directions = [
    (0, 1),  # direita
    (0, -1),  # esquerda
    (1, 0),  # baixo
    (-1, 0),  # cima
]