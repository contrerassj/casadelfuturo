#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 4

print("Bienvenido al Sistema de Homebaning de TuDolarBank.com.\n\n")

def Conversion(Monto):
    dOficial=77.75
    dSolidario=dOficial*1.3
    dBlue=137
    if Monto>200:
        print("El importe a pagar por la compra de U$S",Input1,"es $","{:.2f}".format(Input1*dBlue))
    elif Monto>=100:
        print("El importe a pagar por la compra de U$S",Input1,"es $","{:.2f}".format(Input1*dSolidario))
    else:
        print("El importe a pagar por la compra de U$S",Input1,"es $","{:.2f}".format(Input1*dOficial))

Aux1=0
while Aux1<3:
        Input1=int(input("Ingrese el monto de dólares que desea comprar: "))
        if Input1<0:
            print("El valor ingresado es inválido.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
                break
        elif Input1<50:
            print("La compra mínima es de U$S100.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
                break
        else:
            print("El monto a comprar es de U$S",Input1)
            Conversion(Input1)
            break