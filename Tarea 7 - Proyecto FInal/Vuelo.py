
Destinos={1:["Bali, Indonesia",100],2:["Machu Picchu, Perú",150],3:["Londres, Gran Bretaña",200],
4:["París, Francia",250],5:["Roma, Italia",300],6:["Nueva York, Estados Unidos",350]}
InputVuelo=int(input("""Seleccione el Destino de su Vuelo:
-Bali, Indonesia (1)
-Machu Picchu, Perú (2)
-Londres, Gran Bretaña (3)
-París, Francia (4)
-Roma, Italia (5)
-Nueva York, Estados Unidos (6)
"""))
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
        print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.9, "por cada pasaje debido a un 10% de descuento 'Paquete Familia'.")
        print("El precio final es de",Destinos[InputVuelo][1]*0.9*Input3,".")
        break
    elif Input3>6 and Input3<=30:
        print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.7, "por cada pasaje debido a un 30% de descuento 'Paquete Excursión'.")
        print("El precio final es de",Destinos[InputVuelo][1]*0.7*Input3,".")
        break
    else:
        print("El precio del viaje para una sola persona hacia",InputVuelo,"es de $",Destinos[InputVuelo][1]*0.4, "por cada pasaje debido a un 60% de descuento 'Paquete Cabina'.")
        print("El precio final es de",Destinos[InputVuelo][1]*0.4*Input3,".")
        break