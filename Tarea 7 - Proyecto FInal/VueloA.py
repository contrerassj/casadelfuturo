Destinos={1:["Bali, Indonesia",100,1000,20],2:["Machu Picchu, Perú",150,1500,30],3:["Londres, Gran Bretaña",200,2000,40],
4:["París, Francia",250,2500,50],5:["Roma, Italia",300,3000,60,],6:["Nueva York, Estados Unidos",350,3500,70]}
InputVueloA=int(input("""Seleccione el Destino de su Vuelo:
-Bali, Indonesia (1)
-Machu Picchu, Perú (2)
-Londres, Gran Bretaña (3)
-París, Francia (4)
-Roma, Italia (5)
-Nueva York, Estados Unidos (6)
"""))
print("Usted ha escogido",Destinos[InputVueloA][0],"como destino de su viaje.")
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
        print("El precio del viaje para",Input4, "personas hacia",InputVueloA,"es de $",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*Input4)
        break
    elif Input4>2 and Input4<=6:
        print("El precio del viaje para una sola persona hacia",InputVueloA,"es de $",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.9, "por cada viajero debido a un 10% de descuento 'Paquete Familia'.")
        print("El precio final es de",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.9*Input4,".")
        break
    elif Input4>6 and Input4<=30:
        print("El precio del viaje para una sola persona hacia",InputVueloA,"es de $",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.7, "por cada viajero debido a un 10% de descuento 'Paquete Excursión'.")
        print("El precio final es de",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.7*Input4,".")
        break
    else:
        print("El precio del viaje para una sola persona hacia",InputVueloA,"es de $",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.5, "por cada viajero debido a un 10% de descuento 'Paquete Cabina'.")
        print("El precio final es de",(Destinos[InputVueloA][1]+Destinos[InputVueloA][2])*0.5*Input4,".")
        break