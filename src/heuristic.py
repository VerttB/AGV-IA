Posicao = tuple[int, int]


def manhattan(a: Posicao, b: Posicao) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
