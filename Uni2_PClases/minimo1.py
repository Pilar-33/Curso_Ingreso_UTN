contador=0
min_numero = float('inf')

while(contador<4):
    print("Ingrese un numero:")
    num = int(input())

    if num < min_numero:
        min_numero = num

    contador+=1

print("ejecuciones: ",contador)
print("el valor min es: ", min_numero)