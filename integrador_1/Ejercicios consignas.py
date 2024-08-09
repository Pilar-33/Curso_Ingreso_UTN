'''
Una librería que se especializa en venta de libros importados desea calcular ciertas métricas en base a las ventas de sus productos.
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
################################################################################
'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de valores:
De los inversionistas, no se sabe cuántos, registrar:
Nombre
Monto en pesos de la operación (no menor a $10000)
Cantidad de instrumentos
Tipo (CEDEAR, BONOS, MEP)   

Calcular e informar:    
    -Tipo de instrumento que más se operó.
    -Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
    -Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
    -Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.  

'''
################################################################################
# A PARTIR DE ACÁ SON TODOS EJERCICIOS LARGOS
'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a 
un listado de viajeros para un nuevo transbordador de SpaceX:

Para ello deberás programar el botón 'Cargar Viajeros' para poder cargar los siguientes datos de 5 personas:
    * Nombre
    * Altura (entre 60 cm y 200 cm)
    * Peso (entre 40 kilos y 250 kilos)
    * Edad (entre 1 y 100 ) 

B) Al presionar el botón "Mostrar Datos Crudo" se deberán listar todos los datos de los usuarios y 
    su posición en la lista (por terminal) 

    0) 
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de más de 50 años
    1) 
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de menos de 50 años
    2)
        A- El nombre de la persona con la mayor altura ingresada
        B- La cantidad de personas de más de 80 kilos
    3)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 100 kilos
    4) 
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de más de 100 cm de altura
    5) 
        A- El nombre de la persona con la menor edad ingresada
        B- La cantidad de personas de menos de 170 cm de altura 
    6) 
        A- El nombre de las personas que NO superen la edad promedio
        B- La cantidad de personas de menos de 160 cm de altura
    7) 
        A- El nombre de las personas que NO superen la altura promedio
        B- La cantidad de personas de menos de 80 kilos
    8)
        A- El nombre de las personas que NO superen el peso promedio
        B- La cantidad de personas de más  de 50 kilos
    9) 
        A- El nombre de las personas que SI superen el peso promedio
        B- La cantidad de personas de menos de 18 años
'''
################################################################################

'''
Un jugador de League of Legends tiene un fin de semana libre y 
va a jugar partidas hasta que se canse.

Para mejorar su jugabilidad, por cada partida jugada va a registrar:
    * Modo de juego ("Normal", "Clasificatoria", "ARAM")
    * Nombre del personaje que usó
    * La cantidad de asesinatos a favor (No puede ser negativo)
    * Muertes en contra (No puede ser negativo)
    * Asistencias a favor. (No puede ser negativo, hasta 40)

Consignas:
    0) - El modo de juego más jugado.
    1) - El modo de juego menos jugado.
    2) - El personaje con el cual murió más.
    3) - El personaje con el cual asistio más.
    4) - El promedio de asesinatos a favor en modo Clasificatoria.
    5) - El promedio de muertes en contra en modo ARAM.
    6) - El promedio de asistencias en modo Normal.
    7) - De la partida con mas muertes en contra, el nombre del personaje y el modo de juego.
    8) - De la partida con mas asistencias a favor, el nombre del personaje y el modo de juego.
    9) - De la partida con mas asesinatos a favor, el nombre del personaje y el modo de juego.
'''
################################################################################
'''
El profesor OAK de pueblo paleta quiere que construyas un segundo modelo prototipico 
de pokedex con 10 pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon.
    * El tipo de color (azul , amarillo, blanco , otro).
    * La altura del pokemon en centimetros (validar que sea mayor a 10 y menor a 200).

Consignas
    #! 0) - Cantidad de pokemones de color amarillo.
    #! 1) - Cantidad de pokemones de color blanco.
    #! 2) - Nombre, color y altura del pokemon mas alto.
    #! 3) - Nombre, color y altura del pokemon mas bajo.
    #! 4) - Cantidad de pokemones con mas de 100 cm de altura.
    #! 5) - Cantidad de pokemones con menos de 100 cm de altura.
    #! 6) - color de los pokemones del color que mas pokemones posea.
    #! 7) - color de los pokemones del color que menos pokemones posea.
    #! 8) - el promedio de altura de todos los pokemones ingresados.
    #! 9) - el promedio de altura de todos los pokemones azules.
'''
################################################################################
'''

Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. 
Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.
 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


Consignas:
    #! 0) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 1) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 2) - Calcula el número total de entradas compradas por personas mayores de 30 años y 
    #!          su precio promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa (OMITO).
    #! 5) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito (OMITO)
    #! 6) - Encuentra los nombres y las edades de la personas que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (OMITO)
    #! 7) - Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 8) - Calcula el monto total recaudado por la venta de entradas de tipo "General" y 
    #!          pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.
    #! 9) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''
################################################################################

'''
El presentador del torneo de artes marciales quiere que desarrolles un modelo prototipico 
de scouter (un detector basicamente) para ver ciertas metricas de los participantes.
de cualquier parte del universo, es por eso que deberas realizar la carga 
de 10 participantes.

Para ello deberas programar el boton "Cargar Guerreros" para poder cargar 10 Caballeros del zodiaco.
Los datos que deberas pedir para los Caballeros del zodiaco son:
    * El nombre del Caballeros del zodiaco.
    * El tipo de armadura (Bronce, Plata, Oro, Divina, Oscura).
    * La cantidad de cosmos del guerrero (entre 25000 y 150000).


Consignas:
    #! 0) - Cantidad de guerreros de armadura de Oro.
    #! 1) - Cantidad de guerreros de armadura Divina.
    #! 2) - Nombre, Armadura y Cosmos del guerrero mas fuerte.
    #! 3) - Nombre, Raza y Poder del guerrero mas debil.
    #! 4) - Cantidad de guerreros con mas de 85000 de poder y armadura de Plata.
    #! 5) - Cantidad de guerreros con menos de 50000 de poder y armadura de Bronce.
    #! 6) - Armadura que mas guerreros posea inscriptos.
    #! 7) - Armadura que menos guerreros posea inscriptos.
    #! 8) - el promedio de cosmos de todos los guerreros con armadura Oscura.
    #! 9) - el porcentaje, tipo de armadura y promedio de cosmos de guerreros 
    #!      de cada tipo de armadura, respecto al total de guerreros.
'''