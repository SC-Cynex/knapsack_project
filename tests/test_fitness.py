from knapsack import Item, funcao_aptidao

def test_funcao_aptidao_valida():
    itens = [Item(peso=1, valor=10), Item(peso=2, valor=20)]
    solucao = [1, 1]
    capacidade = 5
    resultado = funcao_aptidao(itens, solucao, capacidade)
    assert resultado == 30

def test_funcao_aptidao_invalida():
    itens = [Item(peso=3, valor=10), Item(peso=4, valor=20)]
    solucao = [1, 1]
    capacidade = 5
    resultado = funcao_aptidao(itens, solucao, capacidade)
    assert resultado == 0
