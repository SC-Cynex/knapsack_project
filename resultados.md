# Relatório de Resultados: Problema da Mochila com Algoritmos Bio-inspirados

## Introdução

Este relatório apresenta os resultados da aplicação de algoritmos bio-inspirados, especificamente o Algoritmo Genético (GA) e o Algoritmo de Colônia de Formigas (ACO), para resolver o Problema da Mochila 0/1. A implementação foi realizada em Python e permite a interação do usuário para definir o problema e os parâmetros de cada algoritmo.

## Algoritmos Implementados

### 1. Algoritmo Genético (GA)

O Algoritmo Genético foi implementado com as seguintes características:

- **Representação:** Vetor binário, onde cada bit indica a inclusão ou não de um item.
- **População Inicial:** Gerada aleatoriamente.
- **Função de Aptidão:** Valor total dos itens, com penalidade (aptidão zero) para soluções que excedem a capacidade da mochila.
- **Seleção:** Torneio.
- **Crossover:** Um ponto.
- **Mutação:** Bit flip.
- **Elitismo:** O melhor indivíduo da geração anterior é mantido.

### 2. Algoritmo de Colônia de Formigas (ACO)

O Algoritmo de Colônia de Formigas (ACO) foi implementado com as seguintes características:

- **Representação da Solução:** Cada formiga constrói uma solução binária indicando os itens selecionados.
- **Informação Heurística:** Utiliza a relação valor/peso do item como um guia inicial para as formigas.
- **Trilha de Feromônio:** Associada a cada item, indicando o quão desejável é sua inclusão, baseando-se nas soluções anteriores.
- **Regra de Transição:** As formigas escolhem itens probabilisticamente, considerando tanto o feromônio quanto a heurística, enquanto respeitam a capacidade da mochila.
- **Atualização de Feromônio:** Inclui evaporação para evitar estagnação e deposição pelas formigas que encontraram boas soluções, reforçando caminhos promissores.

## Exemplos de Entrada/Saída e Testes

A aplicação interativa `main.py` permite testar os algoritmos com diferentes cenários.

### Teste com Conjunto Pequeno (Aplicável a GA e ACO)

- **Itens (Peso, Valor):** `[Item(indice=0, peso=2, valor=3), Item(indice=1, peso=3, valor=4), Item(indice=2, peso=4, valor=5), Item(indice=3, peso=5, valor=6), Item(indice=4, peso=1, valor=2)]`
- **Capacidade da Mochila:** `7`

#### Exemplo de Saída para GA (Pode variar)
- **Parâmetros do GA:** População: 50, Gerações: 100, Crossover: 0.8, Mutação: 0.01
```
--- Resultados do Algoritmo Genético ---
Melhor solução encontrada (representação binária): [1, 1, 0, 0, 1]
Itens selecionados (índice, peso, valor):
  - Item(indice=0, peso=2, valor=3)
  - Item(indice=1, peso=3, valor=4)
  - Item(indice=4, peso=1, valor=2)
Valor total da solução: 9
Peso total da solução: 6
Aptidão da solução (valor total se dentro da capacidade): 9
```

#### Exemplo de Saída para ACO (Pode variar)
- **Parâmetros do ACO:** Formigas: 10, Iterações: 50, Alfa: 1.0, Beta: 2.0, Evaporação: 0.5, Q: 100.0, Fer. Inicial: 1.0
```
--- Resultados do Algoritmo de Colônia de Formigas (ACO) ---
Melhor solução (binária): [1, 1, 0, 0, 1]
Itens selecionados (índice, peso, valor):
  - Item(indice=0, peso=2, valor=3)
  - Item(indice=1, peso=3, valor=4)
  - Item(indice=4, peso=1, valor=2)
Valor total: 9, Peso total: 6
Aptidão: 9
```
*(Nota: Devido à natureza estocástica dos algoritmos bio-inspirados, os resultados exatos podem variar entre execuções. Para este conjunto pequeno, uma solução ótima conhecida é selecionar os itens 0, 1 e 4, resultando em valor 9 e peso 6.)*

### Teste com Conjuntos Grandes (Gerados Aleatoriamente)

A aplicação permite gerar, por exemplo, 1000 ou 10.000 itens aleatórios. O desempenho dos algoritmos pode ser observado:

- **Número de Itens:** 1000 (ou 10000)
- **Capacidade:** Definida como 40% do peso total dos itens gerados.

**Observações Gerais para GA e ACO com Grandes Conjuntos:**
- O tempo de execução aumenta significativamente com o número de itens e os parâmetros do algoritmo (tamanho da população/gerações para GA, número de formigas/iterações para ACO).
- A qualidade da solução encontrada é uma aproximação da solução ótima. Para problemas grandes, encontrar a solução exata é computacionalmente inviável em tempo hábil com esses métodos heurísticos.
- O ajuste fino dos parâmetros de cada algoritmo é crucial para obter boas soluções em tempos razoáveis.

## Dificuldades e Aprendizados

### Gerais para Algoritmos Bio-inspirados:
- **Ajuste de Parâmetros:** Encontrar os parâmetros ideais para cada algoritmo (GA: tamanho da população, taxas de crossover/mutação, número de gerações; ACO: número de formigas, iterações, alfa, beta, taxa de evaporação, Q) é um processo iterativo e depende da instância do problema. Diferentes conjuntos de parâmetros podem levar a diferentes qualidades de solução e tempos de convergência.
- **Natureza Estocástica:** Os resultados podem variar entre execuções devido aos componentes aleatórios. Múltiplas execuções são recomendadas para avaliar a robustez e a qualidade média das soluções.
- **Convergência Prematura:** Ambos os algoritmos podem, por vezes, convergir para ótimos locais. Técnicas específicas para cada algoritmo podem ajudar a mitigar isso (ex: taxas de mutação variáveis no GA, limites de feromônio ou estratégias de reinicialização no ACO), mas não foram implementadas nesta versão básica.
- **Escalabilidade:** Para um número muito grande de itens (ex: 10.000), o tempo de execução com os parâmetros padrão pode ser considerável. Otimizações no código ou abordagens híbridas poderiam ser exploradas.

### Específicos do ACO:
- **Construção da Solução:** A forma como as formigas constroem a solução (ordem de consideração dos itens, regra de transição) impacta diretamente o desempenho. A aleatorização na ordem de consideração dos itens disponíveis ajudou a diversificar a busca.
- **Atualização de Feromônio:** A estratégia de atualização de feromônio é crítica. A combinação de evaporação e deposição baseada na qualidade das soluções encontradas é fundamental para guiar a busca eficientemente.
- **Balanceamento Alfa e Beta:** Os parâmetros alfa (influência do feromônio) e beta (influência da heurística) precisam ser balanceados. Um beta muito alto pode levar a uma busca gulosa, enquanto um alfa muito alto pode levar à estagnação rápida.

## Comparação Preliminar (Observacional)

- **Conceito:** GA opera em uma população de soluções, evoluindo-as através de gerações. ACO utiliza agentes (formigas) que constroem soluções colaborativamente através de comunicação indireta (feromônio).
- **Parâmetros:** Ambos os algoritmos possuem vários parâmetros que necessitam de ajuste.
- **Qualidade da Solução:** Em testes preliminares com os conjuntos de dados fornecidos, ambos os algoritmos foram capazes de encontrar boas soluções, frequentemente aproximando-se ou atingindo a solução ótima para casos pequenos. Para casos maiores, a qualidade pode variar dependendo dos parâmetros e do número de iterações/gerações.
- **Tempo de Execução:** O tempo de execução pode variar. O ACO, com sua construção iterativa de soluções por múltiplas formigas, pode ser mais intensivo computacionalmente por iteração em comparação com uma geração do GA, dependendo do número de formigas e itens.

## Conclusão

A aplicação desenvolvida fornece uma ferramenta interativa para explorar a resolução do Problema da Mochila utilizando tanto o Algoritmo Genético quanto o Algoritmo de Colônia de Formigas. Ela demonstra os princípios básicos de ambos os algoritmos e permite ao usuário experimentar com diferentes configurações e conjuntos de dados. As implementações servem como uma base que pode ser expandida com outros algoritmos bio-inspirados, otimizações e funcionalidades adicionais, como uma interface gráfica ou análises de desempenho mais robustas.

