from pathlib import Path
from simpleai.search import (
    astar,
    breadth_first,
    depth_first,
    uniform_cost,
    greedy,
)

ALGORITMOS = [
    ("Largura", breadth_first),
    ("Profundidade", depth_first),
    ("CustoUniforme", uniform_cost),
    ("Gulosa", greedy),
    ("AStar", astar),
]

RESULTADOS_DIR = Path("resultados")

N_PACOTES = 3
N_EXECUCOES = 50
GRID_SIZE = (75, 75)
DOCAS = [(5, 45), (20, 45), (35, 45), (45, 45)]
N_OBSTACULOS = 300
N_CONGESTIONAMENTOS = 200
