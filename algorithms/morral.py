def morral(tamano_morral, pesos, valores, n):

    #caso base:
    if n == 0 or tamano_morral == 0:
        return 0
    #caso base 2 (si algun peso es mayor que el tamano_morral): 
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))

if __name__ == '__main__' :
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)
    # print("n: ", n)

    resultado = morral(tamano_morral, pesos,  valores, n)
    print(resultado)
    print('-' * 20)