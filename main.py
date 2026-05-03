import time
from src.config import (
    ALGORITIMOS,
    MAPA,
    INICIO,
    COLETA,
    DOCAS,
    OBSTACULOS,
    CONGESTIONAMENTO,
    PACOTES,
)

from src.models import AGVProblem
from src.map_renderer import gerar_mapa_txt

resumo_final = []


for p in [INICIO, COLETA] + DOCAS:
    OBSTACULOS.discard(p)
    CONGESTIONAMENTO.discard(p)

# Ordena os pacotes na prioridade
PACOTES.sort(
    key=lambda p: (
        p["prio"],
        abs(p["doca"][0] - COLETA[0]) + abs(p["doca"][1] - COLETA[1]),
    )
)


for nome, busca_func in ALGORITIMOS:
    print(f"Iniciando missão completa para: {nome}")
    pos_agv_viva = INICIO
    caminho_total_missao = []
    custo_total_missao = 0
    tempo_total_missao = 0
    sucesso_completo = True

    # O loop só para quando todos os pacotes forem entregues
    for pkg in PACOTES:
        t_segmento_start = time.perf_counter()

        # Segmento 1: Da posição atual até o ponto de coleta[cite: 2]
        prob_para_coleta = AGVProblem(
            pos_agv_viva, COLETA, OBSTACULOS, CONGESTIONAMENTO, MAPA
        )
        res_para_coleta = busca_func(prob_para_coleta, graph_search=True)

        if res_para_coleta:
            # Segmento 2: Do ponto de coleta até a doca designada[cite: 2]
            prob_para_doca = AGVProblem(
                COLETA, pkg["doca"], OBSTACULOS, CONGESTIONAMENTO, MAPA
            )
            res_para_doca = busca_func(prob_para_doca, graph_search=True)

            if res_para_doca:
                tempo_total_missao += time.perf_counter() - t_segmento_start
                custo_total_missao += res_para_coleta.cost + res_para_doca.cost
                # Concatena os caminhos no rastro total
                caminho_total_missao.extend(
                    [n[1] for n in res_para_coleta.path()]
                    + [n[1] for n in res_para_doca.path()][1:]
                )
                # O AGV agora está na doca; esta é sua nova posição inicial[cite: 4]
                pos_agv_viva = pkg["doca"]
            else:
                sucesso_completo = False
                break
        else:
            sucesso_completo = False
            break

    if sucesso_completo:
        resumo_final.append((nome, custo_total_missao, tempo_total_missao))
        gerar_mapa_txt(
            caminho_total_missao,
            prob_para_coleta,
            DOCAS,
            f"results/resultado_{nome}.txt",
        )
    else:
        resumo_final.append((nome, "FALHA NA MISSÃO", "N/A"))

print("\n" + "=" * 75)
print(f"{'ALGORITMO':<20} | {'CUSTO ACUMULADO':<20} | {'TEMPO DE EXECUÇÃO (s)':<20}")
print("-" * 75)
for n, c, t in resumo_final:
    t_val = f"{t:.6f}" if isinstance(t, float) else t
    print(f"{n:<20} | {str(c):<20} | {t_val:<20}")
print("=" * 75)
