from os import system
system("cls")
'''1) Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se 
le hace por no ser fresca y el coste final total.'''

pan = 3.49
pan_no_dia_descuento = 0.6

vendidas_barras = int(input("Número de barras de pan (no del día): "))

precio_pan_no_dia = vendidas_barras * pan
descuento_pan_no_dia = precio_pan_no_dia * pan_no_dia_descuento
coste_final = precio_pan_no_dia - descuento_pan_no_dia

msje = f"Precio hbitual: ${pan}\n"
msje += f"Descuento por no ser fresca: ${descuento_pan_no_dia}\n"
msje += f"Coste final total: ${coste_final:.2f}"
print(msje)