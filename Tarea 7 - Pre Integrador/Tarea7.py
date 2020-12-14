#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 7

BBDDitems={
    "1":"a",
    "2":"b",
    "3":"c",
    "4":["d1","d2"],
    "5":["e1","e2",["e31","e32","e33","e34","e35","e36"]]
    }

def Leer():
    Input1=input("Introduzca la clave del elemento a leer (1 a " + str(len(BBDDitems)) + "): ")
    print(BBDDitems[Input1])
    if len(BBDDitems[Input1])>1:
        Input2=input("Introduzca el índice del subelemento a leer (0 a " + str(len(BBDDitems[Input1])-1)+"): ")
        print(BBDDitems[Input1][int(Input2)])
        if int(len(BBDDitems[Input1][int(Input2)]))>1:
            Input3=input("Introduzca el índice del subelemento a leer (0 a " + str(len(BBDDitems[Input1][int(Input2)])-1) + "): ")
            print(BBDDitems[Input1][int(Input2)][int(Input3)])

def Agregar():
    Input4=input("Introduzca la clave del nuevo elemento del diccionario: ")
    BBDDitems[Input4]=input("Introduzca el valor del nuevo elemento del diccionario: ")
    print("El valor para la clave", Input4, "en el diccionario BBDDitems es", (BBDDitems[Input4]))

def Reemplazar():
    Input5=input("Introduzca la clave del elemento del diccionario a reemplazar: ")
    BBDDitems[Input5]=input("Introduzca el nuevo valor del elemento reemplazado: ")
    print("El nuevo valor para la clave", Input5, "en el diccionario BBDDitems es", (BBDDitems[Input5]))

def Eliminar():
    Input6=input("Introduzca la clave del elemento del diccionario a eliminar: ")
    del BBDDitems[Input6]

Leer()
Agregar()
Reemplazar()
Eliminar()