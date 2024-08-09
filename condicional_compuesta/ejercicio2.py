from os import system
system('cls')
#CONDICIONAL COMPUESTO
#Ejercicio2: Determinar el tipo de triángulo según sus lados 
# Observando la siguiente clasificación de los triángulos según sus lados: 
# 1. equilatero (3 lados iguales)
# 2. isoceles (2 lados iguales)
# 3. escaleno (3 lados  idesiguales


print("      CLASIFICACIÓN DE LOS TRIANGULOS SEGÚN SUS LADOS" + "\n" + "*"*60)

lado1 = float(input("Ingrese longitud del primer lado: "))
lado2 = float(input("Ingrese longitud del segundo lado: "))
lado3 = float(input("Ingrese longitud del tercer lado: "))

if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    msje = "El triángulo es equilatero"
elif (lado1 == lado2  or lado1 == lado3 or lado3 == lado2):
    msje = "El triángulo es isóceles"
else:
    msje = "El triángulo es escaleno"

print("*"*60 + "\n" + msje)