#exponenciacion
print("Exponenciacón")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print("")
#multiplicacion
print("Multiplicacion")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(" ")
print("Division")
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print("")
print("Division entera")
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print("")
print("Modulo")
print(14 % 4)
print(10%3)
print(10%2)

#El operador de resta, operadores unarios y binarios
print("")
print("El operador de resta, operadores unarios y binarios")
print(-4 - 4)
print(4. - 8)
print(-1.1)

print("")
print("Asignacion")
var = 100
var = 200 + 300
print(var)

print("")
print("Funcion input")
print("Introduce algun texto en el cursor parpadeando")
valorInputGuardado = input()
print(valorInputGuardado)

print("")
algo= input("Escribir lo que sea...")
print("Hmm...", algo ,"...¿en serio?")

print("")
numero = int(input("Ingresa un número:"))
multiplicacion = numero *  2
print(numero, "multiplicado por 2 es: ", multiplicacion)

print("")
print("Operaciones con variables nro1")
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

print("")
print("Operaciones con variables nro2")
eg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)



print("")
print("Operadores de cadena")
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

print("")
triplica ="James" * 3 
print(triplica)

print("")
nro1 = 3 * "an"
print(nro1)

print("")
nro2 = 5 * "2" 
nro3 = "2" * 5
print(nro2)
print(nro3)
