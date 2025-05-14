# Equipe

- Ruan Cardozo
- Guilherme Elias
- Guilherme Machado

# Solução Interativa para o Problema da Mochila com Algoritmos Bio-inspirados

Este projeto apresenta uma solução interativa em Python para o clássico Problema da Mochila 0/1 (Knapsack), utilizando algoritmos bio-inspirados, incluindo o Algoritmo Genético (GA) e o Algoritmo de Colônia de Formigas (ACO). A aplicação permite ao usuário definir o problema da mochila (itens com pesos e valores, capacidade da mochila) de forma manual, usar conjuntos de teste pré-definidos ou gerar grandes conjuntos de dados aleatoriamente. Além disso, o usuário pode configurar os parâmetros específicos de cada algoritmo para explorar diferentes cenários de otimização.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `main.py`: Ponto de entrada da aplicação CLI interativa. Gerencia o fluxo da aplicação, interação com o usuário, seleção de algoritmos e apresentação dos resultados.
- `knapsack.py`: Contém a modelagem do problema da mochila, incluindo a classe `Item` e funções para calcular o valor/peso de uma solução e a função de aptidão.
- `utils.py`: Módulo com funções utilitárias, como a geração de conjuntos de dados de teste e a obtenção de dados pré-definidos.
- `algorithms/`: Diretório destinado a abrigar as implementações dos algoritmos bio-inspirados.
    - `__init__.py`: Torna o diretório `algorithms` um pacote Python.
    - `genetic_algorithm.py`: Implementação do Algoritmo Genético para o problema da mochila.
    - `ant_colony.py`: Implementação do Algoritmo de Colônia de Formigas para o problema da mochila.
- `README.md`: Este arquivo, contendo a documentação do projeto.
- `resultados.md`: Arquivo Markdown contendo o relatório de resultados, descrição dos algoritmos, exemplos de entrada/saída e análise de desempenho.

## Problema da Mochila 0/1

Dado um conjunto de *n* itens, cada um com um peso *w[i]* e um valor *v[i]*, e uma mochila com capacidade máxima *W*, o objetivo é escolher um subconjunto de itens de forma a maximizar o valor total, sem que a soma dos pesos dos itens escolhidos exceda a capacidade *W*. Cada item só pode ser escolhido uma vez (0/1).

## Algoritmos Implementados

### 1. Algoritmo Genético (GA)

A solução utiliza um Algoritmo Genético para encontrar uma solução aproximada para o problema da mochila. Os principais componentes do GA implementado são:

1.  **Representação do Indivíduo (Cromossomo)**: Vetor binário onde `1` indica inclusão do item.
2.  **População Inicial**: Gerada aleatoriamente.
3.  **Função de Aptidão**: Valor total dos itens, com penalidade (aptidão zero) para soluções que excedem a capacidade.
4.  **Seleção**: Torneio.
5.  **Operadores Genéticos**: Crossover de um ponto e mutação bit flip.
6.  **Elitismo**: O melhor indivíduo é mantido.
7.  **Critério de Parada**: Número pré-definido de gerações.

### 2. Algoritmo de Colônia de Formigas (ACO)

O ACO é outro algoritmo bio-inspirado implementado para resolver o problema da mochila. Suas características principais são:

1.  **Formigas e Soluções**: Cada formiga constrói uma solução (um subconjunto de itens) de forma incremental.
2.  **Informação Heurística**: A desejabilidade de um item é inicialmente avaliada pela sua relação valor/peso.
3.  **Trilha de Feromônio**: Cada item possui uma trilha de feromônio associada, que é atualizada pelas formigas. Itens que aparecem em boas soluções recebem mais feromônio, tornando-os mais atraentes para futuras formigas.
4.  **Regra de Transição Probabilística**: As formigas escolhem o próximo item a ser incluído na mochila com base em uma probabilidade que combina a intensidade do feromônio e a informação heurística do item, sempre respeitando a capacidade restante da mochila.
5.  **Atualização de Feromônio**:
    *   **Evaporação**: O feromônio em todas as trilhas diminui com o tempo (taxa de evaporação), evitando convergência prematura para soluções subótimas.
    *   **Deposição**: As formigas que constroem boas soluções depositam feromônio nas trilhas dos itens que escolheram. A quantidade de feromônio depositado é geralmente proporcional à qualidade da solução encontrada.
6.  **Critério de Parada**: O algoritmo executa por um número pré-definido de iterações (ciclos).

## Como Executar a Aplicação

1.  **Pré-requisitos**:
    *   Python 3.x instalado.

2.  **Execução**:
    *   Navegue até o diretório raiz do projeto (`knapsack_project`).
    *   Execute o script `main.py` a partir do terminal:
        ```bash
        python main.py
        ```

3.  **Interação**:
    *   O programa apresentará um menu principal para escolher o algoritmo (Algoritmo Genético ou Algoritmo de Colônia de Formigas, e a opção de executar ambos).
    *   Em seguida, você poderá escolher como definir o problema:
        *   **Entrada manual**: Você fornecerá os pesos dos itens, os valores dos itens e a capacidade da mochila.
        *   **Conjunto de teste pré-definido**: Você poderá escolher entre conjuntos de teste pequenos e médios.
        *   **Gerar dados grandes**: Você poderá especificar o número de itens a serem gerados aleatoriamente, e a capacidade será definida automaticamente.
    *   Dependendo do algoritmo selecionado, você será solicitado a inserir seus parâmetros específicos (ex: tamanho da população, número de gerações, taxa de crossover, taxa de mutação para GA; número de formigas, número de iterações, alfa, beta, taxa de evaporação para ACO) ou usar os valores padrão.
    *   Após a execução do algoritmo, os resultados serão exibidos, incluindo a melhor solução encontrada (quais itens foram selecionados), o valor total e o peso total dessa solução.

