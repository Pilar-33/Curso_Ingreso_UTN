contador = personas_con_fiebre = personas_sin_fiebre = numero_f = numero_m = numero_nb = 0

while contador < 5:
    nombre = input(f"Nombre del {contador+1}° paciente: ")
    
    temperatura = float(input(f"Temperatura del {contador+1}° paciente (35 y 42): "))
    while temperatura < 35 or temperatura > 42:
        temperatura = float(input(f"Vuelva ingresar la Temperatura del {contador+1}° paciente: "))
    
    personas_con_fiebre += 1 if temperatura >= 37 else 0
    personas_sin_fiebre += 1 if temperatura < 37 else 0
    
    sexo = input(f"Sexo del {contador+1}° paciente (f, m, nb): ").lower()
    while sexo not in ("f", "m", "nb"):
        sexo = input(f"Vuelva ingresar el sexo del {contador+1}° paciente: ").lower()

    if sexo == "f": numero_f += 1
    elif sexo == "m": numero_m += 1
    else: numero_nb += 1

    edad = int(input(f"Edad del {contador+1}° paciente (mayor a 0): "))
    while edad <= 0:
        edad = int(input(f"Vuelva ingresar la Edad del {contador+1}° paciente: "))

    contador += 1
    print()

print("Punto A:")
if numero_f > numero_m and numero_f > numero_nb:
    print(f" ● Sexo más ingresado fue femenino(f): {numero_f}")
elif numero_m > numero_f and numero_m > numero_nb:
    print(f" ● Sexo más ingresado fue masculino(m): {numero_m}")
else:
    print(f" ● Sexo más ingresado fue no binario(nb): {numero_nb}")

print(f"""Punto B:
 ● Porcentaje de personas con fiebre: {(personas_con_fiebre*100)/contador:.2f}%
 ● Porcentaje de personas sin fiebre: {(personas_sin_fiebre*100)/contador:.2f}%""")
