dias=["Lunes:","Martes:","Miercoles:","Jueves:","Viernes:"]
niveles_azucar=[130,160,95,175,160]
niveles_sal=[2000,2400,1800,2400,2700]
presion=[115,130,110,125,175]
def clasificar_presion(sistolica):
    if sistolica < 120:
        return "Normal"
    elif 120<=sistolica<=129:
        return "Elevada"
    elif 130 <= sistolica<= 139:
        return "Hipertension Etapa 1"
    elif sistolica >=140:
        return "Hipertension Etapa 2"
print("Resultados semanales:")
print("-------------------------------------------")
for i in range(len(dias)):
    print(dias[i])
    azucar= niveles_azucar[i]
    if 70<= azucar <= 140:
        print(f"Azucar: {azucar} mg/dL. Niveles normales")
    else: 
        print(f"Azucar { azucar} mg/dL. Niveles altos, ALERTA")
    sal=niveles_sal[i]
    if sal<2300:
        print(f"Sal: {sal} mg/dia. Niveles normales")
    else:
        print(f"Sal: {sal} mg/dia. Niveles Altos, ALERTA")
    pres= presion[i]
    clasificacion=clasificar_presion(pres)
    print(f"Presion:{pres} mmHg. {clasificacion}")
    print("-------------------------------------------")
total_azucar=0
total_sal=0
total_presion=0

for i in range(len(dias)):
    total_azucar+= niveles_azucar[i]
    total_sal+=niveles_sal[i]
    total_presion=presion[i]
    
n=len(dias)
prom_azucar= total_azucar/n
prom_sal=total_sal/n
prom_presion=total_presion/n
print("Promedios semanales:")
print(f"El promedio de azucar es de: {prom_azucar:2} mg/dL")
print(f"El promedio de sal es de: {prom_sal:2} mg")
print(f"El promedio de presion es de: {prom_presion:2} mmHg")
