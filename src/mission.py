import time

from .config import GRID_SIZE
from .instance import ordenar_pacotes
from .models import ResultadoMissao
from .models import AGVProblem


def extrair_caminho(resultado):
    return [state for _, state in resultado.path()]


def juntar_caminho(caminho_total, trecho):
    if not caminho_total:
        return list(trecho)
    return caminho_total + trecho[1:]


def executar_segmento(instancia, algoritmo, origem, destino):
    problema = AGVProblem(
        origem,
        destino,
        instancia.obstaculos,
        instancia.congestionamentos,
        GRID_SIZE,
    )
    resultado = algoritmo(problema, graph_search=True)
    return resultado, problema.nos_expandidos


def executar_missao(instancia, nome_algoritmo, algoritmo):
    """
    Executa a missao completa em segmentos.

    O AGV vai ao ponto de coleta uma unica vez e depois entrega os pacotes
    por ordem de prioridade. A missao termina na doca do ultimo pacote.
    """

    pacotes = ordenar_pacotes(instancia.pacotes)
    posicao_atual = instancia.inicio
    custo_total = 0
    caminho_total = []
    segmentos_resolvidos = 0
    nos_expandidos_total = 0
    inicio_tempo = time.perf_counter()

    try:
        resultado, nos_expandidos = executar_segmento(
            instancia,
            algoritmo,
            posicao_atual,
            instancia.coleta,
        )
        nos_expandidos_total += nos_expandidos
        if resultado is None:
            tempo_total = time.perf_counter() - inicio_tempo
            return ResultadoMissao(
                execucao=instancia.id_execucao,
                algoritmo=nome_algoritmo,
                sucesso=False,
                custo=None,
                tempo=tempo_total,
                caminho=caminho_total,
                pacotes=pacotes,
                distancia_percorrida=max(0, len(caminho_total) - 1),
                segmentos_resolvidos=segmentos_resolvidos,
                nos_expandidos=nos_expandidos_total,
                segmento_falha={
                    "tipo": "ate_coleta",
                    "origem": posicao_atual,
                    "destino": instancia.coleta,
                    "pacote": None,
                },
            )

        custo_total += resultado.cost
        segmentos_resolvidos += 1
        caminho_total = juntar_caminho(
            caminho_total,
            extrair_caminho(resultado),
        )
        posicao_atual = instancia.coleta

        for pacote in pacotes:
            resultado, nos_expandidos = executar_segmento(
                instancia,
                algoritmo,
                posicao_atual,
                pacote["doca"],
            )
            nos_expandidos_total += nos_expandidos
            if resultado is None:
                tempo_total = time.perf_counter() - inicio_tempo
                return ResultadoMissao(
                    execucao=instancia.id_execucao,
                    algoritmo=nome_algoritmo,
                    sucesso=False,
                    custo=None,
                    tempo=tempo_total,
                    caminho=caminho_total,
                    pacotes=pacotes,
                    distancia_percorrida=max(0, len(caminho_total) - 1),
                    segmentos_resolvidos=segmentos_resolvidos,
                    nos_expandidos=nos_expandidos_total,
                    segmento_falha={
                        "tipo": "ate_doca",
                        "origem": posicao_atual,
                        "destino": pacote["doca"],
                        "pacote": pacote,
                    },
                )

            custo_total += resultado.cost
            segmentos_resolvidos += 1
            caminho_total = juntar_caminho(
                caminho_total,
                extrair_caminho(resultado),
            )
            posicao_atual = pacote["doca"]

    except Exception as exc:
        tempo_total = time.perf_counter() - inicio_tempo
        return ResultadoMissao(
            execucao=instancia.id_execucao,
            algoritmo=nome_algoritmo,
            sucesso=False,
            custo=None,
            tempo=tempo_total,
            caminho=caminho_total,
            pacotes=pacotes,
            distancia_percorrida=max(0, len(caminho_total) - 1),
            segmentos_resolvidos=segmentos_resolvidos,
            nos_expandidos=nos_expandidos_total,
            erro=repr(exc),
        )

    tempo_total = time.perf_counter() - inicio_tempo
    return ResultadoMissao(
        execucao=instancia.id_execucao,
        algoritmo=nome_algoritmo,
        sucesso=True,
        custo=custo_total,
        tempo=tempo_total,
        caminho=caminho_total,
        pacotes=pacotes,
        distancia_percorrida=max(0, len(caminho_total) - 1),
        segmentos_resolvidos=segmentos_resolvidos,
        nos_expandidos=nos_expandidos_total,
    )
