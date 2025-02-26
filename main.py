def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    z = max(len(str(x)), len(str(y)))
    m = z // 2
    
    x_primeiros = x // 10**m
    x_ultimos = x % 10**m
    y_primeiros = y // 10**m
    y_ultimos = y % 10**m
    
    a = karatsuba(x_ultimos, y_ultimos)
    b = karatsuba((x_ultimos + x_primeiros), (y_ultimos + y_primeiros))
    c = karatsuba(x_primeiros, y_primeiros)
    
    return (c * 10**(2*m)) + ((b - c - a) * 10**m) + a

if __name__ == "__main__":
    x1 = int(input("Digite o primeiro número: "))
    y2 = int(input("Digite o segundo número: "))
    
    resultado = karatsuba(x1, y2)
    print(f"Resultado da multiplicação pelo metodo de karatsuba: {resultado}")
