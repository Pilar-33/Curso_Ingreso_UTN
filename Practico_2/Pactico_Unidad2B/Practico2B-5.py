#5) Crear un programa que solicite 5 números mediante prompt.
# Calcular la suma acumulada y el promedio de los números ingresados.

print("""
╔════════════════════════════════════════════╗
║      PROGRAMA QUE SOLICITA 5 NÚMEROS       ║
║        CALCULA LA SUMA Y PROMEDIO          ║
║          DE LOS DATOS INGRESADOS           ║
╚════════════════════════════════════════════╝
""")
contador = 0
suma = 0

while contador < 5:
    numero = float(input(f"Ingrese el {contador+1}° número: "))
    contador += 1
    suma += numero
    
promedio = suma/contador

msje = \
f'''
════════════════════════════════════════════════
La suma de los números ingresados es: {suma}
El promedio de los números es: {promedio:.2f}
════════════════════════════════════════════════
El programa finalizó exitosamente.. (●'◡'●) '''

print(msje)