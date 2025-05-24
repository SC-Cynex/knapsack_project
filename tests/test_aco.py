import pytest
from knapsack import Item
from algorithms.ant_colony import calcular_informacao_heuristica, Ant

def test_calcular_informacao_heuristica():
    itens = [Item(peso=2, valor=4), Item(peso=1, valor=3), Item(peso=0, valor=5)]
    heuristica = calcular_informacao_heuristica(itens)
    assert len(heuristica) == len(itens)
    assert heuristica[0] == 2.0
    assert heuristica[1] == 3.0
    assert heuristica[2] > 0

def test_ant_adicionar_item_e_reset():
    item = Item(peso=2, valor=10, indice=0)
    formiga = Ant(num_itens=1)

    assert formiga.adicionar_item(0, item, capacidade_mochila=5)
    assert formiga.peso_atual == 2
    assert formiga.valor_atual == 10
    assert formiga.solucao[0] == 1

    formiga.reset()
    assert formiga.peso_atual == 0
    assert formiga.valor_atual == 0
    assert formiga.solucao == [0]
