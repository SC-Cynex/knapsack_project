from knapsack import Item, calcular_valor_peso_total, funcao_aptidao
from algorithms.genetic_algorithm import algoritmo_genetico
from algorithms.ant_colony import algoritmo_aco
from utils import gerar_dados_teste, obter_conjuntos_de_teste
import time

def obter_dados_problema(conjuntos_teste):

    print("\n--- Definição do Problema da Mochila ---")
    print("Como você gostaria de definir o problema?")
    print("1. Entrada manual de pesos, valores e capacidade")
    print("2. Usar um conjunto de dados de teste pré-definido")
    print("3. Gerar um conjunto de dados grande aleatoriamente")

    while True:
        escolha_fonte = input("Digite sua escolha (1-3): ")
        if escolha_fonte == "1":
            return obter_dados_problema_manual()
        elif escolha_fonte == "2":
            return selecionar_conjunto_teste(conjuntos_teste)
        elif escolha_fonte == "3":
            return gerar_dados_grandes_aleatorios()
        else:
            print("Escolha inválida. Tente novamente.")

def selecionar_conjunto_teste(conjuntos_teste):
    print("\n--- Selecione um Conjunto de Teste ---")
    opcoes = list(conjuntos_teste.keys())
    for i, key in enumerate(opcoes):
        print(f"{i+1}. {key.capitalize()} - {conjuntos_teste[key]['descricao']}")
    
    while True:
        try:
            escolha_idx = int(input(f"Digite o número do conjunto de teste (1-{len(opcoes)}): ")) - 1
            if 0 <= escolha_idx < len(opcoes):
                chave_selecionada = opcoes[escolha_idx]
                conjunto = conjuntos_teste[chave_selecionada]
                print(f"Conjunto '{chave_selecionada}' selecionado.")
                return conjunto["itens"], conjunto["capacidade"]
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def gerar_dados_grandes_aleatorios():
    print("\n--- Geração de Conjunto de Dados Grande ---")
    try:
        num_itens = int(input("Digite o número de itens a serem gerados (ex: 1000, 10000): "))
        if num_itens <= 0:
            print("O número de itens deve ser positivo.")
            return None, None
        
        itens = gerar_dados_teste(num_itens)
        peso_total_itens = sum(item.peso for item in itens)
        capacidade = int(peso_total_itens * 0.4)
        print(f"{num_itens} itens gerados aleatoriamente. Capacidade da mochila definida para {capacidade}.")
        return itens, capacidade
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para o número de itens.")
        return None, None

def obter_dados_problema_manual():

    print("\n--- Entrada Manual de Dados do Problema ---")
    try:
        pesos_str = input("Digite os pesos dos itens separados por vírgula (ex: 2,3,4,5): ")
        pesos = [int(p.strip()) for p in pesos_str.split(",")]

        valores_str = input("Digite os valores dos itens separados por vírgula (ex: 3,4,5,6): ")
        valores = [int(v.strip()) for v in valores_str.split(",")]

        if len(pesos) != len(valores):
            print("Erro: O número de pesos deve ser igual ao número de valores.")
            return None, None

        capacidade = int(input("Digite a capacidade da mochila: "))
        
        itens = [Item(peso=pesos[i], valor=valores[i], indice=i) for i in range(len(pesos))]
        return itens, capacidade
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de que pesos, valores e capacidade são números inteiros.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None, None

def mostrar_menu_algoritmos():

    print("\n--- Escolha o Algoritmo Bio-inspirado ---")
    print("1. Algoritmo Genético (GA)")
    print("2. Algoritmo de Colônia de Formigas (ACO)")
    print("3. Executar os algoritmos em paralelo para comparação")
    print("4. Sair")
    
    while True:
        escolha = input("Digite o número da sua escolha: ")
        if escolha in ["1", "2", "3", "4"]:
            return escolha
        else:
            print("Escolha inválida. Tente novamente.")

def main():

    print("Bem-vindo à Solução Interativa para o Problema da Mochila!")
    conjuntos_teste = obter_conjuntos_de_teste()

    while True:
        escolha_algoritmo = mostrar_menu_algoritmos()

        if escolha_algoritmo == '4':
            print("Saindo da aplicação. Até logo!")
            break
        
        itens, capacidade_mochila = obter_dados_problema(conjuntos_teste)
        if not itens or not capacidade_mochila:
            print("Não foi possível definir o problema. Voltando ao menu principal.")
            continue

        print(f"\n--- Problema Definido ---")
        if len(itens) <= 20:
             print(f"Itens: {itens}")
        else:
            print(f"Número de itens: {len(itens)}")
        print(f"Capacidade da mochila: {capacidade_mochila}")

        if escolha_algoritmo == '1':
            print("\n--- Configuração do Algoritmo Genético ---")
            try:
                tamanho_populacao_str = input(f"Digite o tamanho da população (padrão: 50): ")
                tamanho_populacao = int(tamanho_populacao_str) if tamanho_populacao_str else 50
                num_geracoes_str = input(f"Digite o número de gerações (padrão: 100): ")
                num_geracoes = int(num_geracoes_str) if num_geracoes_str else 100
                taxa_crossover_str = input(f"Digite a taxa de crossover (padrão: 0.8): ")
                taxa_crossover = float(taxa_crossover_str) if taxa_crossover_str else 0.8
                taxa_mutacao_str = input(f"Digite a taxa de mutação (padrão: 0.01): ")
                taxa_mutacao = float(taxa_mutacao_str) if taxa_mutacao_str else 0.01
            except ValueError:
                print("Erro: Parâmetros inválidos. Usando valores padrão para GA.")
                tamanho_populacao, num_geracoes, taxa_crossover, taxa_mutacao = 50, 100, 0.8, 0.01
            
            print(f"\nExecutando Algoritmo Genético com: Pop: {tamanho_populacao}, Ger: {num_geracoes}, Cross: {taxa_crossover}, Mut: {taxa_mutacao}")
            melhor_solucao, melhor_aptidao = algoritmo_genetico(itens, capacidade_mochila, tamanho_populacao, num_geracoes, taxa_crossover, taxa_mutacao)
            print(f"\n--- Resultados do Algoritmo Genético ---")
            if melhor_solucao:
                print(f"Melhor solução (binária): {melhor_solucao}")
                print(f"Itens selecionados (índice, peso, valor):")
                for i, sel in enumerate(melhor_solucao): 
                    if sel == 1: print(f"  - {itens[i]}")
                val_tot, peso_tot = calcular_valor_peso_total(itens, melhor_solucao)
                print(f"Valor total: {val_tot}, Peso total: {peso_tot}")
                print(f"Aptidão: {melhor_aptidao}")
            else:
                print("Nenhuma solução viável encontrada pelo GA.")

        elif escolha_algoritmo == '2':
            print("\n--- Configuração do Algoritmo de Colônia de Formigas (ACO) ---")
            try:
                num_formigas_str = input("Número de formigas (padrão: 10): ")
                num_formigas = int(num_formigas_str) if num_formigas_str else 10
                num_iteracoes_str = input("Número de iterações (padrão: 50): ")
                num_iteracoes = int(num_iteracoes_str) if num_iteracoes_str else 50
                alfa_str = input("Alfa (influência do feromônio, padrão: 1.0): ")
                alfa = float(alfa_str) if alfa_str else 1.0
                beta_str = input("Beta (influência da heurística, padrão: 2.0): ")
                beta = float(beta_str) if beta_str else 2.0
                taxa_evaporacao_str = input("Taxa de evaporação (rho, padrão: 0.5): ")
                taxa_evaporacao = float(taxa_evaporacao_str) if taxa_evaporacao_str else 0.5
                q_str = input("Q (constante de atualização do feromônio, padrão: 100.0): ")
                q_val = float(q_str) if q_str else 100.0
                feromonio_inicial_str = input("Feromônio inicial (padrão: 1.0): ")
                feromonio_inicial = float(feromonio_inicial_str) if feromonio_inicial_str else 1.0
            except ValueError:
                print("Erro: Parâmetros inválidos. Usando valores padrão para ACO.")
                num_formigas, num_iteracoes, alfa, beta, taxa_evaporacao, q_val, feromonio_inicial = 10, 50, 1.0, 2.0, 0.5, 100.0, 1.0

            print(f"\nExecutando ACO com: Formigas: {num_formigas}, Iter: {num_iteracoes}, Alfa: {alfa}, Beta: {beta}, Evap: {taxa_evaporacao}, Q: {q_val}, Fer. Ini: {feromonio_inicial}")
            melhor_solucao, melhor_aptidao = algoritmo_aco(itens, capacidade_mochila, num_formigas, num_iteracoes, alfa, beta, taxa_evaporacao, q_val, feromonio_inicial)
            print(f"\n--- Resultados do Algoritmo de Colônia de Formigas (ACO) ---")
            if melhor_solucao:
                print(f"Melhor solução (binária): {melhor_solucao}")
                print(f"Itens selecionados (índice, peso, valor):")
                for i, sel in enumerate(melhor_solucao): 
                    if sel == 1: print(f"  - {itens[i]}")
                val_tot, peso_tot = calcular_valor_peso_total(itens, melhor_solucao)
                print(f"Valor total: {val_tot}, Peso total: {peso_tot}")
                print(f"Aptidão: {melhor_aptidao}")
            else:
                print("Nenhuma solução viável encontrada pelo ACO.")
        elif escolha_algoritmo == '3':
            print("\n--- Executando ambos os algoritmos em paralelo ---")
            try:
                tamanho_populacao_str = input(f"Digite o tamanho da população (padrão: 50): ")
                tamanho_populacao = int(tamanho_populacao_str) if tamanho_populacao_str else 50
                num_geracoes_str = input(f"Digite o número de gerações (padrão: 100): ")
                num_geracoes = int(num_geracoes_str) if num_geracoes_str else 100
                taxa_crossover_str = input(f"Digite a taxa de crossover (padrão: 0.8): ")
                taxa_crossover = float(taxa_crossover_str) if taxa_crossover_str else 0.8
                taxa_mutacao_str = input(f"Digite a taxa de mutação (padrão: 0.01): ")
                taxa_mutacao = float(taxa_mutacao_str) if taxa_mutacao_str else 0.01

                num_formigas_str = input("Número de formigas (padrão: 10): ")
                num_formigas = int(num_formigas_str) if num_formigas_str else 10
                num_iteracoes_str = input("Número de iterações (padrão: 50): ")
                num_iteracoes = int(num_iteracoes_str) if num_iteracoes_str else 50
                alfa_str = input("Alfa (influência do feromônio, padrão: 1.0): ")
                alfa = float(alfa_str) if alfa_str else 1.0
                beta_str = input("Beta (influência da heurística, padrão: 2.0): ")
                beta = float(beta_str) if beta_str else 2.0
                taxa_evaporacao_str = input("Taxa de evaporação (rho, padrão: 0.5): ")
                taxa_evaporacao = float(taxa_evaporacao_str) if taxa_evaporacao_str else 0.5
                q_val_str = input("Q (constante de atualização do feromônio, padrão: 100.0): ")
                q_val = float(q_val_str) if q_val_str else 100.0
                feromonio_inicial_str = input("Feromônio inicial (padrão: 1.0): ")
                feromonio_inicial = float(feromonio_inicial_str) if feromonio_inicial_str else 1.0
            except ValueError:
                print("Erro: Parâmetros inválidos. Usando valores padrão para ambos os algoritmos.")
                tamanho_populacao, num_geracoes, taxa_crossover, taxa_mutacao = 50, 100, 0.8, 0.01
                num_formigas, num_iteracoes, alfa, beta, taxa_evaporacao, q_val, feromonio_inicial = 10, 50, 1.0, 2.0, 0.5, 100.0, 1.0
            print(f"\nExecutando Algoritmo Genético com: Pop: {tamanho_populacao}, Ger: {num_geracoes}, Cross: {taxa_crossover}, Mut: {taxa_mutacao}")
            print(f"Executando ACO com: Formigas: {num_formigas}, Iter: {num_iteracoes}, Alfa: {alfa}, Beta: {beta}, Evap: {taxa_evaporacao}, Q: {q_val}, Fer. Ini: {feromonio_inicial}")
            start_genetico = time.time()
            melhor_solucao_ga, melhor_aptidao_ga = algoritmo_genetico(itens, capacidade_mochila, tamanho_populacao, num_geracoes, taxa_crossover, taxa_mutacao)
            end_genetico = time.time()

            start_aco = time.time()
            melhor_solucao_aco, melhor_aptidao_aco = algoritmo_aco(itens, capacidade_mochila, num_formigas, num_iteracoes, alfa, beta, taxa_evaporacao, q_val, feromonio_inicial)
            end_aco = time.time()

            print("\n--- Resultados da Execução Paralela ---")
            print(f"Tempo de execução do Algoritmo Genético: {(end_genetico - start_genetico) * 1000:.2f} ms")
            print(f"Tempo de execução do Algoritmo de Colônia de Formigas: {(end_aco - start_aco) * 1000:.2f} ms")
            # Comparar os resultados
            print("\n--- Comparação de Resultados ---")
            if melhor_aptidao_ga > melhor_aptidao_aco:
                print("O Algoritmo Genético encontrou uma solução melhor.")
                print(f"Aptidão GA: {melhor_aptidao_ga}, Aptidão ACO: {melhor_aptidao_aco}")
            elif melhor_aptidao_aco > melhor_aptidao_ga:
                print("O Algoritmo de Colônia de Formigas encontrou uma solução melhor.")
                print(f"Aptidão GA: {melhor_aptidao_ga}, Aptidão ACO: {melhor_aptidao_aco}")
            else:
                print("Ambos os algoritmos encontraram soluções equivalentes.")
            # Exibir resultados de ambos os algoritmos
            print(f"\n--- Resultados do Algoritmo Genético ---")
            if melhor_solucao_ga:
                # print(f"Melhor solução (binária): {melhor_solucao_ga}")
                # print(f"Itens selecionados (índice, peso, valor):")
                # for i, sel in enumerate(melhor_solucao_ga): 
                #     if sel == 1: print(f"  - {itens[i]}")
                
                val_tot_ga, peso_tot_ga = calcular_valor_peso_total(itens, melhor_solucao_ga)
                print(f"Valor total: {val_tot_ga}, Peso total: {peso_tot_ga}")
                print(f"Aptidão: {melhor_aptidao_ga}")
            else:
                print("Nenhuma solução viável encontrada pelo GA.")
            print(f"\n--- Resultados do Algoritmo de Colônia de Formigas (ACO) ---")
            if melhor_solucao_aco:
                # print(f"Melhor solução (binária): {melhor_solucao_aco}")
                # print(f"Itens selecionados (índice, peso, valor):")
                # for i, sel in enumerate(melhor_solucao_aco): 
                #     if sel == 1: print(f"  - {itens[i]}")
                val_tot_aco, peso_tot_aco = calcular_valor_peso_total(itens, melhor_solucao_aco)
                print(f"Valor total: {val_tot_aco}, Peso total: {peso_tot_aco}")
                print(f"Aptidão: {melhor_aptidao_aco}")
            else:
                print("Nenhuma solução viável encontrada pelo ACO.")
        else:
            print("Escolha inválida. Voltando ao menu principal.")
        print("\n--- Fim da Execução ---")
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()