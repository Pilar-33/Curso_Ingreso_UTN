
print(
"""
    Adivina el número secreto
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
secret_number = 777
number= int(input("Introduce un número: "))
while number != secret_number:
    if number <= 300:
        print("Estás lejos....., el número es mayor que 300")
    elif number>300 and number <= 770:
        print("Estás lejos aún....., el número es mayor que 770")
    elif number > 770 and number <= 776:
        print("Estás cerca....., el número es mayor a 776 y menor a 778")
    elif number > 777:
        print("El número es menor de 800")
        
    print('"¡Ja, ja! ¡Estás atrapado en mi bucle!"') 
    number = int(input("Introduce un número nuavamente: "))
print(" ")
print(f"¡Bien hecho, Junior! El número secreto era {secret_number}. ¡Eres libre ahora!")

