# Multiplicação de Karatsuba

Este projeto implementa o algoritmo de multiplicação de Karatsuba em Python. O método de Karatsuba é um algoritmo eficiente para multiplicação de números inteiros grandes, reduzindo a complexidade computacional em comparação com a multiplicação tradicional.

## Estrutura

1. main.py

Arquivo com a implementação do método de Karatsuba.

2. Readme.md

Arquivo explicando como o código funciona e como executa-lo.

## Como o Algoritmo Funciona

O algoritmo de Karatsuba utiliza a seguinte estratégia de divisão e conquista:

1. Divide os números de entrada em duas partes.
2. Realiza três multiplicações recursivas em subproblemas menores.
3. Combina os resultados e obtem o produto final.

## A implementação segue os seguintes passos:

### 1. Caso base
Se um dos números for menor que 10, a multiplicação é feita diretamente:

```python
if x < 10 or y < 10:
    return x * y
```

### 2. Determinação do ponto de divisão
Calculamos o tamanho do maior número e dividimos ao meio:

```python
 numero = max(len(str(x)), len(str(y)))
maior = numero // 2
```

### 3. Divisão dos números
Os números são separados em duas partes: "primeiros dígitos" e "últimos dígitos".

```python
 x_primeiros = x // 10**maior
 x_ultimos = x % 10**maior
 y_primeiros = y // 10**maior
 y_ultimos = y % 10**maior
```

### 4. Recursão
Realizamos três chamadas recursivas para multiplicar partes menores dos números.

```python
 multiplcacao_ultimos = karatsuba(x_ultimos, y_ultimos)
 somas = karatsuba((x_ultimos + x_primeiros), (y_ultimos + y_primeiros))
 multiplicacao_primeiros = karatsuba(x_primeiros, y_primeiros)
```

### 5. Combinação dos resultados
Os produtos são combinados para obter o resultado final.

```python
return (multiplicacao_primeiros * 10**(2*maior)) /
+ ((somas - multiplicacao_primeiros - multiplcacao_ultimos) * 10**maior) / 
+ multiplcacao_ultimos
```

## Como Executar o Projeto

1. O projeto foi realizado em Python na versão 3.13.2.
2. Baixe ou clone este repositório.
3. Execute o programa.
4. Insira os números como argumentos de linha de comando e visualize o resultado.

## Análise da Complexidade Ciclomática

A complexidade ciclomática mede a quantidade de caminhos independentes no código e pode ser calculada pela fórmula:

\[ M = E - N + 2P \]

Onde:
- **E** é o número de arestas no grafo de fluxo do código,
- **N** é o número de nós,
- **P** é o número de componentes conexos (para um único programa, **P = 1**).

### Contagem de Nós e Arestas

- **Nós (N) = 8**
  - Entrada na função
  - Decisão `if x < 10 or y < 10`
  - Retorno direto se verdadeiro
  - Cálculo de `n` e `m`
  - Separação de `x` e `y`
  - Três chamadas recursivas
  - Operações matemáticas finais
  - Retorno do resultado

- **Arestas (E) = 10**
  - Fluxo de execução normal + chamadas recursivas + retorno

### Cálculo da Complexidade

\[ M = 10 - 8 + 2(1) \]
\[ M = 4 \]

## Análise da Complexidade Assintótica

O algoritmo de Karatsuba possui complexidade **O(n^{log_2 3})**, pois divide o problema em três subproblemas de tamanho \( n/2 \), diferentemente da multiplicação tradicional.

### Casos de Complexidade:
- **Melhor caso:** **O(n)**: Quando os dois números possuem apenas um digito.
- **Caso médio:**  **O(n^{log_2 3})**
- **Pior caso:**  **O(n^{log_2 3})**

## Conclusão

O algoritmo de Karatsuba é eficiente para multiplicação de números grandes e tem aplicação em computação de alta precisão. A implementação recursiva reduz significativamente a quantidade de operações em comparação com a multiplicação tradicional.


