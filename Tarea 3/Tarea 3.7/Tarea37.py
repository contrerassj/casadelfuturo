#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.7

from datetime import datetime, timedelta
Meses={"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}

print("Bienvenido al Sistema de Análisis de Fechas.\n\n")

InputY=int(input("Ingresar el año de análsis (YYYY): "))

if InputY%4==0 or (InputY%100==0 and InputY%400==0):
    InputYType="Bisiesto"
    print("El año de análisis", InputY, "es",InputYType)
    Meses["2"]=29
else:
    InputYType="No Bisiesto"
    print("El año de análisis", InputY, "es",InputYType)

Aux1=0
while Aux1<3:
        InputM=int(input("Ingresar el mes de análsis (MM): "))
        if InputM<0 or InputM>12:
            print("El valor ingresado es inválido.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El mes ingresado es",InputM)
            break

Aux1=0
while Aux1<3:
        InputD=int(input("Ingresar el día de análsis (DD): "))
        if InputD<0 or InputD>Meses[str(InputM)]:
            print("El valor ingresado es inválido.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El día ingresado es",InputD)
            break

InputStrDate=f"{InputD}/{InputM}/{InputY}"
InputDate=datetime.strptime(InputStrDate, "%d/%m/%Y")
InputDateAnterior = InputDate + timedelta(days=-1)
InputDatePosterior = InputDate + timedelta(days=+1)

print("La fecha ingresada es: ", InputDate)
print("La fecha anterior es",InputDateAnterior,"y la fecha posterior es",InputDatePosterior)
print("El último día del mes ingresado es",Meses[str(InputM)],".")
print("Faltan ",int(Meses[str(InputM)])-InputD, "días para llegar al final del mes de análisis.")