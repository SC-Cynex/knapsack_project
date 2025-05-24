# Processo de Trabalho - Refatoração

## Origem do Código

O código original foi obtido a partir do repositório da equipe:

🔗 https://gitlab.com/ruanvcardozo/knapsack_project.git

## Organização

Esta refatoração foi dividida em duas partes:

- **Parte 1:** Análise e Planejamento da refatoração, criação de testes automatizados e estruturação do repositório.
- **Parte 2:** Refatoração efetiva, ajustes finais e melhorias de qualidade de código.

## Abordagem Adotada

1. Análise do código para identificação de problemas como:
   - Funções grandes e acopladas
   - Falta de testes
   - Estrutura de diretórios desorganizada
   - Nomeação pouco descritiva

2. Planejamento da refatoração baseado em técnicas como:
   - Extract Function
   - Rename Variable
   - Split Phase
   - Introduce Test

3. Criação da base de testes com `pytest`

4. Estruturação da documentação e ferramentas

## Ferramentas Sugeridas

- `pytest` – testes automatizados
- `flake8` – estilo de código
- `pylint` – análise estática
- `radon` – complexidade ciclomática

## 📊 Análise de Qualidade de Código - ANTES da Refatoração

### Ferramenta: `flake8`

- Muitos avisos de estilo (linhas longas, nomes não padronizados)
- Código altamente acoplado no `main.py`

### Ferramenta: `pylint`

- Pontuação geral baixa (~4.5/10)
- Funções com muitas responsabilidades
- Nomes de variáveis como `q`, `eta_i`, `tau_i` sem contexto

### Ferramenta: `radon`

- Complexidade alta nas funções `main()` e `algoritmo_aco`
- Níveis C e D (ruim a médio)

### Conclusão da Análise

A refatoração é necessária principalmente para:
- Tornar o código testável
- Reduzir complexidade
- Melhorar manutenibilidade
- Aumentar legibilidade



**Para detalhes completos da análise de qualidade, veja a seção [Análise de Qualidade de Código — Antes da Refatoração](refactoring.md#antes-da-refatoração).**
