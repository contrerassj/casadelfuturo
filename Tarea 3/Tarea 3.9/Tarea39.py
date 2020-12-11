#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.9

"""
for i in [InputY1,InputY2]:
    if i%4==0 or (i%100==0 and i%400==0):
        print("El año de análisis", i, "es bisiesto.")
    else:
        InputYType="No Bisiesto"
        print("El año de análisis", i, "no es bisiesto.")
"""

print("Bienvenido al Sistema de Análisis de Fechas 2.0.\n\n")

InputY1=int(input("Ingresar primer año de análsis (YYYY): "))
InputY2=int(input("Ingresar segundo año de análsis (YYYY): "))
IntervaloI=list(range(InputY1,InputY2+1))
IntervaloO=[]

for i in IntervaloI:
    if i%4==0 or (i%100==0 and i%400==0) or i%10==0:
        IntervaloO.append(i)
if len(IntervaloO)==0:
    print("No existen años dentro del intervalo que cumplan con la condición establecida.")
else:
    print("Los años dentro del intervalo que cumplen con las condiciones establecidas son: ")
    for j in IntervaloO:
        print(j, end="  ")




