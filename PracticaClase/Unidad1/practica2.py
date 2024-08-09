# 1) Escribe un programa que pida el nombredel usuario y muestre por consolauntexto: “Hola nombreUsuario"

"""nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")
print("Hola" , nombre)"""

# 2) Escribe un programa que pida unnúmero, luego pida otro número y muestre por consola el resultado de sumar dichos números.

"""print("")
nro1 = float(input("Ingrese primer número: "))
nro2 = float(input("Ingrese segundo número: "))
suma = nro1 + nro2
print(F"La suma de: {nro1} + {nro2} = {suma}")"""

# 3) Cree un programa que pida elnombre,elapellido, edad del usuario y luego muestre por consola los datos ingresados

"""print("")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
print("")
print("--------------------")
print("Datos del usuario:")
print("--------------------")
print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}")"""

#4) Cree un programa que pida el nombre,número de comisión, asignatura, docente y si el usuario estuvo presente, luego que muestre 
# los datos por consola con las leyendas pertinentes

"""print("")
nombre = input("Ingrese su nombre: ")
comision = int(input("Ingrese su número de comisión: "))
asignatura = input("Ingrese su asignatura: ")
docente = input("Ingrese su docente: ")
presente = input("¿Estuvo presente?(si/no): ").lower().replace("í", "i")

if presente == "si":
    print("")
    print("Bienvenido")
    print("Datos del usuario:")
    print("--------------------")
    print(f"Nombre: {nombre}\nNúmero de comisión: {comision}\nAsignatura: {asignatura}\nDocente: {docente}\nPresente: {presente}")
else:
    print("Estudiante: Ausente")"""

# 5) Cree un programa que pida el lado de un cuadrado y calcule la superficie
"""print("")
print("Superficie del Cuadrado")
lado = float(input("Ingrese el lado del cuadrado: "))
superficie = lado * lado
print(f"La superficie del cuadrado es: {superficie}")"""


# 6) Cree un programa que pida los lados de un rectángulo y calcule la superficie
"""print("")
print("Superficie del rectángulo")
lado1 = float(input("Ingrese el lado 1 del rectángulo: "))
lado2 = float(input("Ingrese el lado 2 del rectángulo: "))
superficie = lado1 * lado2
print(f"La superficie del rectángulo es: {lado1} * {lado2} = {superficie}")"""

# 7) Cree un program aque calcule la superficie de un triángulo
"""print("")
print("Superficie del triángulo")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
superficie = (base * altura) / 2
print(f"La superficie del triángulo es: {superficie}")"""

#8) Cree un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.
"""print("")
print("IVA")
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.21

print("Nombre del producto:", nombre)
print(F"Precio del producto sin IVA: {precio}")
print(f"Precio del producto con IVA: {iva: .2f}")"""


# 9) cree un programa que calcule el promedio de un alumno, ingresando sunombre apellido, 
# #3 notas, que muestre al final las leyendas pertinentes
"""print("")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
print("")
print("--------------------")
print("Datos del alumno:")
print("--------------------")
print(f"Nombre: {nombre}\nApellido: {apellido}\nNota 1: {nota1}\nNota 2: {nota2}\nNota 3: {nota3}\nPromedio: {promedio}")"""

# 10) Cree un programa en el cual pida al usuario el nombre y la edad y muestre por consola la edad que tentra dentro de 10 años
"""print("")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad10 = edad + 10
print("")
print("--------------------")
print("Datos del usuario:")
print("--------------------")
print(f"Nombre: {nombre}\nEdad: {edad}\nEdad dentro de 10 años: {edad10}")"""

x= 50
y = "30"
print(str(x)+y)
print(f"{x}{y}")

#Cree un programa que al ingresar un numero entero, vaya incrementando de a una unidad y se muestre por consola:
numero = int(input("Ingrese un número entero:"))
limite = 10
contador = 0
while contador < limite:
    numero +=1
    print(numero)
    contador += 1

