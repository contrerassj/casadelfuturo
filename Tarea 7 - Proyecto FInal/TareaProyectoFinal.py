#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea Proyecto Final


Destinos={1:["Bali, Indonesia",100,1000,20],2:["Machu Picchu, Perú",150,1500,30],3:["Londres, Gran Bretaña",200,2000,40],
4:["París, Francia",250,2500,50],5:["Roma, Italia",300,3000,60,],6:["Nueva York, Estados Unidos",350,3500,70]}

def Vuelo(InputVuelo):
    
    print("Usted ha escogido",Destinos[InputVuelo][0],"como destino de su viaje.")
    Aux3=0
    while Aux3<3:
        Input3=int(input("Ingrese la cantidad de pasajes (1 a 100) que desea comprar: "))
        if Input3<1 or Input3>100:
            print("La cantidad de pasajes debe ser, como mínimo, igual a 1, o menor que 101.")
            Aux3+=1
            if Aux3==3:
                print("Límite de intentos alcanzado.")
                break
        elif Input3==1 or Input3==2:
            print("El precio del viaje para",Input3, "personas hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*Input3)
            break
        elif Input3>2 and Input3<=6:
            print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.9,
             "por cada pasaje debido a un 10% de descuento 'Paquete Familia'.")
            print("El precio final es de",Destinos[InputVuelo][1]*0.9*Input3,".")
            break
        elif Input3>6 and Input3<=30:
            print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.7,
             "por cada pasaje debido a un 30% de descuento 'Paquete Excursión'.")
            print("El precio final es de",Destinos[InputVuelo][1]*0.7*Input3,".")
            break
        else:
            print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.4,
             "por cada pasaje debido a un 60% de descuento 'Paquete Cabina'.")
            print("El precio final es de",Destinos[InputVuelo][1]*0.4*Input3,".")
            break

def VueloA(InputVA):
    print("Usted ha escogido",Destinos[InputVA][0],"como destino de su viaje.")
    Aux4=0
    while Aux4<3:
        Input4=int(input("Ingrese la cantidad de pasajes (1 a 100) que desea comprar: "))
        if Input4<1 or Input4>100:
            print("La cantidad de pasajes debe ser, como mínimo, igual a 1, o menor que 101.")
            Aux4+=1
            if Aux4==3:
                print("Límite de intentos alcanzado.")
                break
        elif Input4==1 or Input4==2:
            print("El precio del viaje para",Input4, "personas hacia",InputVA,"es de $",(Destinos[InputVA][1]+Destinos[InputVA][2])*Input4)
            break
        elif Input4>2 and Input4<=6:
            print("El precio del viaje para una sola persona hacia",InputVA,"es de $",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.9,
             "por cada viajero debido a un 10% de descuento 'Paquete Familia'.")
            print("El precio final es de",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.9*Input4,".")
            break
        elif Input4>6 and Input4<=30:
            print("El precio del viaje para una sola persona hacia",InputVA,"es de $",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.7,
             "por cada viajero debido a un 10% de descuento 'Paquete Excursión'.")
            print("El precio final es de",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.7*Input4,".")
            break
        else:
            print("El precio del viaje para una sola persona hacia",InputVA,"es de $",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.5,
             "por cada viajero debido a un 10% de descuento 'Paquete Cabina'.")
            print("El precio final es de",(Destinos[InputVA][1]+Destinos[InputVA][2])*0.5*Input4,".")
            break

def VueloR(InputVR):
    Destinos={1:["Bali, Indonesia",100,1000,20],2:["Machu Picchu, Perú",150,1500,30],3:["Londres, Gran Bretaña",200,2000,40],
    4:["París, Francia",250,2500,50],5:["Roma, Italia",300,3000,60,],6:["Nueva York, Estados Unidos",350,3500,70]}
    InputVR=int(input("""Seleccione el Destino de su Vuelo:
    -Bali, Indonesia (1)
    -Machu Picchu, Perú (2)
    -Londres, Gran Bretaña (3)
    -París, Francia (4)
    -Roma, Italia (5)
    -Nueva York, Estados Unidos (6)
    """))
    print("Usted ha escogido",Destinos[InputVR][0],"como destino de su viaje.")
    Aux5=0
    while Aux5<3:
        Input4=int(input("Ingrese la cantidad de pasajes (1 a 100) que desea comprar: "))
        if Input4<1 or Input4>100:
            print("La cantidad de pasajes debe ser, como mínimo, igual a 1, o menor que 101.")
            Aux5+=1
            if Aux5==3:
                print("Límite de intentos alcanzado.")
                break
        elif Input4==1 or Input4==2:
            print("El precio del viaje para",Input4, "personas hacia",InputVR,"es de $",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*Input4)
            break
        elif Input4>2 and Input4<=6:
            print("El precio del viaje para una sola persona hacia",InputVR,"es de $",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.9,
             "por cada viajero debido a un 10% de descuento 'Paquete Familia'.")
            print("El precio final es de",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.9*Input4,".")
            break
        elif Input4>6 and Input4<=30:
            print("El precio del viaje para una sola persona hacia",InputVR,"es de $",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.7,
             "por cada viajero debido a un 10% de descuento 'Paquete Excursión'.")
            print("El precio final es de",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.7*Input4,".")
            break
        else:
            print("El precio del viaje para una sola persona hacia",InputVR,"es de $",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.5,
             "por cada viajero debido a un 10% de descuento 'Paquete Cabina'.")
            print("El precio final es de",(Destinos[InputVR][1]+Destinos[InputVR][2]+Destinos[InputVR][3])*0.5*Input4,".")
    

print("Bienvenido al Sistema de Gestión de Paquetes Vacacionales.\n\n")
Aux1=0
Aux2=0
while Aux1<3:
    Input2=int(input("""Seleccione el Destino de su Vuelo:
    -Bali, Indonesia (1)
    -Machu Picchu, Perú (2)
    -Londres, Gran Bretaña (3)
    -París, Francia (4)
    -Roma, Italia (5)
    -Nueva York, Estados Unidos (6)
    """))
    Input1=input("""Elija el Paquete de sus Vacaciones Soñadas Mediante la Letra Entre Paréntesis, o precione 'X' para salir:
    -Vuelo (V)
    -Vuelo y Alojamiento (A)
    -Vuelo, Alojamiento y Rent Car (R)
    ------
    """
    ).upper()
    if Input1=="":
            print("El valor ingresado no puede ser nulo.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
                break
    elif Input1=="X":
        print("Gracias por utilizar el Sistema de Gestión de Paquetes Vacacionales.")
        Aux1=3
    elif Input1=="V":
        Vuelo(Input2)
        print("Gracias por elegir volar con nosotros.")
        print("¡Buen Vuelo y Felices Vacaciones!")
        break
    elif Input1=="A":
        VueloA(Input2)
        print("Gracias por elegir volar con nosotros.")
        print("¡Buen Vuelo y Felices Vacaciones!")
        break
    elif Input1=="R":
        VueloR(Input2)
        print("Gracias por elegir volar con nosotros.")
        print("¡Buen Vuelo y Felices Vacaciones!")
        break
    else:
        print("El valor ingresado no pertenece a la base de datos.")
        Aux2+=1
        if Aux2==3:
            print("Límite de intentos alcanzado.")
            break