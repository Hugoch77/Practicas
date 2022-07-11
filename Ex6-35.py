# Imprime la serie de fibanocci

def serie(numero):
    a = 0
    b = 1
    i = 0
    while i < numero:

        suma = a + b
        a = b
        b = suma
        print(suma)
        i += 1

numero = 7
print(serie(numero))