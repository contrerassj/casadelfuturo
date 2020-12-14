#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 6


def CargaPrecio():
    for i in BBDDproductos.keys():
        Aux1=0
        Aux2=0
        while Aux1<3:
            BBDDproductos[i][0]=input(f"ingresar precio de {i}: ")
            if BBDDproductos[i][0]=="":
                print("El valor ingresado no puede ser nulo.")
                Aux1+=1
                if Aux1==3:
                    print("Límite de intentos alcanzado.")
                    break
            elif int(BBDDproductos[i][0])<0:
                print("El valor ingresado no puede ser negativo.")
                Aux2+=1
                if Aux2==3:
                    print("Límite de intentos alcanzado.")
                    break
            else:
                BBDDproductos[i][1]=int(BBDDproductos[i][0])*0.85
                print("Se ha asignado un precio base de $","{:.2f}".format(float(BBDDproductos[i][0])), "y un precio promocional de $",
                "{:.2f}".format(float(BBDDproductos[i][1]))," al producto",i,".")
                break

def MuestraPrecios():
    Aux1=0
    while Aux1<3:
        Input01=input("\nIngrese el nombre del producto de interés, precione 'enter' para mostrar lista completa o 'x' para salir: ")
        Input1=Input01.lower()
        if Input1=="x":
            print("Gracias por utilizar el Sistema de Gestión de Precios.")
            Aux1=3
        elif Input1=="":
            for j in BBDDproductos.keys():
                print("El producto",j, "tiene un precio base de $",
                "{:.2f}".format(float(BBDDproductos[j][0])), "y un precio promocional de $",
                "{:.2f}".format(float(BBDDproductos[j][1])),", correspondiente al 15% de descuento.")
            break
        elif not(Input1 in BBDDproductos.keys()):
            print("El valor ingresado no pertenece a la base de datos.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
                break
        else:
            print("El producto",Input1, "tiene un precio base de $","{:.2f}".format(float(BBDDproductos[Input1][0])),
             "y un precio promocional de $","{:.2f}".format(float(BBDDproductos[Input1][1])),", correspondiente al 15% de descuento.")
    
print("Bienvenido al Sistema de Gestión de Precios.\n\n")
BBDDproductos={"producto1":["",""],"producto2":["",""],"producto3":["",""],"producto4":["",""],"producto5":["",""],
    "producto6":["",""],"producto7":["",""],"producto8":["",""],"producto9":["",""],"producto10":["",""]}
CargaPrecio()
MuestraPrecios()



