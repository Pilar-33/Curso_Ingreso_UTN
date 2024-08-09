from os import system
system('cls')
#4) Crear un programa que solicite al usuario que ingrese una letra. 
# Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). 
# En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.

print("""
+============================================+
    PROGRAMA QUE EVALUA LA LETRA INGRESADA
+============================================+
""")

letra = input("Por favor, ingrese una letra (U, T, N): ")

while (letra != 'U' and letra != 'T' and letra != 'N'):
    print("Letra incorrecta. Debe ser U, T o N.")
    letra = input("Ingrese una letra (U, T, N): ")
    print("")

print(f"La letra {letra} es correcta.")
print("Programa finalizado exitosamente!!!")
