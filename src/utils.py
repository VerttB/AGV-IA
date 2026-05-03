import random


def gerar_pacotes_aleatorios(quantidade, docas):
    return [
        {
            "id": pacote_id,
            "doca": random.choice(docas),
            "prio": random.randint(1, 3),
        }
        for pacote_id in range(1, quantidade + 1)
    ]
