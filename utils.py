import random

from knapsack import Item

def gerar_dados_teste(num_itens, max_peso=100, max_valor=100):

    itens = []
    for i in range(num_itens):
        peso = random.randint(1, max_peso)
        valor = random.randint(1, max_valor)
        itens.append(Item(peso=peso, valor=valor, indice=i))
    return itens

def obter_conjuntos_de_teste():

    conjuntos = {}

    # Conjunto Pequeno (5 itens)
    itens_pequeno = [
        Item(peso=2, valor=3, indice=0),
        Item(peso=3, valor=4, indice=1),
        Item(peso=4, valor=5, indice=2),
        Item(peso=5, valor=6, indice=3),
        Item(peso=1, valor=2, indice=4)
    ]
    capacidade_pequeno = 7
    conjuntos["pequeno"] = {"itens": itens_pequeno, "capacidade": capacidade_pequeno, "descricao": "5 itens, capacidade 7"}

    # Conjunto Médio (10 itens)
    itens_medio = [
        Item(peso=10, valor=60, indice=0),
        Item(peso=20, valor=100, indice=1),
        Item(peso=30, valor=120, indice=2),
        Item(peso=15, valor=70, indice=3),
        Item(peso=25, valor=110, indice=4),
        Item(peso=35, valor=150, indice=5),
        Item(peso=5, valor=30, indice=6),
        Item(peso=40, valor=160, indice=7),
        Item(peso=50, valor=200, indice=8),
        Item(peso=12, valor=50, indice=9)
    ]
    capacidade_medio = 100
    conjuntos["medio"] = {"itens": itens_medio, "capacidade": capacidade_medio, "descricao": "10 itens, capacidade 100"}

    return conjuntos