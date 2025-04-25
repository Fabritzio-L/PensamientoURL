#Fabritzio Lopez
#Ejercicio 1
def es_par_o_impar(n):
    if n % 2 ==0:
        print("Es par")
    else:
        print("Es impar")


es_par_o_impar(11)


#Ejercicio 2
def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
numeros =[1,2,3,4,5]
print(suma_lista(numeros))
#Ejercicio 3
def  cuenta_regresiva(n):
    if n < 0:
        print("Despegue")
    else:
        print(n)
        cuenta_regresiva(n-1)
cuenta_regresiva(10)
#Ejercicio 4
def cuenta_ascendente(n, act=1):
    if act <= n:
        print(act)
        cuenta_ascendente(n,act + 1)
cuenta_ascendente(1)
#Ejercicio 5
def suma_hasta(numb):
    sum = 0
    for i in range(1,numb+1):
        sum +=i
    print(sum)
suma_hasta(3)
#Ejercicio 6
def factorial(num,resultado=1):
    if num > 1:
        factorial(num-1,resultado*num)
    else:
        print(resultado)
factorial(1)
#Ejercicio #7
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        menor_del_resto = minimo(lista[1:])
        if lista[0] < menor_del_resto:
            return lista[0]
        else:
            return menor_del_resto
print(minimo([5, 3, 8, 6, 2])) 

#Juego interactivo
import time
import random
def adivina_el_numero(numero, intentos, tiempo_inicio):
    if intentos == 0:
        print(f"¡Te has quedado sin intentos! El número era {numero}.")
        return
    intento = int(input(f"Te quedan {intentos} intentos. Ingresa tu número: "))
    if intento == numero:
        tiempo_final = time.time()
        tiempo_total = round(tiempo_final - tiempo_inicio, 2)
        print(f"¡Felicidades! Adivinaste el número {numero} en {tiempo_total} segundos.")
    elif intento < numero:
        print("Demasiado bajo.")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)
    else:
        print("Demasiado alto.")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)
numero_secreto = random.randint(1, 100)
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")
tiempo_inicio = time.time()
adivina_el_numero(numero_secreto, 10, tiempo_inicio)
