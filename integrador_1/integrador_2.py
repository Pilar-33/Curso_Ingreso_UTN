from os import system
system('cls')
'''Ferrete Lámparas
En una ferretería se quiere implementar un sistema que permita a los usuarios 
saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene 
en cuenta que todas las #?lámparas cuestan $800.
#!A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) 
se aplicará el siguiente descuento:
* Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
* Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % 
y si es de otra marca el descuento es del 30%.
* Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” 
se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
* Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  
el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
#?Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
Mostrar por pantalla: 
#! Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, 
#! el descuento adicional (si corresponde) y el total a pagar con descuento. '''
# Todo !
# !
# ?
# //** */

costo_lamparas = 800
descuento = 0
print("                             FERRETE ILUMINACIÓN")
print("="*80)
cantidad_lamparas = int(input("Ingrese cantidad de lámparas a comprar: "))

if cantidad_lamparas > 0:
    marca_lamparas = input("Ingrese la marca de lámpara (ArgentinaLuz/FelipeLamparas/otra): ")
    if cantidad_lamparas > 5:
        descuento = 0.50
    elif cantidad_lamparas == 5:
        if marca_lamparas == "ArgentinaLuz":
            descuento = 0.40
        else:
            descuento = 0.30
    elif cantidad_lamparas == 4:
        if marca_lamparas == "ArgentinaLuz" or marca_lamparas == "FelipeLamparas":
            descuento = 0.25
        else:
            descuento = 0.20
    elif cantidad_lamparas == 3:
        if marca_lamparas == "ArgentinaLuz":
            descuento = 0.15
        elif marca_lamparas == "FelipeLamparas":
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0
    
    total_sin_descuento = cantidad_lamparas * costo_lamparas
    descuento1 = total_sin_descuento * descuento
    total_con_descuento = total_sin_descuento - descuento1
    
    if total_con_descuento > 4000:
        descuento2 = 0.05
        descuento_adicional = total_con_descuento * descuento2
        total_con_descuento1 = total_con_descuento  - descuento_adicional
    
    # Mostrar información
    print('*'*70) 
    msje = f"Marca: {marca_lamparas}\n"
    msje += f"Cantidad de lámparas: {cantidad_lamparas}\n"
    if cantidad_lamparas > 2:
        msje += f"Total a pagar sin descuento: ${total_sin_descuento:.2f}\n"
        msje += f"Descuento del {int(descuento*100)}%: ${descuento1:.2f}\n"
        msje += f"Total con descuento del {int(descuento*100)}%: ${total_con_descuento:.2f}\n"
        
        if total_con_descuento > 4000:
            msje += f"Descuento adicional {int(descuento2*100)}%: ${descuento_adicional:.2f}\n"
            msje += f"Importe final a pagar con descuento adicional del {int(descuento2*100)}%: ${total_con_descuento1:.2f}\n"
    else:
        msje += f"Importe final a pagar sin descuento: ${total_sin_descuento:.2f}\n"
    print(msje)
    
else:
    print("Error, debe ingresar una cantidad mayor a cero")
