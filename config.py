<<<<<<< HEAD
import random
from simpleai.search import (
    astar,
    breadth_first,
    depth_first,
    uniform_cost,
    greedy,
)


ALGORITIMOS = [
    ("Largura", breadth_first),
    ("Profundidade", depth_first),
    ("CustoUniforme", uniform_cost),
    ("Gulosa", greedy),
    ("AStar", astar),
]
=======
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
>>>>>>> 99ad6e861d17be7cf0affb0b49c2a9a4c3c068a3

MAPA = (75, 75)
INICIO = (random.randint(0, 5), random.randint(0, 5))
COLETA = (random.randint(30, 40), random.randint(30, 40))
DOCAS = [(10, 70), (30, 70), (50, 70), (70, 70)]

OBSTACULOS = set(
    map(lambda _: (random.randint(0, 74), random.randint(0, 74)), range(750))
)
CONGESTIONAMENTO = set(
    map(lambda _: (random.randint(10, 60), random.randint(10, 60)), range(400))
)


PACOTES = [
    {
        "id": 1,
        "doca": DOCAS[random.randint(0, 3)],
        "prio": random.randint(1, 2),
    },
    {
        "id": 2,
        "doca": DOCAS[random.randint(0, 3)],
        "prio": random.randint(1, 2),
    },
    {
        "id": 3,
        "doca": DOCAS[random.randint(0, 3)],
        "prio": random.randint(1, 2),
    },
]