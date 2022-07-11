# compara los indexes equivalentes de 2 listas y si son iguales lo agrega a una nueva lista

def listaequivalente(lista1, lista2):
    lista3 = []
    if lista1 < lista2:
        for i in range(len(lista1)):
            if lista1[i] == lista2[i]:
                lista3.append(lista1[i])
    else:
        for i in range(len(lista2)):
            if lista1[i] == lista2[i]:
                lista3.append(lista1[i])
    return lista3

lista1 = [7, 3, 4, 1, 2, 3]
lista2 = [7, 4, 3, 1, 9, 3]

listanew = listaequivalente(lista1, lista2)

print(listaequivalente(lista1, lista2))
print(listanew[::-1])