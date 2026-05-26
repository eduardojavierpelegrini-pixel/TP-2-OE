
archivo = open("datos/sales_sample_2024.csv", "r")

lineas = archivo.readlines()

archivo.close()


total_ventas = 0
cantidad_ventas = 0
venta_maxima = 0
venta_minima = float("inf")


for linea in lineas[1:]:

    datos = linea.strip().split(",")

    monto = int(datos[2])

    total_ventas = total_ventas + monto

    cantidad_ventas = cantidad_ventas + 1


    if monto > venta_maxima:
        venta_maxima = monto


    if monto < venta_minima:
        venta_minima = monto


promedio_ventas = total_ventas / cantidad_ventas


print("ANÁLISIS DE VENTAS")
print("-------------------")

print("Total de ventas:", total_ventas)

print("Cantidad de ventas:", cantidad_ventas)

print("Promedio de ventas:", round(promedio_ventas, 2))

print("Venta máxima:", venta_maxima)

print("Venta mínima:", venta_minima)
