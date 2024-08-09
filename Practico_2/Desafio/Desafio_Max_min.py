contador=0
min_numero = float('inf')
max_numero = float('-inf')
print("=" * 50)
print("              PROGRAMA QUE EVALÚA              ")
print("         CUÁL ES EL NÚMERO MÁXIMO Y MÍNIMO     ")
print("=" * 50)


while(contador < 4):
    numero = int(input(f"Digite el {contador+1}° número: "))
    if(numero > max_numero):
        max_numero = numero
    
    if(numero < min_numero):
            min_numero = numero
            
    contador +=1
print("=" * 25)   
print("Ejecuciones:",contador)
print("El valor mínimo es:", min_numero )
print("El valor maximo es:", max_numero)
print("=" * 25) 