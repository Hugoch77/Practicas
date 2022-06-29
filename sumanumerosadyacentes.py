lista = [1, 2, 3, 0]

for i in range(len(lista)-1):
    if lista[i] + lista[i+1] == 3:
        print(f"{lista[i]} + {lista[i+1]} == 3")
    else:
        print(f"{lista[i]} + {lista[i+1]} no es == 3")