# Multiplicação de Karatsuba

Este projeto implementa o algoritmo de multiplicação de Karatsuba em Python. O método de Karatsuba é um algoritmo eficiente para multiplicação de números inteiros grandes, reduzindo a complexidade computacional em comparação com a multiplicação tradicional.

## Como o Algoritmo Funciona

O algoritmo de Karatsuba utiliza a seguinte estratégia de divisão e conquista:

1. Divide os números de entrada em duas partes.
2. Realiza três multiplicações recursivas em subproblemas menores.
3. Combina os resultados e obtem o produto final.

A implementação segue os seguintes passos:

1. **Caso base:** 

  if x < 10 or y < 10:
        return x * y

Se um dos números for menor que 10, retorna a multiplicação simples.

2. **Determinação do ponto de divisão:** 

   n = max(len(str(x)), len(str(y)))
    m = n // 2

O tamanho do maior número é calculado e dividido ao meio.

3. **Divisão dos números:** 

    x_primeiros = x // 10**m
    x_ultimos = x % 10**m
    y_primeiros = y // 10**m
    y_ultimos = y % 10**m

Os números são separados em duas partes: "primeiros dígitos" e "últimos dígitos".

4. **Recursão:** 

   multiplicacao_ultimos = karatsuba(x_ultimos, y_ultimos)
   soma_multiplicacao = karatsuba((x_ultimos + x_primeiros), (y_ultimos + y_primeiros))
   multiplicacao_primeiros = karatsuba(x_primeiros, y_primeiros)

São feitas três chamadas recursivas para multiplicar partes menores dos números.

5. **Combinação dos resultados:** 

   return (multiplicacao_primeiros * 10**(2*m)) + ((soma_multiplicacao - multiplicacao_primeiros - multiplicacao_ultimos) * 10**m) + multiplicacao_ultimos

Os produtos são combinados para obter o resultado final.


## Como Executar o Projeto

1. O projeto foi realizado em Python na versão 3.13.2.
2. Baixe ou clone este repositório.
3. Execute o programa.
4. Insira os números como argumentos de linha de comando e visualize o resultado.

## Análise da Complexidade Ciclomática

A complexidade ciclomática mede a quantidade de caminhos independentes no código e pode ser calculada pela fórmula:

\[ M = E - N + 2P \]

Onde:
- \( E \) é o número de arestas no grafo de fluxo do código,
- \( N \) é o número de nós,
- \( P \) é o número de componentes conexos (para um único programa, \( P = 1 \)).

Nós (N): 8

Entrada na função
Decisão if x < 10 or y < 10
Retorno direto se verdadeiro
Cálculo de n e m
Separação de x e y
Três chamadas recursivas
Operações matemáticas finais
Retorno do resultado

Arestas (E): 10

Fluxo de execução normal + chamadas recursivas + retorno.

M=10−8+2(1)
M=4

## Análise da Complexidade Assintótica

O algoritmo de Karatsuba possui complexidade **O(n^{log_2 3})**, pois divide o problema em três subproblemas de tamanho \( n/2 \), diferentemente da multiplicação tradicional.

### Casos de Complexidade:
- **Melhor caso:** **O(n)**: Quando os dois números possuem apenas um digito.
- **Caso médio:**  **O(n^{log_2 3})**
- **Pior caso:**  **O(n^{log_2 3})**

## Conclusão

O algoritmo de Karatsuba é eficiente para multiplicação de números grandes e tem aplicação em computação de alta precisão. A implementação recursiva reduz significativamente a quantidade de operações em comparação com a multiplicação tradicional.


