contador=0
max_numero = 0

while(contador<4):
    print("Ingrese un numero")
    num = int(input())

    if num > max_numero:
        max_numero = num

    contador+=1

print("ejecuciones: ",contador)
print("el valor maximo es: ", max_numero)