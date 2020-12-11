#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.6

print("Bienvenido al Sistema de Cobro por Telefonía de Chismefon.\n\n")


Aux1=0
while Aux1<3:
        Input1=int(input("Ingrese en la duración de la llamada, en segundos: "))
        if Input1<1:
            print("El valor ingresado es inválido.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
        else:
            print("La duración de la llamada es de",Input1, "segundos.")
            break
if Input1>600:
    Monto=Input1*0.5*1.21/60
    print("El valor de la llamada por", "{:.2f}".format(Input1/60), "minutos es de $", "{:.2f}".format(Monto))
elif Input1>480:
    Monto=Input1*0.7*1.21/60
    print("El valor de la llamada por", "{:.2f}".format(Input1/60), "minutos es de $", "{:.2f}".format(Monto))
elif Input1>300:
    Monto=Input1*0.8*1.21/60
    print("El valor de la llamada por", "{:.2f}".format(Input1/60), "minutos es de $", "{:.2f}".format(Monto))
else:
    Monto=Input1*1.21/60
    print("El valor de la llamada por", "{:.2f}".format(Input1/60), "minutos es de $", "{:.2f}".format(Monto))