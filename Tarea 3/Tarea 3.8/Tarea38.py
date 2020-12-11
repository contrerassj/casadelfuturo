#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.8

Indice=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
Output1=[]
AuxO=0
print("Bienvenido al Sistema de Encriptación de Códigos de Guerra de César.\n\n")
Input01=input("Ingrese frase a encriptar: ")
Input1=Input01.lower()

Aux1=0
while Aux1<3:
        Input2=int(input("Ingrese paso de encriptación mayor que cero: "))
        if Input2<0:
            print("El valor ingresado es inválido.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
        else:
            print("El paso de encriptación ingresado es",Input2)
            break

for i in Input1:
    if not(i in Indice):
        Output1.append(i)
    else:
        AuxI=int(Indice.index(i))+int(Input2)
        if AuxI>27:
            AuxO=AuxI%27
        else:
            AuxO=AuxI
            Output1.append(Indice[AuxO])
for j in Output1:
    print(j, end="")
