#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.2

def Pago(Ht):
    print("El número de horas simples trabajadas es de ",Ht,".")
    if Ht>40:
        print("El total de horas extras trabajadas es de ",Ht-40,".")
    print("El precio de cada hora simple es de $100.")
    print("El total a pagar por horas simples de $", Ht*100,".")
    if Ht>40:
        print("El total a pagar por horas extras es $",(Ht-40)*150,".")
        print("El pago neto por horas simples y extras es de $",Ht*150-2000,".")
    


print("Bienvenido al Sistema de Contable de Recursos Humanos.\n\n")
Aux=0
while Aux<3:   
        Ht=int(input("Introduzca el número entero de horas trabajadas: "))
        if Ht>0:
            Pago(Ht)
            break
        else:
            print("El número de horas ingresadas es inválido.")
            Aux+=1
            if Aux==3:
                print("Límite de intentos alcanzado.")


        
