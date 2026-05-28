
#TP 2-Organizacion empresarial
##Análisis de ventas de una pequeña empresa

###Tecnicatura Universitaria en Programación a Distancia-UTN


----
##Integrantes
.Lucas Barragan
.Eduardo Pelegrini

----

##Descripición del proyecto

Este proyecto fue realizado para el Trabajo Práctico N°2 de la materia
Organizacion Empresarial.

El objetivo principal fue aplicar herramientas de trabajo
colaborativo utilizando Git, GitHub, Jira y Google Colab, ademas de desarrollar 
un script en Python capaz de analizar un conjunto de datos de ventas 
almacenados en un archivo CSV

Para el desarrollo se eligió el escenario de análisis de ventas
propuesto en la consigna del trabajo práctico.

---

##Funcionalidades implementadas

El programa desarrollado permite:

.Leer información desde un archivo CSV
.Procesar los datos de ventas
.Calcular:
  -Total de ventas
  -Cantidad de ventas registradas
  -Promedio de ventas
  -Venta máxima
  -Venta mínima
.Generar automáticamente un reporte de resultados en formato .txt

---

##Organización del Proyecto

El proyecto se encuentra organizado en distitntas carpetas
para separar correctamente los datos, el código y los resultados generados

.datos/
Contiene el archivo CSV utilizando por el análisis de ventas
.Scripts/
Contiene el script principal desarrollado en Python (analisis_ventas.py).

.resultados/
Carpeta donde se generan automáticamente los reportes del análisis al ejecutar
el programa

.README.md
Archivo utilizado para evitar subir archivos innecesarios al repositorio

---

##Tecnologias Utilizadas

Durante el desarrollo del proyecto se utilizaron las siguientes
herramientas:

.Python
.Google Colab
.Git
.GitHub
.Jira

---

##Cómo ejecutar el proyecto en Google Colab
  1.Clonar el repositorio
python
!git clone https://github.com/eduardojavierpelegrini-pixel/TP-2-OE.git
  2.Ingresar a la carpeta del proyecto
python
%cd TP-2-OE
  3. Ejecutar el script principal:
python
!python scripts/analisis_ventas.py

---

##Resultados

Al ejecutar el programa se genera automaticamente el archivo:

txt
resultados/reporte_ventas.txt

Este archivo contiene el resumen completo del análisis realizado
realizado sobre el dataset de ventas
