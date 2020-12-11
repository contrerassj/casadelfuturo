#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.1

def Inversion():
    print("\nGracias por invertir en Sistema de Capitales de Riesgo del Banco Fantasía.")
    print("Puede elegir entre 3 de nuestros sistemas de inversiones, según prefiera: ")
    print("-Inversiones Ahorristas: 3% Interanual\n-Inversiones Terceros: 4% Intermensual\n-Intermensual de Riesgo: 5% Intermensual")
    Aux2=0
    while Aux2<3:   
        Input2=input("Ingrese Sistema de Inversión deseado. (Ahorrista: a / Terceros: t / Riesgo: r): ")
        if Input2=="a":
            Metodo(1.03)
            break
        elif Input2=="t":
            Metodo(1.04)
            break
        elif Input2=="r":
            Metodo(1.05)
            break
        else:
            print("El comando ingresado es inválido.")
            Aux2+=1
            if Aux2==3:
                print("Límite de intentos alcanzado.")


def Metodo(factor):
    Aux3=0
    while Aux3<3:
        Input3=int(input("Ingrese el plazo de la inversión en meses (12 a 36): "))
        if Input3<12 or Input3>36:
            print("El plazo ingresado es inválido.")
            Aux3+=1
            if Aux3==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El plazo ingresado es de",Input3, "meses.")
            break
    Aux3=0
    while Aux3<3:
        Input4=int(input("Ingrese el valor entero de la inversión: $"))
        if Input4<0:
            print("El monto ingresado es inválido.")
            Aux3+=1
            if Aux3==3:
                print("Límite de intentos alcanzado.")
        elif Input4<10000:
            print("El monto ingresado es insuficiente.")
            Aux3+=1
            if Aux3==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El monto ingresado es de $",Input4, ".")
            break
    Monto=Input4
    i=1
    while i<=Input3:
        Monto=Monto*factor
        i+=1
    print("El monto obtenido por la inversión de $",Input4, "durante",Input3, "meses es de $",int(Monto),".")
    print("La ganancia neta es de $",int(Monto-Input4),".")


print("Bienvenido al Sistema de Capitales de Riesgo del Banco Abstracto.\n\n")
Aux1=0
while Aux1<3:
    Input1=input("¿Desea iniciar una operación de inversión en nuestro banco? (s/n): ")
    if  not(Input1=="s" or Input1=="n"):
        print("El comando ingresado es inválido.")
        Aux1+=1
        if Aux1==3:
            print("Límite de intentos alcanzado.")
    elif Input1=="n":
        print("Gracias por visitar el Sistema de Capitales de Riesgo del Banco Abstracto.")
        print("Operación finalizada")
        break
    else:
        Inversion()
        break
