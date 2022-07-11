# Un programa que te de el resultado de la resta de los numeros adyacentes de una lista

def resta(lista):
    resta = 0
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            resta = lista[i] - lista[i+1]
            print(resta)
        else:
            resta = lista[i + 1] - lista[i]
            print(resta)

array = [7, 3, 4,1 ,2, 3]
print(resta(array))