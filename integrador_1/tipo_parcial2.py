from os import system
system("cls")
'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de valores:
De los inversionistas, no se sabe cuántos, registrar:
#?Nombre
#?Monto en pesos de la operación (no menor a $10000)
#?Cantidad de instrumentos
#?Tipo (CEDEAR, BONOS, MEP)   

Calcular e informar:    
    -Tipo de instrumento que más se operó.
    -Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
    -Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
    -Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.  

'''
carga_inversionista = "si"
cantidad_cedear = 0
cantidad_bonos = 0
cantidad_mep = 0
cantidad_usuarios_bonos = 0
cantidad_mep_monto = 0
flag_menos_invirtio = True
total_usuarios = 0

while carga_inversionista == "si":
    nombre = input("Nombre del inversionista: ")
    
    monto = int(input("Monto de la operación (no menor a $10000): "))
    while monto < 10000:
        monto = int(input("Error!!!. Vuelva ingresar monto de la operación (no menor a $10000): "))
        
    cantidad_instrumentos = int(input("Cantidad de instrumentos: "))
    
    tipo = input("Tipo de instrumento (CEDEAR/BONOS/MEP): ")
    while tipo != "CEDEAR" and tipo != "BONOS" and tipo != "MEP":
        tipo = input("Error!!!. Vuelva ingresar tipo de instrumento (CEDEAR/BONOS/MEP): ")

    #Tipo de instrumento que más se operó.
    if tipo == "CEDEAR":
        cantidad_cedear += 1
    elif tipo == "BONOS":
        cantidad_bonos += 1
        
        #Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
        if (cantidad_instrumentos > 149 and cantidad_instrumentos < 201) and monto > 50000:
            cantidad_usuarios_bonos += 1 
        
        #Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
        if flag_menos_invirtio == True:
            flag_menos_invirtio = False
            nombre_menos_invirtio = nombre
            cantidad_instrumentos_menos_invirtio = cantidad_instrumentos
            monto_menos_invirtio = monto
        elif monto < monto_menos_invirtio:
            nombre_menos_invirtio = nombre
            cantidad_instrumentos_menos_invirtio = cantidad_instrumentos
            monto_menos_invirtio = monto
    elif tipo == "MEP":
        cantidad_mep += 1
        
        #Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.
        if monto > 19999 and monto < 50001:    
            cantidad_mep_monto += 1 

        #Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
        if flag_menos_invirtio == True:
            flag_menos_invirtio = False
            nombre_menos_invirtio = nombre
            cantidad_instrumentos_menos_invirtio = cantidad_instrumentos
            monto_menos_invirtio = monto
        elif monto < monto_menos_invirtio:
            nombre_menos_invirtio = nombre
            cantidad_instrumentos_menos_invirtio = cantidad_instrumentos
            monto_menos_invirtio = monto

    total_usuarios += 1
    carga_inversionista = input("Desa ingresar otro inversionista (si/no): ")

# -Tipo de instrumento que más se operó.
if cantidad_cedear > cantidad_bonos and cantidad_cedear > cantidad_mep:
    msje = "CEDEAR"
elif cantidad_bonos > cantidad_cedear and cantidad_bonos > cantidad_mep:
    msje = "BONOS"
else:
    msje = "MEP"

#Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.
if cantidad_mep_monto > 0:
    porcentaje_mep =(cantidad_mep_monto * 100) / total_usuarios
else:
    porcentaje_mep = 0

informe =\
f''' 
===============================================================================================
a) El tipo de instrumento que más se operó es {msje}
b) Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000: {cantidad_usuarios_bonos}
c) Nombre y cantidad de instrumentos que compró BONOS o MEP, que menos dinero invirtió: 
    Nombre: {nombre_menos_invirtio} 
    Cantidad de instrumentos: {cantidad_instrumentos_menos_invirtio}
d) Porcentaje que invirtieron en MEP, cuando el monto está entre $20000 y $50000: {porcentaje_mep}%'''

print(informe)