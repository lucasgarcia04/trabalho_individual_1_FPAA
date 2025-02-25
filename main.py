def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    numero = max(len(str(x)), len(str(y)))
    maior = numero // 2
    
    x_primeiros = x // 10**maior
    x_ultimos = x % 10**maior
    y_primeiros = y // 10**maior
    y_ultimos = y % 10**maior
    
    multiplcacao_ultimos = karatsuba(x_ultimos, y_ultimos)
    somas = karatsuba((x_ultimos + x_primeiros), (y_ultimos + y_primeiros))
    multiplicacao_primeiros = karatsuba(x_primeiros, y_primeiros)
    
    return (multiplicacao_primeiros * 10**(2*maior)) + ((somas - multiplicacao_primeiros - multiplcacao_ultimos) * 10**maior) + multiplcacao_ultimos

if __name__ == "__main__":
    x1 = int(input("Digite o primeiro número: "))
    y2 = int(input("Digite o segundo número: "))
    
    resultado = karatsuba(x1, y2)
    print(f"Resultado da multiplicação pelo metodo de karatsuba: {resultado}")
