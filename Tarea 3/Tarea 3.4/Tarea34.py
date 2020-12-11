#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.4

Output1=[]
print("Bienvenido al Sistema de Análsis de Caracteres.\n\n")
Input1=input("Ingrese una frase: ")
for i in "aeiou":
    for j in Input1:
        if j==i and not(i in Output1):
            Output1.append(i)
print("Las vocales que se encuentran en la frase ingresada son: ", Output1)
print("Gracias por utilizar el Sistema de Análsis de Caracteres.")


