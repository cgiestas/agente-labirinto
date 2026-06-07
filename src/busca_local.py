import random
import math
import time
import itertools
import matplotlib.pyplot as plt

from src.busca_classica import (
    TenhoQueExplorar_Prioridade, 
    executar_busca_classica,
)

dicionario_real = {}

def construir_gps(matriz, pontos_mapeados):

    gps = {}

    for origem, destino in itertools.permutations(pontos_mapeados.keys(), 2):
        coord_origem = pontos_mapeados[origem]
        coord_destino = pontos_mapeados[destino]

        dados_labirinto = {
            "matriz": matriz,
            "inicio": coord_origem,
            "objetivo": coord_destino
        }

        fila = TenhoQueExplorar_Prioridade(criterio="total_f")

        resultado = executar_busca_classica(dados_labirinto, fila)

        if resultado["sucesso"]:
            gps[(origem, destino)] = resultado["custo"]
        else:
            gps[(origem, destino)] = 99999

    return gps

def func_custo (ordem_coleta):

    custo_total = 0

    ponto_atual = 'A'

    primeira_coleta = ordem_coleta[0]

    custo_total += dicionario_real.get((ponto_atual, primeira_coleta), 999)


    for i in range(len(ordem_coleta) -1):
        origem = ordem_coleta[i]
        destino = ordem_coleta[i+1]
        custo_total += dicionario_real.get((origem, destino), 999)

    ultima_coleta = ordem_coleta[-1]


    custo_total += dicionario_real.get((ultima_coleta, 'B'), 999)

    return custo_total

def gerar_vizinho(solucao_atual):
    vizinho = solucao_atual.copy()

    a1, a2 = random.sample(range(len(vizinho)), 2)

    vizinho[a1], vizinho[a2] = vizinho[a2], vizinho[a1]

    return vizinho

def hill_climbing(solucao_inicial, max_iteracoes=999):
    solucao_atual = solucao_inicial
    custo_atual = func_custo(solucao_atual)
    historico_custos = []
    historico_custos.append(custo_atual)

    for i in range(max_iteracoes):
        novo_vizinho = gerar_vizinho(solucao_atual)
        custo_vizinho = func_custo(novo_vizinho)
        if (custo_vizinho < custo_atual):
            solucao_atual = novo_vizinho
            custo_atual = func_custo(solucao_atual)
            historico_custos.append(custo_atual)

    return solucao_atual, custo_atual, historico_custos

def simulated_annealing(solucao_inicial, temp_inicial=100.0, taxa_resfriamento=0.99):
    solucao_atual = solucao_inicial
    custo_atual = func_custo(solucao_atual)
    temperatura = temp_inicial
    historico_custos = []
    historico_custos.append(custo_atual)

    while temperatura > 0.01:
        novo_vizinho = gerar_vizinho(solucao_atual)
        custo_vizinho = func_custo(novo_vizinho)
        diferenca = custo_vizinho - custo_atual
        if diferenca < 0:
            solucao_atual = novo_vizinho
            custo_atual = custo_vizinho
            historico_custos.append(custo_atual)

        if diferenca > 0:
            aux = diferenca / temperatura
            p = math.exp(-aux)
            aleatorio = random.random()
            if aleatorio < p:
                solucao_atual = novo_vizinho
                custo_atual = custo_vizinho
                historico_custos.append(custo_atual)
        temperatura = temperatura * taxa_resfriamento

    return solucao_atual, custo_atual, historico_custos

def teste(funcao_busca, pontos_coleta, repeticoes=30):
    custos_finais = []
    tempos_execucao = []
    todas_iteracoes = []

    melhor_custo_global = float('inf')
    pior_custo_global = float('-inf')
    melhor_historico_convergencia = []

    print(f"Iniciando {repeticoes} execucoes. Aguarde...")

    for i in range(repeticoes):
        solucao_inicial = pontos_coleta.copy()
        random.shuffle(solucao_inicial)

        tempo_inicio = time.time()

        solucao_final, custo_final, historico = funcao_busca(solucao_inicial)

        tempo_fim = time.time()
        tempo_gasto = tempo_fim - tempo_inicio

        custos_finais.append(custo_final)
        tempos_execucao.append(tempo_gasto)
        todas_iteracoes.append(len(historico) - 1)

        if custo_final < melhor_custo_global:
            melhor_custo_global = custo_final
            melhor_historico_convergencia = historico

        if custo_final > pior_custo_global:
            pior_custo_global = custo_final

    custo_medio = sum(custos_finais) / repeticoes
    tempo_medio = sum(tempos_execucao) / repeticoes
    iteracoes_medias = sum(todas_iteracoes) / repeticoes

    qtd_sucesso = custos_finais.count(melhor_custo_global)
    taxa_sucesso = (qtd_sucesso / repeticoes) * 100

    print("="*40)
    print(f"METRICAS OBRIGATORIAS ({repeticoes} Rodadas)")
    print(f"Melhor custo: {melhor_custo_global}")
    print(f"Pior custo: {pior_custo_global}")
    print(f"Custo medio: {custo_medio:.2f}")
    print(f"Tempo medio: {tempo_medio:.6f} segundos")
    print(f"Iteracoes medias: {iteracoes_medias:.1f} passos aceitos")
    print(f"Taxa de Sucesso: {taxa_sucesso:.1f}%")
    print("="*40 + "\n")

    return melhor_historico_convergencia


def gerar_grafico_convergencia(historico_hc, historico_sa):

    plt.figure(figsize=(10, 6))

    plt.plot(historico_hc, label='Hill-Climbing', color='blue', linewidth=2, marker='o')

    plt.plot(historico_sa, label='Simulated Annealing', color='red', linewidth=2, marker='x', linestyle='--')
    
    plt.title('Curva de Convergencia da Busca Local', fontsize=14)

    plt.xlabel('Iteracoes (Passos aceitos)', fontsize=12)

    plt.ylabel('Custo da Rota (Menor e melhor)', fontsize=12)

    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()

    plt.tight_layout()
    plt.savefig('grafico_convergencia.png')
    print("\nGrafico 'grafico_convergencia.png' gerado com sucesso!")
    plt.show()