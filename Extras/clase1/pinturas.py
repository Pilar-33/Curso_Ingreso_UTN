from os import system
system('cls')

'''2) Para el departamento de Pinturas:
A.	Se ingresa una temperatura en Fahrenheit y la debemos mostrar en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C
    
B.	Se ingresa una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F
'''
print('''              DEPARTAMENTO DE PINTURAS
======================================================''')
temperatura_fahrenheit = float(input("Ingrese temperatura en Fahrenheit (°F): "))
temperatura_centigrados = float(input("Ingrese temperatura en centigrados (°C): "))

#conversión de °F a °C
conversion_f_c = (temperatura_fahrenheit -32) * (5/9)

#conversión de °C a °F
conversion_c_f = (temperatura_centigrados * (9/5)) + 32

msje =f'''
========================================================
A. Conversión de temperatura Fahrenheit en Centígrados:
    ({temperatura_fahrenheit}°F -32) * (5/9) = {conversion_f_c:.2f}°C
B. Conversión de temperatura Centigrados en Fahrenheit:
    ({temperatura_centigrados}°C * (9/5)) + 32 = {conversion_c_f:.2f}°F'''

print(msje)
