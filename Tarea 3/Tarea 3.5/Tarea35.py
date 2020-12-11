#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.5

Aux=0
print("Bienvenido al Sistema de Análsis de Caracteres 2.0.\n\n")
Input1=input("Ingrese una frase: ")
for i in "aeiou":
    for j in Input1:
        if j==i:
            Aux+=1
print("Se encontraron ", Aux,"vocales en la frase analizada.")