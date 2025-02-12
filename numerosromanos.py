numero=int(input("Ingrese un numero entre el 1-9: "))
resultado=""
if numero <=3:
    resultado=numero*"I"
elif numero == 4:
    resultado= "IV"
elif numero >= 5 and numero <=8:
    resultado= "V" +(numero-5)*"I"
elif numero == 9:
    resultado= "IX"
elif numero >= 10:
    resultado = "No es un numero valido"
print("El",numero, "en romano es: ",resultado)