from os import system
system('cls')
#CONDICIONAL COMPUEST0
# Ejercicio6: Determinar descuento el descuento a menores y jubilados 
# Suponiendo que la entrada al espectáculo cuesta $1500, solicitar 
# la edad al usuario y calcular el precio final dependiendo de la edad ingresada por el usuario, 
# aplicando el descuento del 10% si la edad es menor de 18 o mayor a 60 años.

entrada = 1500
descuento = 0.10

edad = int(input("Ingrese su edad: "))

if edad > 0:
    if edad < 18 or edad > 60:
        precio = entrada - (entrada * descuento)
        msje = f"El precio final con descuento es: ${precio}"
    else:
        msje = f"El precio final  sin descuento es: ${entrada}"
else:
    msje = "Edad inválida"
    
print(msje)