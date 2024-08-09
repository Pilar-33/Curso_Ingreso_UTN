from os import system
system('cls')
'''
Una librería que se especializa en venta de libros importados desea calcular ciertas métricas en base a 
las ventas de sus productos.
Se ingresa de cada venta:
Título del libro
Género: (Ciencia ficción – Drama – Terror)
Material del libro (rústica – tapa dura)
Importe (No pueden ser números negativos ni mayor a los 30000)
Se pide:                          	
a) El libro más barato de drama con su importe.
b) Del libro más caro, el título.
c) Porcentaje de libros de cada género
d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700.
'''
carga_datos = "si"
flag_drama_barato = True
flag_libro_caro = True
cantidad_libros = 0
cantidad_drama = 0
cantidad_ciencia_ficcion = 0
cantidad_terror = 0
contador_ciencia_menos700 = 0

while carga_datos == "si":
    titulo = input("Título del libro: ")
    
    genero = input("Genero del libro (Ciencia ficcion/Drama/Terror): ")
    while genero != "Ciencia ficcion" and genero != "Drama" and genero != "Terror":
        genero = input("Error!!!. Vuelva ingresar género del libro (Ciencia ficcion/Drama/Terror): ")
        
    material = input("Mterial del libro (rustica/tapa dura): ")
    while material != "rustica" and material != "tapa dura":
        material = input("Error!!!. Vuelva ingresar material del libro (rustica/tapa dura): ")
        
    importe = int(input("Importe del libro (no negativos o mayor a 30000): "))
    while importe < 0 or importe > 30000:
        importe = int(input("Error!!!. Vuelva ingresar importe del libro (no negativos o mayor a 30000): "))
        
    #a) El libro más barato de drama con su importe.
    if genero == "Drama":
        cantidad_drama += 1
        if flag_drama_barato == True:
            flag_drama_barato = False
            importe_barato_drama = importe
        elif importe < importe_barato_drama:
            importe_barato_drama = importe
    elif genero == "Ciencia ficcion":
        cantidad_ciencia_ficcion += 1
        #d) La cantidad de libros que sean de ciencia ficción y cuesten menos de $700
        if importe < 700:
            contador_ciencia_menos700 += 1
    else:
        cantidad_terror += 1
            
    #b) Del libro más caro, el título.
    if flag_libro_caro == True:
        flag_libro_caro = False
        importe_caro = importe
        titulo_caro = titulo
    elif importe > importe_caro:
        importe_caro = importe
        titulo_caro = titulo
    
    cantidad_libros += 1
    carga_datos = input("Desea cargar otro libro? (si/no): ")
#c) Porcentaje de libros de cada género 
# cantidad libros -----> 100
# cantidad drama ----->   x
# x = (cantidad drama* 100)/ cantidad drama 
porcentaje_drama = (cantidad_drama*100)/cantidad_libros
porcentaje_ciencia_ficcion = (cantidad_ciencia_ficcion*100)/cantidad_libros
porcentaje_terror = (cantidad_terror*100)/cantidad_libros
msje = "*"*65 
msje += f"\nLibro drama mas barato: ${importe_barato_drama}\n"
msje += f"Libro más caro, el título: {titulo_caro} \n"
msje += f"Porcentaje de libro de cada género: \nCiencia ficcion: \n{porcentaje_ciencia_ficcion}% \nDrama: {porcentaje_drama}% \nTerror: {porcentaje_terror}% \n"
msje += f"La cantidad de libros de ciencia ficción y cuesten menos de $700: {contador_ciencia_menos700}"

print(msje)