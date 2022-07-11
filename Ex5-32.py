# compara los valores de una lista y los ordena de mayor a menor o viceversa (2 metodos)

def menor(lista1):
    for i in range(len(lista1)):
        for j in range(i+1, len(lista1)):
            if lista1[i] >= lista1[j]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
    return lista1

lista = [7, 3, 4, 1, 2, 3]

listanew = menor(lista)

print(menor(lista))
#print(listanew[::-1])