from os import system 
system("cls")
#Escribe un programa que pida al usuario el total de una cuenta en un restaurante
#y el porcentaje de propina que desea dejar. 
#El programa debe calcular y mostrar la cantidad de propina y el total a pagar
#antes y luego de la misma:
#Precio: x
#Propina: x
#Precio con propina: x
print("""=====================================================
                    RESTAURANTE COMIDA CASERA
======================================================""")
    
total_cuenta = float(input("Ingrese total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese porcentaje propina: "))

#calcula propina
propina = total_cuenta * (porcentaje_propina/100)
total_con_propina = total_cuenta + propina

#1era forma de imprimir datos
"""msj = \
f'''
    ===========================
        CUENTA DE RESTAURANTE
    ===========================
    Precio: ${total_cuenta:.2f}
    Propina: ${propina:.2f}
    Precio con propina: ${total_con_propina:.2f}
'''
print(msj)"""

#2da forrma de imprimir datos
#precio= f"Precio: ${total_cuenta:.2f}"
#propina= f"Propina: ${propina:.2f}"
#precio_con_propina= f"Precio con propina: ${total_con_propina:.2f}"
#print("\nCUENTA DE RESTAURANTE "+"\n"+precio + "\n" + propina +"\n" + precio_con_propina)

"""msj= \
'''
===========================
    CUENTA DE RESTAURANTE
===========================
Precio: ${0:.2f}
Propina: ${1: .2f}
Precio con propina: ${2:.2f}
'''.format(total_cuenta, propina, total_con_propina)
print(msj)"""
#####################################################
msj = f"Precio: ${total_cuenta:.2f}\n"
msj += f"Propina: ${propina: .2f}\n" 
msj += f"Precio con propina: ${total_con_propina:.2f}"
print(msj)


