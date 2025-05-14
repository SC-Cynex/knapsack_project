import random

from knapsack import funcao_aptidao, calcular_valor_peso_total

class Ant:

    def __init__(self, num_itens):
        self.num_itens = num_itens
        self.solucao = [0] * num_itens
        self.peso_atual = 0
        self.valor_atual = 0
        self.itens_visitados_indices = []

    def adicionar_item(self, item_index, item_obj, capacidade_mochila):

        if self.solucao[item_index] == 0 and self.peso_atual + item_obj.peso <= capacidade_mochila:
            self.solucao[item_index] = 1
            self.peso_atual += item_obj.peso
            self.valor_atual += item_obj.valor
            self.itens_visitados_indices.append(item_index)
            return True
        return False

    def reset(self):
        self.solucao = [0] * self.num_itens
        self.peso_atual = 0
        self.valor_atual = 0
        self.itens_visitados_indices = []

    def get_aptidao(self, itens, capacidade_mochila):

        if self.peso_atual > capacidade_mochila:
            return 0
        return self.valor_atual

def calcular_informacao_heuristica(itens):

    heuristica = []
    for item in itens:
        if item.peso > 0:
            heuristica.append(item.valor / item.peso)
        else:
            heuristica.append(item.valor / 0.0001 if item.valor > 0 else 0.0001) 
    return heuristica

def algoritmo_aco(itens, capacidade_mochila, num_formigas=10, num_iteracoes=50, alfa=1.0, beta=2.0, taxa_evaporacao=0.5, q=100.0, feromonio_inicial=1.0):

    num_itens = len(itens)
    if num_itens == 0:
        return [], 0

    feromonios = [feromonio_inicial] * num_itens
    heuristica = calcular_informacao_heuristica(itens)

    melhor_solucao_global = [0] * num_itens
    melhor_aptidao_global = 0

    colonia = [Ant(num_itens) for _ in range(num_formigas)]

    for iteracao in range(num_iteracoes):
        for formiga in colonia:
            formiga.reset()
            itens_disponiveis_indices = list(range(num_itens))
            random.shuffle(itens_disponiveis_indices)

            while True:
                probabilidades = []
                soma_prob_denom = 0.0
                itens_viaveis_para_escolha = []

                for i in itens_disponiveis_indices:
                    if formiga.solucao[i] == 0 and formiga.peso_atual + itens[i].peso <= capacidade_mochila:

                        tau_i = feromonios[i]
                        eta_i = heuristica[i]
                        prob_numerador = (tau_i ** alfa) * (eta_i ** beta)
                        probabilidades.append((i, prob_numerador))
                        soma_prob_denom += prob_numerador
                        itens_viaveis_para_escolha.append(i)
                
                if not itens_viaveis_para_escolha or soma_prob_denom == 0:
                    break

                rand_val = random.uniform(0, soma_prob_denom)
                soma_acumulada = 0.0
                item_escolhido_idx = -1

                for item_idx, prob_num in probabilidades:
                    prob_item = prob_num / soma_prob_denom
                    soma_acumulada += prob_item
                    if rand_val <= soma_acumulada:
                        item_escolhido_idx = item_idx
                        break
                
                if item_escolhido_idx != -1:
                    formiga.adicionar_item(item_escolhido_idx, itens[item_escolhido_idx], capacidade_mochila)
                    itens_disponiveis_indices.remove(item_escolhido_idx)
                else:
                    break
        
        for formiga in colonia:
            aptidao_atual = formiga.get_aptidao(itens, capacidade_mochila)
            if aptidao_atual > melhor_aptidao_global:
                melhor_aptidao_global = aptidao_atual
                melhor_solucao_global = formiga.solucao[:]

        for i in range(num_itens):
            feromonios[i] *= (1.0 - taxa_evaporacao)


        for formiga in colonia:
            aptidao_formiga = formiga.get_aptidao(itens, capacidade_mochila)
            if aptidao_formiga > 0:
                for i in range(num_itens):
                    if formiga.solucao[i] == 1:
                        feromonios[i] += (q / (aptidao_formiga + 0.0001))
                        feromonios[i] += (q * aptidao_formiga) / (melhor_aptidao_global + 1e-9)

    return melhor_solucao_global, melhor_aptidao_global


