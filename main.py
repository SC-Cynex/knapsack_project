from models.problem import KnapsackProblem
from models.item import Item
from controllers.problem_controller import ProblemController
from controllers.algorithm_controller import AlgorithmController
from views.cli_view import CLIView
from utils.data_generator import DataGenerator
from utils.predefined_datasets import KnapsackDatasets
from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.ant_colony import AntColonyOptimizer
import time

class KnapsackSolverApp:
    def __init__(self):
        self.view = CLIView()
        self.predefined_datasets = KnapsackDatasets.get_predefined_sets()
        self.ga_params = AlgorithmController.DEFAULT_GA_PARAMS
        self.aco_params = AlgorithmController.DEFAULT_ACO_PARAMS

    def setup_problem(self):
        """Configura o problema conforme escolha do usuário"""
        choice = self.view.display_menu(
            "Definição do Problema",
            [
                "Entrada manual de dados",
                "Usar conjunto de teste pré-definido",
                "Gerar dados aleatórios"
            ]
        )

        if choice == "1":
            return self._setup_manual_problem()
        elif choice == "2":
            return self._select_test_set()
        elif choice == "3":
            return self._generate_random_problem()
        return None

    def _setup_manual_problem(self):
        """Configura problema com entrada manual"""
        try:
            weights = [int(w) for w in self.view.get_input("Pesos (separados por vírgula): ").split(",")]
            values = [int(v) for v in self.view.get_input("Valores (separados por vírgula): ").split(",")]
            capacity = int(self.view.get_input("Capacidade da mochila: "))
            
            return ProblemController.create_from_user_input(weights, values, capacity)
        except ValueError as e:
            self.view.show_error("Dados inválidos: " + str(e))
            return None

    def _select_test_set(self):
        """Seleciona um conjunto de teste pré-definido"""
        options = list(self.predefined_datasets.keys())
        choice = self.view.display_menu(
            "Conjuntos de Teste",
            [f"{name} ({data['description']})" for name, data in self.predefined_datasets.items()]
        )
        
        selected = options[int(choice)-1]
        data = self.predefined_datasets[selected]
        return KnapsackProblem(
            items=data["items"],
            capacity=data["capacity"],
            description=data["description"]
        )

    def _generate_random_problem(self):
        """Gera um problema aleatório"""
        try:
            num_items = int(self.view.get_input("Número de itens a gerar: "))
            items = DataGenerator.generate_random_items(num_items)
            capacity = DataGenerator.calculate_capacity(items)
            return KnapsackProblem(
                items=items,
                capacity=capacity,
                description=f"Problema aleatório ({num_items} itens)"
            )
        except ValueError as e:
            self.view.show_error("Valor inválido: " + str(e))
            return None

    def configure_algorithms(self):
        """Configura parâmetros dos algoritmos"""
        self.ga_params = self._get_algorithm_params("GA")
        self.aco_params = self._get_algorithm_params("ACO")

    def _get_algorithm_params(self, algo_type):
        """Obtém parâmetros para um algoritmo específico"""
        params = {}
        base_params = AlgorithmController.get_algorithm_params(algo_type)
        
        for param, default in base_params.items():
            while True:
                try:
                    value = self.view.get_input(
                        f"{algo_type} - {param} (padrão: {default}): ",
                        default=str(default)
                    )
                    params[param] = type(default)(value) if value else default
                    break
                except ValueError:
                    self.view.show_error(f"Valor inválido para {param}. Use {type(default).__name__}.")
        return params

    def run_algorithm(self, algorithm, problem):
        """Executa um algoritmo e mostra resultados"""
        start_time = time.time()
        try:
            solution, fitness = algorithm.run(problem.items, problem.capacity)
        except Exception as e:
            self.view.show_error(f"Erro durante execução: {str(e)}")
            return None, 0.0, 0.0
        exec_time = (time.time() - start_time) * 1000  # ms
        
        self.view.show_solution(solution, problem.items)
        self.view.show_metrics(fitness, exec_time)
        return solution, fitness, exec_time

    def compare_algorithms(self, problem):
        """Executa e compara ambos algoritmos"""
        ga = GeneticAlgorithm(self.ga_params)
        aco = AntColonyOptimizer(self.aco_params)
        
        self.view.show_message("\nExecutando Algoritmo Genético...")
        ga_solution, ga_fitness, ga_time = self.run_algorithm(ga, problem)
        
        self.view.show_message("\nExecutando Colônia de Formigas...")
        aco_solution, aco_fitness, aco_time = self.run_algorithm(aco, problem)
        
        self.view.show_comparison(
            ga_fitness, ga_time,
            aco_fitness, aco_time
        )

    def main_loop(self):
        """Loop principal da aplicação"""
        self.view.show_message("Bem-vindo ao Solucionador de Problemas da Mochila!")
        
        while True:
            choice = self.view.display_menu(
                "Menu Principal",
                [
                    "Resolver com Algoritmo Genético",
                    "Resolver com Colônia de Formigas",
                    "Comparar ambos algoritmos",
                    "Configurar parâmetros",
                    "Sair"
                ]
            )

            if choice == "5":
                self.view.show_message("Até logo!")
                break
                
            if choice == "4":
                self.configure_algorithms()
                continue
                
            problem = self.setup_problem()
            if not problem:
                continue
                
            self.view.show_problem(problem)
            
            if choice == "1":
                ga = GeneticAlgorithm(self.ga_params)
                self.run_algorithm(ga, problem)
            elif choice == "2":
                aco = AntColonyOptimizer(self.aco_params)
                self.run_algorithm(aco, problem)
            elif choice == "3":
                self.compare_algorithms(problem)
                
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    app = KnapsackSolverApp()
    app.main_loop()