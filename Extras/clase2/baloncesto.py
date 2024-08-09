"""A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa 
deberá determinar la posición del jugador en la cancha, considerando los siguientes parametros:

Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot"""

altura = float(input("Ingrese altura en cm: "))

if altura < 140 or altura > 250:
    msje = "Ingrese altura incorrecta"
elif altura < 160:
    msje = "Menos de 160 cm: Base"
elif altura < 180:
    msje ="Entre 160 cm y 179 cm: Escolta"
elif altura < 200:
    msje = "Entre 180 cm y 199 cm: Alero"
else:
    msje = "200 cm o más: Ala-Pívot o Pívot"
print(msje)