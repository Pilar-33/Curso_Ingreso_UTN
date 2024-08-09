#4) Crear un programa que solicite al usuario que ingrese una letra. 
# Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). 
# En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.

print("""
    +=======================================================+
        PROGRAMA QUE VALIDA LETRA INGRESADA POR EL USUARIO
    +=======================================================+""")

letra = ""
while not(letra == "U" or letra == "T" or letra == "N"):
    letra = input("Por favor, ingrese una letra (U, T o N): ")
    
        
print(f"La letra {letra} es correcta")
print("Programa finalizado exitosamente!!!")