#Fabritzio Alejandro Lopez Castillo 1507525
##Ejercicio 1
n = int(input("Ingrese el tamaño array: ")) 
m= int(input("Ingrese un multiplo: "))
salida = []
for i in range (0,n):
    salida.append(i*m)
print(salida)

#Ejercicio 2
n = int(input("Ingrese la cantidad de nombres: "))
nombres = []
longitud = []
for i in range(n):
    nombre = input("Ingrese los nombres: ")
    nombres.append(nombre)
    longitud.append(len(nombre))
print("Los nombres y sus longitudes son: ")
print(nombres, longitud)


#Escenario 
n = int(input("Ingrese el número de clientes: "))
respuestas = []
for i in range(n):
    while True:
        respuesta = input(f"Cliente {i+1}: ")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if respuesta in [1, 2, 3, 4, 5]:
                respuestas.append(respuesta)
                break
        print("Número no válido. Ingrese un número entre 1 y 5.")

conteo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for r in respuestas:
    conteo[r] += 1

categorias = {5: "Excelente", 4: "Muy Buena", 3: "Buena", 2: "Regular", 1: "Malo"}

print("Respuestas:")
for clave in [5, 4, 3, 2, 1]:
    print(f"{categorias[clave]}: {conteo[clave]}")

frecuencia_maxima = 0
respuesta_frecuente = 0
for clave in conteo:
    if conteo[clave] > frecuencia_maxima:
        frecuencia_maxima = conteo[clave]
        respuesta_frecuente = clave
print(f"\nMás frecuente: {respuesta_frecuente}")

suma = 0
for r in respuestas:
    suma += r
promedio = suma / n
print(f"Promedio: {promedio:.2f}")

menores_promedio = []
for i in range(n):
    if respuestas[i] < promedio:
        menores_promedio.append(i + 1)
porcentaje_menor = (len(menores_promedio) / n) * 100

print(f"Porcentaje menor al promedio: {porcentaje_menor:.2f}%")
