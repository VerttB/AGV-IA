from .config import DOCAS, COLETA


def gerar_mapa_txt(path_total, prob, docas_lista, nome_arq):
    setas = {}
    for i in range(len(path_total) - 1):
        at, prox = path_total[i], path_total[i + 1]
        dx, dy = prox[0] - at[0], prox[1] - at[1]
        if dx == 1:
            setas[at] = "→"
        elif dx == -1:
            setas[at] = "←"
        elif dy == 1:
            setas[at] = "↑"
        elif dy == -1:
            setas[at] = "↓"

    with open(nome_arq, "w", encoding="utf-8") as f:
        f.write(f"Relatório de Missão: {nome_arq}\n")
        f.write("S=Início, G=Fim Missão, X=Obstáculo, ~=Tráfego, D=Doca, C=Coleta\n\n")
        for y in range(prob.grid_size[1] - 1, -1, -1):
            linha = f"{y:02d} |"
            for x in range(prob.grid_size[0]):
                p = (x, y)
                if p == path_total[0]:
                    linha += " S "
                elif p == path_total[-1]:
                    linha += " G "
                elif p == COLETA:
                    linha += " C "
                elif p in DOCAS:
                    linha += " D "
                elif p in setas:
                    linha += f" {setas[p]} "
                elif p in prob.obstacles:
                    linha += " X "
                elif p in prob.congestion_zones:
                    linha += " ~ "
                else:
                    linha += " . "
            f.write(linha + "\n")
