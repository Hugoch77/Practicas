# Imprime si es numero primo

def esprimo(numero):
    contador = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
    if contador <= 2:
        return True
    else:
        return False

rango=100
numero = 25
for i in range(2, 101):
    if esprimo(i):
        print(f"el numero {i} es primo")