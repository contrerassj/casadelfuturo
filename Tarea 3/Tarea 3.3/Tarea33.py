#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 3.3

# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# Casa del Futuro
# Municipalidad de Godoy Cruz
# Provincia de Mendoza
# Contreras, Sim�n Jes�s
# Comisi�n 1 - Octubre
# Tarea 3.3
if __name__ == '__main__':
	recorrido = int()
	importe = int()
	print("Bienvenido al Sistema de Cobro por Alquiler de Veh�culo")
	print("Ingrese el valor del recorrido realizado [Km]")
	recorrido = int(input())
	if recorrido>1000:
		importe = 800000+recorrido*10000
	else:
		if recorrido>300:
			importe = recorrido*15000-4200000
		else:
			importe = 300000
	print("El Importe total por el recorrido realizado es de ",importe)
