from os import system
system('cls')
#2) Crear unprogramaquesolicite al usuario que ingrese una contraseña mediante prompt. 
# Comprobar quela contraseña ingresada sea ‘utn750’. En caso de no coincidir, 
# volver a solicitarla hasta que coincidan.

contrasenia = "utn750"
print(""" 
                    +================================+
                    |  BIENVENIDOS A CAJEROS MAGNUS  |
                    +================================+""")
contrasenia_ingresada = input("Por favor, ingrese la contraseña: ")

while (contrasenia_ingresada != contrasenia):
    contrasenia_ingresada = input("Contraseña incorrecta. Intentelo de nuevo: ")
    
print('''
+=======================================+
Contraseña correcta. Acceso concedido!!!
Gracias, por utilizar nuestro servicio.''')