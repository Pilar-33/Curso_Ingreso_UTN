from os import system
system("cls")
#CONDICIONAL SIMPLE
#Ejercicio4: Verificación de contraseña Solicitar una contraseña al usuario, 
# suponiendo que la correcta es “python123”. 
# Si la contraseña ingresada coincide darle el siguiente mensaje “Contraseña correcta. Acceso concedido.”, 
# si no coincide darle el siguiente mensaje “Contraseña incorrecta. Acceso denegado.”

clave = "python123"


print("         BIENVENIDO A CAJEROS MAGNUS" + "\n" + "="*50)
contrasenia = input("Por favor, ingrese su contraseña: ")

if contrasenia == clave:
    msje = "Contraseña correcta. Acceso concedido."
else:
    msje = "Contraseña incorrecta. Acceso denegado."

print("="*50 + "\n" +msje)

