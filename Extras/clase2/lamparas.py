from os import system
system('cls')
'''
FERRETE ILUMINACION

Para el departamento de iluminación:
Tomando en cuenta que todas las lámparas están en oferta al mismo precio de $35 pesos final.
A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" 
    se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” 
    se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  
    el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
E.	Si el importe final con descuento suma más de $120  se debe sumar un 10% de ingresos brutos 
    en informar del impuesto con el siguiente mensaje:
Usted pago X de IIBB.”, siendo X el impuesto que se pagó.

Precio final sin descuento: 
Precio final con descuento: 
Precio final con descuento + IIBB: 
Cant lamparas compradas
Marca de las lamparas
'''
precio_unidad = 35
marca_lampara = " "
descuento = 0
impuesto_iibb = 0
precio_final_iibb = 0

print("                             FERRETE ILUMINACIÓN")
print("="*80)
cantidad_lamparas = int(input("Ingrese cantidad de lamparas a comprar: "))


if cantidad_lamparas > 0:  
    marca_lampara = input("Ingrese la marca de lampara (ArgentinaLuz/FelipeLamparas/Otra): ") 
    if (cantidad_lamparas) > 5:
        descuento = 0.50
    elif (cantidad_lamparas) == 5:
            if (marca_lampara) == "ArgentinaLuz":
                descuento = 0.40  
            else:
                descuento = 0.30
    elif (cantidad_lamparas == 4):  
            if (marca_lampara == "ArgentinaLuz" or marca_lampara == "FelipeLamparas"):
                descuento = 0.25
            else:
                descuento = 0.20
    elif (cantidad_lamparas == 3):
        if (marca_lampara == "ArgentinaLuz"):
                descuento = 0.15
        elif (marca_lampara == "FelipeLamparas"):
                descuento = 0.10
        else:
                descuento = 0.05
    else:
        descuento = 0
    #Precio sin descuento y con descuento
    precio_sin_descuento = cantidad_lamparas * precio_unidad
    precio_con_descuento = precio_sin_descuento * (1 - descuento)

    print('*'*80) 
    #calcular el importe final con descuento suma más de $120  se debe sumar un 10% de ingresos brutos
    if precio_con_descuento > 120:
        impuesto_iibb = precio_con_descuento *  0.10
        precio_final_iibb = precio_con_descuento + impuesto_iibb
        print(f"\nUsted pago ${impuesto_iibb:.2f} de IIBB, siendo ${impuesto_iibb:.2f} el impuesto que se pagó.") 
    
    # mostrar informacón
    if cantidad_lamparas > 2:
        ticket = f"Precio final sin descuento: ${precio_sin_descuento:.2f}\n"
        ticket += f"Precio final con descuento: ${precio_con_descuento:.2f}\n"
        if precio_final_iibb > 0:
            ticket += f"Precio final con descuento + IIBB: ${precio_final_iibb:.2f}\n"
        ticket += f"Cantidad lamparas compradas: {cantidad_lamparas}\n"
        ticket += f"Marca de las lamparas: {marca_lampara}"
    else: 
        ticket = f"Precio final sin descuento: ${precio_sin_descuento:.2f}\n"
        ticket += f"Cantidad lamparas compradas: {cantidad_lamparas}\n"
        ticket += f"Marca de las lamparas: {marca_lampara}"
    
    print(ticket)
else:
    print("Cantidad de lamparas inválida")




