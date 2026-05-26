
archivo = open("datos/sales_sample_2024.csv", "r")

lineas = archivo.readlines()

archivo.close()

print("Primeros 5 registros:\n")

for linea in lineas[1:6]:

    datos = linea.strip().split(",")

    id_venta = datos[0]
    fecha = datos[1]
    monto = datos[2]

    print("ID:", id_venta)
    print("Fecha:", fecha)
    print("Monto:", monto)
    print()
