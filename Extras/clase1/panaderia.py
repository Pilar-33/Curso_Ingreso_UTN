from os import system
system('cls')

'''1) Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se 
le hace por no ser fresca y el coste final total.'''
precio_pan= 3.49
descuento= 0.60
barras_pan_no_fresco = int(input("Ingrese cantidad de barras vendidas no del día: "))

descuento_pan_no_fresco = precio_pan - (precio_pan * descuento)
precio_final_pan_no_fresco = barras_pan_no_fresco * descuento_pan_no_fresco

msj= f'''
Precio barra de pan: ${precio_pan}
Descuento por cada pan no fresco: ${descuento_pan_no_fresco:.2f}
Total a pagar: ${precio_final_pan_no_fresco:.2f}
'''
print(msj)  
