def isprime(num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont > 2:
        return False
    else:
        return True

for i in range(2, 1001):
    if isprime(i):
        print(f"El numero {i} es Primo")
