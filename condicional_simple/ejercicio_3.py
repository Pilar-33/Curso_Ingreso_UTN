from os import system
system('cls')
#CONDICIONAL SIMPLE
# Ejercicio3:Evaluación de calificaciones: Solicitar una nota al usuario que puede ingresar en este formato 
# (ej: 6.50) Informar las siguientes notificaciones dependiendo la nota ingresada:
#Entre 7 y 9: “Notable” [7,9)
# Entre 5 y 7: “Aprobado” [5,7)
# Entre 9 y 10: “Sobresaliente” [9, 10]
# Entre 0 y 5: “Suspenso” [0,5)


print("             EVALÚA CALIFICACIONES" + "\n" + "="*50)
nota = float(input("Ingrese la calificación: "))

if nota < 0 or nota > 10:
    print("La nota ingresada es incorrecta")
elif nota > 8.8: #9,10
    msje = '"SOBRESALIENTE"'
elif nota > 6.8 : #7,8
    msje = '"NOTABLE"'
elif nota > 4.8: #5,6
    msje = '"APROBADO"'
else: #0,4
    msje = "SUSPENSO"

if nota > -1 and nota < 11:
    print("="*50 + "\n" + f"Nota {nota}: {msje}")