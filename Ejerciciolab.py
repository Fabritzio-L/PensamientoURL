#Ejercicio no. 1 
consumo = int(input("Ingrese su consumo en m3: "))

if consumo < 15:
    tarifa = 5
elif 15 <= consumo <= 30:
    num_habitantes = int(input("Ingrese el numero de habitantes: "))
    if num_habitantes > 3:
        tarifa = 4
    elif num_habitantes == 3:
        tarifa = 4.5
    else:
            tarifa = 5
elif consumo > 30:
    num_habitantes = int(input("Ingrese el numero de habitantes: "))
    if num_habitantes > 5:
        tarifa = 3.5
    elif num_habitantes % 2 ==0:
        tarifa = 4
    else: 
        tarifa = 4.2

total = consumo * tarifa
print(f"La tarifa por m3 en total es de: Q{total}")

#Ejercicio no. 2 
placa = input("Ingrese la placa del vehículo: ").upper()  
año = int(input("Ingrese el año del vehículo: "))

ultimo_digito = int(placa[-1])  
advertencia = ""


if ultimo_digito % 2 == 0: 
    restriccion = "No circula los lunes"
else: 
    restriccion = "No circula los viernes"

if año % 2 == 0:
    restriccion += " y los sábados hasta el mediodía"

año_actual = 2025 
if año_actual - año > 25:
    advertencia = "Debe recibir mantenimiento obligatorio."
    print(advertencia)
print(f"Restricción: {restriccion}")

