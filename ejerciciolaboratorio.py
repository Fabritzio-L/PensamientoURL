#1
comentario="Python es un lenguaje poderoso"
palabras=comentario.split()
print("Primera palabra:",palabras[0],", Última palabra:",palabras[4])

#2
comentario="Hola  mundo en  Python"
palabras=comentario.split()
comentario_sin_espacio= " ".join(palabras)
print(comentario_sin_espacio)

#3.
comentario="usuario@gmail.com"
palabras=comentario.split("@")[1]
print(palabras)

#4.
documento= input("Ingrese un documento: ")
print(documento.endswith(".pdf"))

#5
texto= input("Ingrese un texto: ")
palabras=texto.split()[::-1]
palabras=" ".join(palabras)
print(palabras)

#6
solicitud=input("Ingrese lo que necesite: ")
poema1= "Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podráromperse el eje de la tierra, Como un débil cristal."
canto1="Eres como la noche, callada y constelada. Tu silencio es de estrella, tan lejano y sencillo. Me gustas cuando callas porque estás como ausente. Distante y dolorosa como si hubieras muerto."
palabras_clave_poema= ["amor","quiero","amo","cariño","poema"]
palabras_clave_canto= ["canto","alegria","cancion"]
solicitud=solicitud.lower()
if palabras_clave_poema[0] in solicitud or palabras_clave_poema[1] in solicitud or palabras_clave_poema[2] in solicitud or palabras_clave_poema[3] in solicitud or palabras_clave_poema[4] in solicitud:
    print(poema1)
elif palabras_clave_canto[0] in solicitud or palabras_clave_canto[1] in solicitud or palabras_clave_canto[2] in solicitud:
    print(canto1)