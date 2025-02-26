n= int(input("Ingrese un numero de 5 digitos: "))

if n < 10000 or n > 99999:
    print("El numero no es de 5 digitos")
else:
    n_1= n // 10000
    n_2= ((n // 1000) % 10)
    n_3= ((n // 100) % 10)
    n_4= ((n // 10) % 10)
    n_5= n % 10
    if n_1 > n_2: 
        n_1, n_2 = n_2, n_1
    if n_2 > n_3:
        n_2, n_3 = n_3 , n_2
    if n_3 > n_4:
        n_3, n_4 = n_4, n_3 
    if n_4 > n_5:
        n_4 , n_5 = n_5 , n_4
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    if n_2 > n_3:
        n_2, n_3 = n_3 , n_2
    if n_3 > n_4:
        n_3, n_4 = n_4, n_3
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    if n_2 > n_3:
        n_2, n_3 = n_3 , n_2
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    forma_descendente= n_1 * 10000 + n_2 * 1000+ n_3 * 100+ n_4 * 10 + n_5
    forma_ascendente= n_5 * 10000 + n_4 * 1000+ n_3 * 100+ n_2 * 10 + n_1
    print("La forma descendente del numero:", n, "es:" ,forma_descendente)
    print("La forma ascendente del numero:", n, "es:", forma_ascendente)