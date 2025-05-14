import random

from knapsack import funcao_aptidao

def criar_individuo(num_itens):

    return [random.randint(0, 1) for _ in range(num_itens)]

def criar_populacao_inicial(tamanho_populacao, num_itens):

    return [criar_individuo(num_itens) for _ in range(tamanho_populacao)]

def selecionar_pais_torneio(populacao, aptidoes, k=3):

    selecao = random.sample(list(zip(populacao, aptidoes)), k)
    selecao.sort(key=lambda x: x[1], reverse=True)
    return selecao[0][0]

def crossover_um_ponto(pai1, pai2):

    num_itens = len(pai1)
    if num_itens < 2:
        return pai1[:], pai2[:]
    ponto_corte = random.randint(1, num_itens - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao_bit_flip(individuo, taxa_mutacao):

    mutado = individuo[:]
    for i in range(len(mutado)):
        if random.random() < taxa_mutacao:
            mutado[i] = 1 - mutado[i]
    return mutado

def algoritmo_genetico(itens, capacidade_mochila, tamanho_populacao=50, num_geracoes=100, taxa_crossover=0.8, taxa_mutacao=0.01):

    num_itens = len(itens)
    populacao = criar_populacao_inicial(tamanho_populacao, num_itens)
    
    melhor_solucao_global = None
    melhor_aptidao_global = -1

    for geracao in range(num_geracoes):
        aptidoes = [funcao_aptidao(itens, ind, capacidade_mochila) for ind in populacao]

        for i in range(tamanho_populacao):
            if aptidoes[i] > melhor_aptidao_global:
                melhor_aptidao_global = aptidoes[i]
                melhor_solucao_global = populacao[i][:]
        
        nova_populacao = []

        if melhor_solucao_global:
            nova_populacao.append(melhor_solucao_global[:]) 

        while len(nova_populacao) < tamanho_populacao:
            pai1 = selecionar_pais_torneio(populacao, aptidoes)
            pai2 = selecionar_pais_torneio(populacao, aptidoes)
            
            filho1, filho2 = pai1, pai2
            if random.random() < taxa_crossover:
                filho1, filho2 = crossover_um_ponto(pai1, pai2)
            
            nova_populacao.append(mutacao_bit_flip(filho1, taxa_mutacao))
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(mutacao_bit_flip(filho2, taxa_mutacao))
        
        populacao = nova_populacao

    return melhor_solucao_global, melhor_aptidao_global