#Construir programa que permita identificar las empresas que han tenido ventas inferiores
# a $100.000.000, entre $100.000.001 y $200.000.000 y más de $200.000.000, a lo cual
# usted deberá crear un archivo llamado “segmentacionEmpresas.json” que permita hacer
# llamada clasificacionEmpresa donde se indique “Pequeño Contribuyente”, “Mediano
# Contribuyente” y “Gran Contribuyente”.
# Datos de archivo de archivo “listadoRutEmpresa.csv”
# rut,nombre,ventas
# 72642413-6,Comercial Calcetas Runner,150000000
# 76437473-2,Reparación Mac,300000000
# 76254356-9,ProgramaSoftware,27500000
# 76077262-3,Calzados Roma,15000000
# 76310800-8,Empresa Arcos,80000000
# 76283690-4,Casino Coffe,120000000
# 76952985-5,Cafe Express ltda,50000000
# 76081440-2,Vino Export SA,20000000
# 76216579-1,Cepa Merl LTDA,30000000
# 76597875-0,Comercial Ropa America,60000000
# 76852106-3,Empresas JP,90000000
# 76887745-8,Empresas ICata SA,100000000
# 76210124-2,Buses Peñalolen,150000000
# 76802052-4,Sandias Paine LTDA,70000000
# 76575973-1,Modas Junior P,400000000
# 76869384-2,Bar del 81,25000000
# 76877803-6,Empresas LLS,8000000
# 76706124-0,Empresas luz y vida SA,3000000
#76162938-1,Empresa Matrix,120000000
granContribuyente = 0
medianoContribuyente = 0
pequeñoContribuyente = 0
import csv
with open("listadoRutEmpresa.csv", "w", newline="") as listadoRutEmpresa_csv:
    escritor_csv = csv.writer(listadoRutEmpresa_csv)
    escritor_csv.writerow(["rut","nombre","ventas"])
    escritor_csv.writerows([
    [72642413-6,"Comercial Calcetas Runner",150000000],
    [76437473-2,"Reparación Mac",300000000],
    [76254356-9,"ProgramaSoftware",27500000],
    [76077262-3,"Calzados Roma",15000000],
    [76310800-8,"Empresa Arcos",80000000],
    [76283690-4,"Casino Coffe",120000000],
    [76952985-5,"Cafe Express ltda",50000000],
    [76081440-2,"Vino Export SA",20000000],
    [76216579-1,"Cepa Merl LTDA",30000000],
    [76597875-0,"Comercial Ropa America",60000000],
    [76852106-3,"Empresas JP",90000000],
    [76887745-8,"Empresas ICata SA",100000000],
    [76210124-2,"Buses Peñalolen",150000000],
    [76802052-4,"Sandias Paine LTDA",70000000],
    [76575973-1,"Modas Junior P",400000000],
    [76869384-2,"Bar del 81",25000000],
    [76877803-6,"Empresas LLS",8000000],
    [76706124-0,"Empresas luz y vida SA",3000000],
    [76162938-1,"Empresa Matrix",120000000]
    ])
    
with open("listadoRutEmpresa.csv", "r",newline="") as listadoRutEmpresa_csv:
    lector_csv = csv.reader(listadoRutEmpresa_csv)
    for fila in lector_csv:
        rut,nombre, ventas = fila
        print(ventas)
        if str(ventas) < 100000000:
            pequeñoContribuyente += 1
        elif str(ventas) > 100000000 and str(ventas) < 200000000:
            medianoContribuyente += 1
        else:
            granContribuyente +=1
print (pequeñoContribuyente, medianoContribuyente, granContribuyente)            