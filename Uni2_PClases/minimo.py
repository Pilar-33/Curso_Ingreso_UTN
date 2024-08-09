contador=0
#min_numero = 0
flag_min = True

# while(contador<4):
#     print("Ingrese un numero")
#     num = int(input())

#     if num < min_numero:
#         min_numero = num

#     contador+=1

while contador < 4:
    numero = int(input("Ingrese un número:"))
    if flag_min == True:
        flag_min = False
        min_numero = numero
    elif numero < min_numero:
        min_numero = numero
    contador += 1
    
print("ejecuciones: ",contador)
print("el valor minimo es: ", min_numero)