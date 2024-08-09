"""TP: ES_Facturaciones
Enunciado:
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%)."""


print("Facturaciónes")
print("------------------------------------")
#A. Ingresar tres precios de productos y mostrar la suma de los mismos.
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))
print("A: Suma de los mismos")
suma = precio1 + precio2 + precio3
print(f"La suma de los precios es: {suma:.2f}")

#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
print("")
print("B: Promedio de los mismos")
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))
suma = precio1 + precio2 + precio3
promedio = suma / 3
print(f"El promedio de los precios es: {promedio:.2f}")


#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%)
print("")
print("C: Precio final")
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))
suma = precio1 + precio2 + precio3
iva = suma * 0.21
precio_final = suma + iva
print("El precio final más IVA: ", precio_final)