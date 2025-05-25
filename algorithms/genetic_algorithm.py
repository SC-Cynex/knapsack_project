from controllers.problem_controller import ProblemController
from typing import List, Tuple
from models.item import Item
import random

class GeneticAlgorithm:
    def __init__(self, params: dict):
        self.params = params

    def _initialize_population(self, num_items: int) -> List[List[int]]:
        return [[random.randint(0, 1) for _ in range(num_items)] 
                for _ in range(self.params['population_size'])]

    def _selection(self, population: List[List[int]], fitness: List[float]) -> List[int]:
        """Seleciona um indivíduo usando torneio"""
        tournament_size = 3
        tournament = random.sample(list(zip(population, fitness)), tournament_size)
        return max(tournament, key=lambda x: x[1])[0]

    def _crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """Realiza crossover de um ponto"""
        if random.random() < self.params['crossover_rate']:
            point = random.randint(1, len(parent1) - 1)
            return parent1[:point] + parent2[point:]
        return parent1.copy()

    def _mutation(self, individual: List[int]) -> List[int]:
        """Realiza mutação bit a bit"""
        return [1 - bit if random.random() < self.params['mutation_rate'] else bit 
                for bit in individual]

    def run(self, items: List[Item], capacity: int) -> Tuple[List[int], float]:
        population = self._initialize_population(len(items))
        best_solution = population[0]
        best_fitness = 0.0

        for _ in range(self.params['generations']):
            # Calcula fitness para cada indivíduo
            fitness = [ProblemController.fitness_function(items, ind, capacity) 
                      for ind in population]
            
            # Encontra melhor solução
            best_idx = fitness.index(max(fitness))
            if fitness[best_idx] > best_fitness:
                best_fitness = fitness[best_idx]
                best_solution = population[best_idx].copy()
            
            # Nova população
            new_population = [best_solution]  # Elitismo
            while len(new_population) < self.params['population_size']:
                parent1 = self._selection(population, fitness)
                parent2 = self._selection(population, fitness)
                offspring = self._crossover(parent1, parent2)
                offspring = self._mutation(offspring)
                new_population.append(offspring)
            
            population = new_population

        return best_solution, best_fitness