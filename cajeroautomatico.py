#Fabritzio Alejandro Lopez Castillo - 1507525
saldo_actual = 3000
intentos = 0
maximo_intentos= 3 
while True:
    retiro = int(input("Ingrese el monto a retirar: "))
    if retiro ==0:
        print("Operación cancelada, feliz día.")
        break
    if retiro > saldo_actual:
        intentos += 1 
        
        print(f"Saldo insuficiente. Su numero de intentos es {maximo_intentos-intentos}")
        if intentos >= maximo_intentos:
            print("Demasiados intentos fallidos, operacion cancelada feliz dia.")
            break
    else:
        saldo_actual-= retiro 
        print(f"Retiro exitoso. Su nuevo saldo actual es de: {saldo_actual}")

        if saldo_actual ==0:
            print("Su saldo esta agotado, feliz día")
            break 
            
        