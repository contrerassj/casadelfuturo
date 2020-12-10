#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús

def Ahorrista():
    Aux3=0
    while Aux3<3:
        Input3=int(input("Ingrese el plazo de la inversión en meses (12 a 36): "))
        if Input3<12 or Input3>36:
            print("El plazo ingresado es inválido.")
            Aux3+=1
            if Aux3==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El plazo ingresado es de ",Input3, " meses.")
            break

Ahorrista()