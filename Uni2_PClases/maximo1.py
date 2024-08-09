contador=0
#max_numero = float('-inf')
flag_numero = True

# while(contador<4):
#     print("Ingrese un numero")
#     num = int(input())

#     if num > max_numero:
#         max_numero = num

#     contador+=1

# print("ejecuciones:",contador)
# print("el valor maximo es:", max_numero)

while(contador < 4):
    numero = int(input("Ingrese número entero: "))
    
    if flag_numero == True:
        flag_numero = False
        max_numero = numero
    elif numero > max_numero:
        max_numero = numero
    contador += 1

print("ejecuciones:",contador)
print("el valor maximo es:", max_numero)
        