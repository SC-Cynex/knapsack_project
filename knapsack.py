class Item:

    def __init__(self, peso, valor, indice=0):
        self.peso = peso
        self.valor = valor
        self.indice = indice

    def __repr__(self):
        return f"Item(indice={self.indice}, peso={self.peso}, valor={self.valor})"

def calcular_valor_peso_total(itens, solucao):

    valor_total = 0
    peso_total = 0
    for i, item_incluido in enumerate(solucao):
        if item_incluido == 1:
            valor_total += itens[i].valor
            peso_total += itens[i].peso
    return valor_total, peso_total

def funcao_aptidao(itens, solucao, capacidade_mochila):

    valor_total, peso_total = calcular_valor_peso_total(itens, solucao)

    if peso_total > capacidade_mochila:
        return 0
    else:
        return valor_total

