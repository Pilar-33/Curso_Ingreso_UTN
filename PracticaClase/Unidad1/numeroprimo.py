from os import system
system('cls')

#encuentre los numeros primos de 1 a 10 incluido

contador = 2
primer_primo = True
while contador < 11 :
    es_primo = True
    divisor = 2
    while divisor < contador and es_primo == True:
        if contador % divisor == 0:
            es_primo = False
        divisor += 1

    if es_primo == True:
        if not primer_primo == True:
            print(", ", end = '')
        print(contador, end = ' ')
        primer_primo = False
    contador += 1
print("")