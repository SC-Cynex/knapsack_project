import pytest
import random
from algorithms.genetic_algorithm import (
    criar_individuo,
    criar_populacao_inicial,
    crossover_um_ponto,
    mutacao_bit_flip,
)
from knapsack import Item, funcao_aptidao

def test_criar_individuo():
    individuo = criar_individuo(5)
    assert len(individuo) == 5
    assert all(gene in [0, 1] for gene in individuo)

def test_criar_populacao_inicial():
    populacao = criar_populacao_inicial(10, 6)
    assert len(populacao) == 10
    assert all(len(ind) == 6 for ind in populacao)

def test_crossover_um_ponto():
    pai1 = [1, 1, 1, 1]
    pai2 = [0, 0, 0, 0]
    filho1, filho2 = crossover_um_ponto(pai1, pai2)
    assert len(filho1) == len(pai1)
    assert len(filho2) == len(pai2)
    assert any(gene == 1 for gene in filho1) or any(gene == 0 for gene in filho1)
    assert any(gene == 1 for gene in filho2) or any(gene == 0 for gene in filho2)

def test_mutacao_bit_flip():
    individuo = [1, 1, 1, 1]
    mutado = mutacao_bit_flip(individuo, taxa_mutacao=1.0)
    assert all(gene == 0 for gene in mutado)

    individuo = [0, 0, 0, 0]
    mutado = mutacao_bit_flip(individuo, taxa_mutacao=0.0)
    assert mutado == individuo
