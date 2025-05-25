import random
from typing import List, Tuple
from models.item import Item
from controllers.problem_controller import ProblemController
import logging

# Configura logging para depuração
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AntColonyOptimizer:
    def __init__(self, params: dict):
        self.params = params

    class Ant:
        def __init__(self, num_items: int):
            self.solution = [0] * num_items
            self.total_weight = 0
            self.total_value = 0

        def add_item(self, item: Item, capacity: int) -> bool:
            """Tenta adicionar um item à solução"""
            if self.total_weight + item.weight <= capacity:
                self.solution[item.index] = 1
                self.total_weight += item.weight
                self.total_value += item.value
                return True
            return False

    def run(self, items: List[Item], capacity: int) -> Tuple[List[int], float]:
        """Executa o algoritmo ACO"""
        logger.info(f"Iniciando ACO com {len(items)} itens, capacidade {capacity}")
        
        # Pré-calcula densidades de valor
        value_densities = [item.value_density() for item in items]
        pheromones = [1.0] * len(items)
        best_solution = [0] * len(items)
        best_fitness = 0.0

        # Filtra itens que excedem a capacidade
        available_indices = [i for i in range(len(items)) if items[i].weight <= capacity]
        logger.info(f"Itens viáveis: {len(available_indices)}")

        for iteration in range(self.params['iterations']):
            logger.info(f"Iteração {iteration + 1}/{self.params['iterations']}")
            ants = [self.Ant(len(items)) for _ in range(self.params['ants'])]
            
            for ant_idx, ant in enumerate(ants):
                logger.debug(f"Construindo solução para formiga {ant_idx}")
                current_available = available_indices.copy()
                while current_available:
                    probabilities = [
                        (pheromones[i] ** self.params['alpha']) * 
                        (value_densities[i] ** self.params['beta'])
                        for i in current_available
                    ]
                    total_prob = sum(probabilities) or 1.0  # Evita divisão por zero
                    probabilities = [p / total_prob for p in probabilities]
                    
                    chosen_idx = random.choices(current_available, weights=probabilities, k=1)[0]
                    if not ant.add_item(items[chosen_idx], capacity):
                        current_available.remove(chosen_idx)  # Remove mesmo se não adicionado
                    else:
                        current_available.remove(chosen_idx)
                
                fitness = ProblemController.fitness_function(items, ant.solution, capacity)
                logger.debug(f"Fitness da formiga {ant_idx}: {fitness}")
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_solution = ant.solution.copy()
            
            # Atualização de feromônios
            for i in range(len(pheromones)):
                pheromones[i] *= (1 - self.params['evaporation'])
                for ant in ants:
                    if ant.solution[i] == 1:
                        pheromones[i] += ant.total_value / 100.0

        logger.info(f"Melhor fitness encontrado: {best_fitness}")
        return best_solution, best_fitness