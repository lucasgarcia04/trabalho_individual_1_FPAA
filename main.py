def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_primeiros = x // 10**m
    x_ultimos = x % 10**m
    y_primeiros = y // 10**m
    y_ultimos = y % 10**m
    
    multiplcacao_ultimos = karatsuba(x_ultimos, y_ultimos)
    soma_multiplicacao = karatsuba((x_ultimos + x_primeiros), (y_ultimos + y_primeiros))
    multiplicacao_primeiros = karatsuba(x_primeiros, y_primeiros)
    
    return (multiplicacao_primeiros * 10**(2*m)) + ((soma_multiplicacao - multiplicacao_primeiros - multiplcacao_ultimos) * 10**m) + multiplcacao_ultimos

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    resultado = karatsuba(num1, num2)
    print(f"Resultado da multiplicação pelo metodo de karatsuba: {resultado}")
