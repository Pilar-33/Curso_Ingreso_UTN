from os import system
system("cls")
'''1. Una librería que se especializa en venta de libros importados desea calcular ciertas
métricas en base a las ventas de sus productos.
Se ingresa de cada venta:
Título del libro
Género: (Ciencia ficción – Drama – Terror)
Material del libro (rústica – tapa dura)
Importe (No pueden ser números negativos ni mayor a los 30000)
Se pide:
a) El libro más barato de drama con su importe.
b) Del libro más caro, el título.
c) Porcentaje de libros de cada género
d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700.'''

carga_libro = "si"
flag_libro_barato_drama = True
flag_libro_caro = True
contador_libros = 0
contador_drama = 0
contador_ficcion = 0
contador_terror = 0
cantidad_ficcion_700 = 0

while carga_libro == "si":
    titulo = input("TÍtulo del libro: ")
    
    genero = input("Género (Ciencia ficcion/Drama/Terror): ")
    while genero != "Ciencia ficcion" and genero != "Drama" and genero != "Terror":
        genero = input("Género (Ciencia ficcion/Drama/Terror): ")
        
    material = input("Material (rustica/tapa dura): ")
    while material != "rustica" and material != "tapa dura":
        material = input("Material (rustica/tapa dura): ")
        
    importe = float(input("Importe: $"))
    while importe < 0 or importe > 3000:
        importe = float(input("Importe(mayor a cero y menor a 3000): $"))
    
    if genero == "Drama":
        contador_drama += 1
        if flag_libro_barato_drama == True:
            flag_libro_barato_drama = False
            libro_barato_drama = importe
            nombre_barato_drama = titulo
        elif importe < libro_barato_drama:
            libro_barato_drama = importe
            nombre_barato_drama = titulo
    elif genero == "Ciencia ficcion":
        contador_ficcion += 1
        if importe < 700:
            cantidad_ficcion_700 += 1
    else:
        contador_terror += 1
    
    if flag_libro_caro == True:
        flag_libro_caro = False
        libro_caro = importe
        nombre_caro = titulo
    elif importe > libro_caro:
        libro_caro = importe
        nombre_caro = titulo
    
    contador_libros += 1
    carga_libro = input("¿Desea agregar otro libro (si/no)?: ")

#porcentajes
#contador_libros-----> 100
#contador_drama ------> porcentaje
porcentaje_drama = (contador_drama * 100)/contador_libros
porcentaje_ficcion = (contador_ficcion * 100)/contador_libros
porcentaje_terror = (contador_terror * 100)/contador_libros

msje = "\nINFORME DE VENTA DE LIBROS\n"
msje = "==================================================================\n"
msje += f"Libro más barato de drama y su importe: \nNombre: {nombre_barato_drama} \nImporte: ${libro_barato_drama}\n"
msje += f"Libro más caro, el título es: {nombre_caro}\n"
msje += f"Porcentaje de libros de cada género:\nDrama: {porcentaje_drama}% \nCiencia ficción: {porcentaje_ficcion}% \nTerror: {porcentaje_terror}%\n"
msje += f"Cantidad de libros de ciencia ficción y cuesten menos de $700: {cantidad_ficcion_700}"
print(msje)