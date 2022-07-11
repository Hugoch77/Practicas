# print 5 multiplication table without using multiply operator

def multiply(numero, multiplicador):
    multiplicacion = 0
    for i in range(multiplicador):
        multiplicacion += numero
    return multiplicacion


print(multiply(7, 3))