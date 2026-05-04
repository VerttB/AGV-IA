from statistics import mean


def criar_estatisticas(algoritmos):
    return {
        nome: {
            "custos": [],
            "tempos": [],
            "nos_expandidos": [],
            "sucessos": 0,
            "falhas": 0,
        }
        for nome, _ in algoritmos
    }


def registrar_resultado(estatisticas, resultado):
    dados = estatisticas[resultado.algoritmo]
    dados["nos_expandidos"].append(resultado.nos_expandidos)

    if resultado.sucesso:
        dados["custos"].append(resultado.custo)
        dados["tempos"].append(resultado.tempo)
        dados["sucessos"] += 1
    else:
        dados["falhas"] += 1


def resumir_estatisticas(estatisticas):
    resumo = []
    for nome, dados in estatisticas.items():
        custos = dados["custos"]
        tempos = dados["tempos"]
        nos_expandidos = dados["nos_expandidos"]

        resumo.append(
            {
                "algoritmo": nome,
                "custo_medio": mean(custos) if custos else None,
                "custo_min": min(custos) if custos else None,
                "custo_max": max(custos) if custos else None,
                "tempo_medio": mean(tempos) if tempos else None,
                "tempo_min": min(tempos) if tempos else None,
                "tempo_max": max(tempos) if tempos else None,
                "nos_expandidos_medio": mean(nos_expandidos)
                if nos_expandidos
                else None,
                "nos_expandidos_min": min(nos_expandidos) if nos_expandidos else None,
                "nos_expandidos_max": max(nos_expandidos) if nos_expandidos else None,
                "sucessos": dados["sucessos"],
                "falhas": dados["falhas"],
            }
        )
    return resumo


def imprimir_tabela(resumo):
    print("\n" + "=" * 185)
    print(
        f"{'ALGORITMO':<16} | "
        f"{'CUSTO MEDIO':>12} | {'CUSTO MIN':>9} | {'CUSTO MAX':>9} | "
        f"{'TEMPO MEDIO':>12} | {'TEMPO MIN':>10} | {'TEMPO MAX':>10} | "
        f"{'NOS MEDIO':>10} | {'NOS MIN':>8} | {'NOS MAX':>8} | "
        f"{'SUCESSOS':>8} | {'FALHAS':>6}"
    )
    print("-" * 185)

    for linha in resumo:
        if linha["custo_medio"] is None:
            print(
                f"{linha['algoritmo']:<16} | "
                f"{'--':>12} | {'--':>9} | {'--':>9} | "
                f"{'--':>12} | {'--':>10} | {'--':>10} | "
                f"{_fmt_numero(linha['nos_expandidos_medio']):>10} | "
                f"{_fmt_numero(linha['nos_expandidos_min']):>8} | "
                f"{_fmt_numero(linha['nos_expandidos_max']):>8} | "
                f"{linha['sucessos']:>8} | {linha['falhas']:>6}"
            )
            continue

        print(
            f"{linha['algoritmo']:<16} | "
            f"{linha['custo_medio']:>12.2f} | {linha['custo_min']:>9.2f} | {linha['custo_max']:>9.2f} | "
            f"{linha['tempo_medio']:>12.6f} | {linha['tempo_min']:>10.6f} | {linha['tempo_max']:>10.6f} | "
            f"{_fmt_numero(linha['nos_expandidos_medio']):>10} | "
            f"{_fmt_numero(linha['nos_expandidos_min']):>8} | "
            f"{_fmt_numero(linha['nos_expandidos_max']):>8} | "
            f"{linha['sucessos']:>8} | {linha['falhas']:>6}"
        )

    print("=" * 185)


def _fmt_numero(valor):
    if valor is None:
        return "--"
    return f"{valor:.2f}" if isinstance(valor, float) else str(valor)
