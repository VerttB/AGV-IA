# Analise dos Resultados dos Algoritmos de Busca

## Tabela de resultados

| Algoritmo | Custo medio | Custo min | Custo max | Tempo medio | Tempo min | Tempo max | Nos medio | Nos min | Nos max | Sucessos | Falhas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Largura | 393.98 | 104.00 | 869.00 | 0.099757 | 0.028076 | 0.163435 | 7025.08 | 2254 | 12014 | 50 | 0 |
| Profundidade | 3958.74 | 1404.00 | 6895.00 | 0.530726 | 0.074230 | 0.869861 | 7250.70 | 1699 | 11129 | 50 | 0 |
| CustoUniforme | 229.18 | 94.00 | 401.00 | 0.250991 | 0.059027 | 0.433050 | 6890.18 | 1932 | 11780 | 50 | 0 |
| Gulosa | 429.44 | 119.00 | 907.00 | 0.006726 | 0.001971 | 0.014735 | 249.34 | 103 | 435 | 50 | 0 |
| AStar | 229.18 | 94.00 | 401.00 | 0.051103 | 0.004240 | 0.193104 | 1156.66 | 206 | 2840 | 50 | 0 |

## Interpretacao geral

Todos os algoritmos tiveram 50 sucessos e 0 falhas. Portanto, todos conseguiram encontrar uma solucao em todas as execucoes. A diferenca principal entre eles esta na qualidade da solucao encontrada, no tempo gasto e na quantidade de nos explorados.

O algoritmo A* apresentou o melhor equilibrio geral. Ele encontrou o mesmo custo medio do Custo Uniforme, 229.18, mas com tempo medio muito menor e expandindo bem menos nos. Isso indica que a heuristica ajudou a direcionar a busca para regioes mais promissoras do espaco de estados.

O Custo Uniforme tambem encontrou as melhores solucoes em termos de custo, empatando com o A*. Isso e esperado, pois esse algoritmo sempre prioriza o menor custo acumulado. A desvantagem e que ele explorou muitos nos e teve tempo medio maior que o A*.

A Busca em Largura teve custo medio 393.98, pior que A* e Custo Uniforme. Esse resultado e esperado quando as acoes possuem custos diferentes, pois a largura busca a solucao com menor numero de passos, nao necessariamente a solucao de menor custo total.

A Busca em Profundidade teve o pior custo medio, 3958.74. Ela encontrou solucoes, mas geralmente solucoes muito caras. Isso acontece porque a profundidade segue caminhos longos sem considerar custo acumulado nem proximidade real do objetivo.

A Busca Gulosa foi a mais rapida, com tempo medio de apenas 0.006726 segundos, e expandiu poucos nos em media. No entanto, seu custo medio foi 429.44, maior que o de A*, Custo Uniforme e Largura. Isso ocorre porque a busca gulosa considera apenas a heuristica, sem levar em conta o custo ja acumulado.

## Resultado esperado

Sim, os resultados sao coerentes com o comportamento esperado desses tipos de busca.

A* e Custo Uniforme apresentarem o mesmo custo medio e um bom sinal, especialmente se a heuristica usada pelo A* for admissivel ou consistente. Nesse caso, o A* preserva a otimalidade, mas tende a explorar menos nos que o Custo Uniforme.

A Busca Gulosa ser a mais rapida tambem e esperado, pois ela usa a heuristica de forma agressiva para escolher o proximo estado. O custo maior mostra a principal limitacao desse metodo: ele e eficiente, mas nao garante a solucao otima.

A Busca em Largura ter custo pior que A* e Custo Uniforme tambem e normal quando os custos das acoes variam. Ela seria mais adequada em problemas nos quais cada passo tem o mesmo custo.

A Busca em Profundidade ter custo muito alto tambem e esperado. Ela nao e uma boa escolha quando a qualidade da solucao depende do custo do caminho, pois pode encontrar o objetivo por trajetos longos e ruins.

## Conclusao

O A* foi o algoritmo mais eficiente no conjunto de testes, pois encontrou solucoes otimas como o Custo Uniforme, mas com muito menos tempo e menos nos explorados.

A Busca Gulosa foi a mais rapida, mas sacrificou qualidade da solucao. A Busca em Largura funcionou corretamente, mas nao foi ideal para custos variados. A Busca em Profundidade foi a pior em qualidade das solucoes encontradas.

Em resumo:

- Melhor qualidade de solucao: A* e Custo Uniforme.
- Melhor equilibrio entre custo, tempo e nos explorados: A*.
- Mais rapido: Busca Gulosa.
- Menos indicado para custos variados: Busca em Largura.
- Pior qualidade media: Busca em Profundidade.
