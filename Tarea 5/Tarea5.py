#Casa del Futuro
#Municipalidad de Godoy Cruz
#Provincia de Mendoza
#Contreras, Simón Jesús
#Comisión 1 - Octubre
#Tarea 5

from covid import Covid

print("Sistema de Gestión de Infercados por Virus SARS-CoV-2, año 2020.\n\n")
covid=Covid(source="worldometers")
BBDDcovid=covid.list_countries()

Aux1=0
while Aux1<3:
        Input1=input("Ingrese el nombre del país de análisis: ")
        if not(Input1 in BBDDcovid):
            print("El valor ingresado no pertenece a la base de datos.")
            Aux1+=1
            if Aux1==3:
                print("Límite de intentos alcanzado.")
                break
        else:
            print("El país de análisis es",Input1,"\n")
            PaisData=covid.get_status_by_country_name(Input1)
            print("Base de datos de:",Input1)
            print("Población Total: ",PaisData["population"])
            print("Casos Totales Confirmados por Millón de Habitantes: ",PaisData["total_cases_per_million"])
            print("Casos Totales Confirmados Netos: ",(PaisData["total_cases_per_million"]*PaisData["population"]/1000000))
            print("Casos Activos: ",PaisData["active"])
            print("Casos Activos en Estado Crítico: ",PaisData["critical"])
            print("Nuevos Casos: ",PaisData["new_cases"])
            print("Fallecidos Totales: ",PaisData["deaths"])
            print("Nuevos Fallecidos: ",PaisData["new_deaths"])
            print("Recuperados: ",PaisData["recovered"])
            if int((PaisData["total_cases_per_million"]*PaisData["population"]/1000000))==(int(PaisData["new_deaths"])+int(PaisData["recovered"])+int(PaisData["active"])):
                print("El control de datos de",Input1, "es coherente.")
            else:
                print("El control de datos de",Input1, "no es coherente.")
            print("La taza de mortalidad porcentual por SARS-Cov-2 en",Input1,"es de", 
            "{:.8f}".format(PaisData["deaths"]/PaisData["population"]*100))
            print("La taza de recuperados porcentual por SARS-Cov-2 en",Input1,"es de",
             "{:.8f}".format(PaisData["recovered"]/PaisData["population"]*100))
            print("La taza porcentual de casos críticos respecto a casos activos por SARS-Cov-2 en",Input1,"es de",
             "{:.8f}".format(PaisData["critical"]/PaisData["active"]*100))
            print("La taza porcentual de contagios por SARS-Cov-2 en",Input1,"es de",
             "{:.8f}".format((PaisData["total_cases_per_million"]*PaisData["population"]/1000000)/PaisData["population"]*100))
            break

            


