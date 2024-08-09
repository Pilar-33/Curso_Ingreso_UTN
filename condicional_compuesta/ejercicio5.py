from os import system
system('cls')
#CONDICIONAL COMPUESTO
#Ejercicio5: Determinar un Período Considerando el siguiente esquema para calcular un período escolar
#mes : 1 al 3, periodo: inscripcion
#mes : 4 al 6, periodo: cursada
#mes : 7, periodo: parciales
#mes : 8, finales
# Solicitar un mes al usuario e informar a qué período corresponde, 
# si ingresa un mes que no se contempla en el esquema, indicar que es inválido.

mes = int(input("Ingresar un mes (1 al 8): "))

if mes > 0 and mes < 9:
    if mes < 4:
        msje = f" Mes {mes} ---> Periodo: Inscripcion"
    elif mes > 3:
        msje = f" Mes {mes} ---> Periodo: Cursada"
    elif mes == 7:
        msje = f" Mes {mes} ---> Periodo: Parciales"
    elif mes == 8:
        msje = f" Mes {mes} ---> Periodo: Finales"
else: 
    msje = f" Mes {mes} ---> Mes inválido"

print(msje)