from models.problem import KnapsackProblem
from models.item import Item
from typing import List, Tuple

class ProblemController:
    @staticmethod
    def calculate_solution_stats(items: List[Item], solution: List[int]) -> Tuple[int, int]:
        """Calcula (valor_total, peso_total) para uma solução"""
        total_value = sum(item.value for i, item in enumerate(items) if solution[i] == 1)
        total_weight = sum(item.weight for i, item in enumerate(items) if solution[i] == 1)
        return total_value, total_weight

    @staticmethod
    def fitness_function(items: List[Item], solution: List[int], capacity: int) -> float:
        """Função de aptidão que penaliza soluções inválidas"""
        total_value, total_weight = ProblemController.calculate_solution_stats(items, solution)
        return total_value if total_weight <= capacity else 0

    @staticmethod
    def create_from_user_input(weights: List[int], values: List[int], capacity: int) -> KnapsackProblem:
        """Cria um problema da mochila a partir de entrada manual"""
        if len(weights) != len(values):
            raise ValueError("O número de pesos deve ser igual ao número de valores")
        items = [Item(index=i, weight=w, value=v) for i, (w, v) in enumerate(zip(weights, values))]
        return KnapsackProblem(items=items, capacity=capacity, description="Problema da Mochila Manual")