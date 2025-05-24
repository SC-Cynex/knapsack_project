# Plano de Refatoração - Problema da Mochila com Algoritmos Bio-inspirados

## 🔍 O que será refatorado

1. Separação entre lógica de interface e lógica de execução dos algoritmos.
2. Extração de funções com responsabilidades únicas em `main.py`.
3. Renomeação de variáveis pouco descritivas.
4. Modularização dos testes com `pytest`.
5. Reestruturação dos arquivos em `src/`, `tests/` e `utils/`.

## ❓ Por que será refatorado

- Melhor legibilidade e clareza de propósitos.
- Reduzir dependência entre componentes (desacoplamento).
- Facilitar testes e manutenção futura.
- Preparar a base para aplicação de Clean Code.

## 🛠 Técnicas de Refatoração

- **Extract Function**: dividir `main()` em funções menores.
- **Rename Variable**: tornar nomes mais significativos.
- **Move Function / Class**: transferir lógica de `main.py` para `controller.py` ou `runner.py`.
- **Introduce Test**: criar cobertura com `pytest`.
- **Split Phase**: separar leitura de dados da aplicação dos algoritmos.

## 🔧 Ferramentas de Qualidade

- `flake8`: análise de estilo
- `pylint`: análise estática e coesão
- `radon`: análise de complexidade ciclomática
- `pytest`: framework de testes

## 🔜 Propostas de Melhorias

- Criar pasta `src/` com `algorithms`, `controllers`, `utils`
- Criar pasta `tests/` com cobertura básica de aptidão e algoritmos
- Separar a execução em `run_ga.py` e `run_aco.py` como wrappers

## 📊 Análise de Qualidade de Código 
### Antes da Refatoração

### 🔹 flake8
Comando executado:
```bash
python -m flake8 main.py
```

> Foram identificadas **mais de 70 ocorrências**, incluindo:
- Linhas muito longas (`E501`)
- Imports não utilizados (`F401`)
- Espaços em branco desnecessários (`W293`)
- Uso de f-strings mal formatadas (`F541`)
- Má formatação de indentação (`E111`, `E117`)

---

### 🔹 pylint
Comando executado:
```bash
python -m pylint main.py
```

> Resultado:
- **Pontuação final:** 7.26/10
- Problemas:
  - Ausência de docstrings em várias funções
  - Função `main()` com:
    - `too-many-branches (27)`
    - `too-many-statements (144)`
    - `too-many-locals (45)`
  - Uso de `f-string` sem interpolação (`W1309`)
  - Importações fora da ordem (`C0411`)

---

### 🔹 radon
Comando executado:
```bash
python -m radon cc main.py -s -a
```

> Complexidade por função:

| Função                             | Complexidade |
|-----------------------------------|--------------|
| `main()`                          | **F (44)** ❌ |
| `obter_dados_problema_manual()`   | B (7)        |
| `obter_dados_problema()`          | A (5)        |
| `selecionar_conjunto_teste()`     | A (5)        |
| `gerar_dados_grandes_aleatorios()`| A (4)        |
| `mostrar_menu_algoritmos()`       | A (3)        |

> **Média geral:** **C (11.33)**

---

### ✅ Conclusão
- O código original apresenta alta complexidade, baixa coesão e muitos problemas de estilo
- Refatoração é **fundamental** para melhorar organização, legibilidade e manutenção
