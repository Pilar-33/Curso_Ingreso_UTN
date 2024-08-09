from os import system
system('cls')
'''La juguetería El MUNDO DE CHARLY nos encarga un programa para 
conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

CONFECCIÓN DE UN COMETA: 
Medidas:
AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores
El usuario ingresará las medidas  BC, CD y AD=DA.

Detalles de construcción
Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de 
plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo 
papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la
construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.'''

#Entradas de medidas
BC = float(input('Ingrese la medida de BC (cm): '))
CD = float(input('Ingrese la medida de CD (cm): '))
AD = float(input('Ingrese la medida de AD (cm): '))

#convirtieendo datos a mts
BC = BC/100
CD = CD/100
AD = AD/100

#cálculos
#Hallando la diagonal mayor
AB = (BC**2 + AD**2)**0.5 


#perímetro de las varillas para 10 cometas
perimetro = 10*(2*AB + 2*AD + 2*BC + CD) 

# hallando área del cometa
area = (AB*CD)/2

#hallando cantidad de papel de alta resistencia para 10 cometas
papel = area*10*1.1

#Resultados
msje =f''' 
                    RESULTADOS
================================================
Varillas de plástico necesarias (m): {perimetro:.2f} m
Papel necesario para 10 cometas (m2): {papel:.2f} m2'''

print(msje)

