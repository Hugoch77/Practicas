def isprime(num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

for i in range(1001):
    if isprime(i) == True:
        print(f"{i} es numero primo")