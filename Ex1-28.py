# Create a method which accepts array and returns sum of all the elements in array

def sumofelements(lista):
    suma = 0
    for i in lista:
        #print(i)
        suma += i
    return suma


print(sumofelements([1, 2, 3, 4, 5]))