from os import system
system('cls')

'''2. Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la
bolsa de valores:
De los inversionistas, no se sabe cuántos, registrar:
● Nombre
● Monto en pesos de la operación (no menor a $10000)
● Cantidad de instrumentos
● Tipo (CEDEAR, BONOS, MEP)
Calcular e informar:
a. Tipo de instrumento que más se operó.
b. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más
de $50000.
c. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que
menos dinero invirtió.
d. Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se
encuentre entre $20000 y $50000'''

carga_inversionistas = "si"
flag_menos_invirtio = True
flag_menos_invirtio_mep = True
cantidad_cedear = 0
cantidad_bonos = 0
cantidad_mep = 0
cantidad_150_200 = 0
cantidad_mep_inversion = 0
total_usuarios = 0

while carga_inversionistas == "si":
    nombre = input("Nombre: ")
    
    monto = float(input("Monto (no menor a $10000): "))
    while monto < 10000:
        monto = float(input("Monto (no menor a $10000): "))
    
    cantidad_instrumentos = int(input("Cantidad de instrumentos: "))
    while cantidad_instrumentos < 0:
        cantidad_instrumentos = int(input("Cantidad de instrumentos (no menor a 0): "))
        
    tipo = input("Tipo (CEDEAR, BONOS, MEP): ")
    while tipo != "CEDEAR" and tipo != "BONOS" and tipo != "MEP":
        tipo = input("Tipo (CEDEAR, BONOS, MEP):")
    
    if tipo == "CEDEAR":
        cantidad_cedear += 1
    elif tipo == "BONOS":
        cantidad_bonos += 1
        if (cantidad_instrumentos > 149 and cantidad_instrumentos < 201) and monto > 50000:
            cantidad_150_200 += 1
        
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
        if monto > 19999 and monto < 50001:
            cantidad_mep_inversion += 1
        
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
    carga_inversionistas = input("¿Desea ingresar otro inversionista (si/no)?: ")

tipo_mas_operado = "MEP"
if cantidad_bonos > cantidad_cedear and cantidad_bonos > cantidad_mep:
    tipo_mas_operado = "BONOS"
elif cantidad_cedear > cantidad_bonos and cantidad_cedear > cantidad_mep:
    tipo_mas_operado = "CEDEAR"

#porcentaje
porcentaje_mep = (cantidad_mep_inversion * 100) / total_usuarios

msje = f"a. Tipo de instrumento que más se operó: {tipo_mas_operado}\n"
msje += f"b. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000: {cantidad_150_200}\n"
msje += f"c. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió:\nNombre: {nombre_menos_invirtio}\nCantidad de instrumentos: {cantidad_instrumentos_menos_invirtio}\n"
msje += f"d. Porcentaje de usuarios que invirtieron en MEP, cuando el monto es entre $20000 y $5000: {porcentaje_mep}%\n"
print(msje)