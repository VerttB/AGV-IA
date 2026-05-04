import random

from .models import Posicao


def gerar_pacotes_aleatorios(quantidade, docas):
    return [
        {
            "id": pacote_id,
            "doca": random.choice(docas),
            "prio": random.randint(1, 3),
        }
        for pacote_id in range(1, quantidade + 1)
    ]


def formatar_posicao(pos: Posicao) -> str:
    return f"({pos[0]}, {pos[1]})"
