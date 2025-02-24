# Projeto: Multiplicação de Números Grandes com o Algoritmo de Karatsuba

## Descrição do Projeto

Este projeto implementa o **algoritmo de Karatsuba** para multiplicação eficiente de dois números inteiros grandes. O algoritmo de Karatsuba reduz a complexidade da multiplicação tradicional de **O(n²)** para aproximadamente **O(n^log₂3) ≈ O(n^1.585)**, tornando-o mais rápido para números grandes.

## Lógica do Algoritmo

O algoritmo de Karatsuba funciona dividindo os números de entrada em duas partes e aplicando multiplicações recursivas. A lógica é baseada na seguinte identidade matemática:

Seja **x** e **y** dois números:

1. Determina-se **n**, o maior comprimento entre os dois números.
2. Divide-se **x** e **y** em duas partes:
   - `x_primeiros` = primeira metade de `x`
   - `x_ultimos` = última metade de `x`
   - `y_primeiros` = primeira metade de `y`
   - `y_ultimos` = última metade de `y`
3. Calculam-se três multiplicações menores:
   - `multiplicacao_primeiros = karatsuba(x_primeiros, y_primeiros)`
   - `multiplcacao_ultimos = karatsuba(x_ultimos, y_ultimos)`
   - `soma_multiplicacao = karatsuba((x_primeiros + x_ultimos), (y_primeiros + y_ultimos))`
4. O resultado final é obtido pela fórmula:
   ```
   (multiplicacao_primeiros * 10^(2*m)) + ((soma_multiplicacao - multiplicacao_primeiros - multiplcacao_ultimos) * 10^m) + multiplcacao_ultimos
   ```

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado

### Passos para execução:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/karatsuba-multiplication.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd karatsuba-multiplication
   ```
3. Execute o script:
   ```bash
   python main.py
   ```
4. Insira os números quando solicitado.

## Análise Técnica

### Complexidade Assintótica

- **Melhor Caso**: O(n) (se um dos números for de um dígito)
- **Caso Médio & Pior Caso**: O(n^log₂3) ≈ O(n^1.585)

### Complexidade Ciclomática

Para calcular a **complexidade ciclomática**, usamos a fórmula:

**M = E - N + 2P**

Onde:

- **E**: Número de arestas
- **N**: Número de nós
- **P**: Número de componentes conexos (para um programa simples, P=1)

O fluxo do código contém chamadas recursivas e estruturas condicionais, resultando em uma complexidade ciclomática relativamente baixa.

---

Autor: [Seu Nome]

📌 **Repositório:** [GitHub Link](https://github.com/seu-usuario/karatsuba-multiplication)

