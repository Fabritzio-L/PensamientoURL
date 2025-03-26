#Ejercicio 1
for i in range(1,11):
    if i % 2 != 0:
        print(f"Los numeros impares de 0-10 son: {i}")


#Ejercicio no. 2
x = 1
contador=0
while x < 11:
    if x % 2 ==0:
        x+=1
        continue
    print(x)
    x+=1


#Escenario 1
palabra_secreta = "chupacabra"
while True:
    palabra = input("Ingrese la palabra secreta para temrinar el bucle: ")
    if palabra == palabra_secreta:
        print("Has dejado el bucle con exito")
        break


#Escenario 2
palabra_usuario = input("Ingresa una palabra: ")
palabra_usuario= palabra_usuario.upper()  # Convertir la palabra a mayúsculas

for letra in palabra_usuario:
    if letra in "AEIOU":  # Si la letra es una vocal, omitirla
        continue
    print(letra)  # Imprimir solo las consonantes en líneas separadas
