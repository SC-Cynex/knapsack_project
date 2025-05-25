from typing import Dict, Any
from models.problem import KnapsackProblem

class AlgorithmController:
    DEFAULT_GA_PARAMS = {
        'population_size': 50,
        'generations': 100,
        'crossover_rate': 0.8,
        'mutation_rate': 0.01
    }

    DEFAULT_ACO_PARAMS = {
        'ants': 10,
        'iterations': 20,
        'alpha': 1.0,
        'beta': 2.0,
        'evaporation': 0.5
    }

    @classmethod
    def get_algorithm_params(cls, algorithm_type: str) -> Dict[str, Any]:
        """Retorna parâmetros padrão ou customizados"""
        if algorithm_type == 'GA':
            return cls.DEFAULT_GA_PARAMS
        elif algorithm_type == 'ACO':
            return cls.DEFAULT_ACO_PARAMS
        raise ValueError("Algoritmo não suportado")