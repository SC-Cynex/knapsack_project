from typing import List
from models.item import Item
from models.problem import KnapsackProblem

class CLIView:
    @staticmethod
    def show_message(message: str):
        """Exibe uma mensagem genérica"""
        print(message)

    @staticmethod
    def show_error(error_msg: str):
        """Exibe mensagens de erro"""
        print(f"Erro: {error_msg}")

    @staticmethod
    def display_menu(title: str, options: List[str]) -> str:
        """Mostra um menu e retorna a escolha"""
        print(f"\n--- {title} ---")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        return input("Sua escolha: ")

    @staticmethod
    def get_input(prompt: str, default: str = "") -> str:
        """Obtém entrada do usuário com valor padrão"""
        user_input = input(f"{prompt} ")
        return user_input if user_input else default

    @staticmethod
    def show_problem(problem: KnapsackProblem):
        """Exibe informações do problema"""
        print(f"\n🔷 Problema: {problem.description}")
        print(f"📦 Capacidade: {problem.capacity}")
        print(f"🧮 Total de itens: {problem.total_items}")

    @staticmethod
    def show_solution(solution: List[int], items: List[Item]):
        """Exibe a solução encontrada"""
        print("\n🔹 Itens selecionados:")
        for i, selected in enumerate(solution):
            if selected == 1:
                print(f"  - {items[i]}")

    @staticmethod
    def show_metrics(fitness: float, exec_time: float):
        """Exibe métricas de desempenho"""
        print(f"\n📊 Aptidão: {fitness:.2f}")
        print(f"⏱️ Tempo de execução: {exec_time:.2f} ms")

    @staticmethod
    def show_comparison(ga_fitness: float, ga_time: float,
                       aco_fitness: float, aco_time: float):
        """Compara resultados de algoritmos"""
        print("\n⚖️ Comparação:")
        print(f"Algoritmo Genético - Aptidão: {ga_fitness:.2f}, Tempo: {ga_time:.2f} ms")
        print(f"Colônia de Formigas - Aptidão: {aco_fitness:.2f}, Tempo: {aco_time:.2f} ms")
        if ga_fitness > aco_fitness:
            print("✅ Algoritmo Genético teve melhor desempenho")
        elif aco_fitness > ga_fitness:
            print("✅ Colônia de Formigas teve melhor desempenho")
        else:
            print("⚡ Ambos tiveram desempenho equivalente")