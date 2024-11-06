Proyecto Individual: Plataforma de Streaming de Películas

-Intro- 

Este proyecto fue realizado con el propósito de demostrar las capacidades adquiridas en cuanto a manejo de datasets, python, ETL y machine learning entre otros.

-Descripcion básica del Proyecto- 

A partir de dos datasets crudos de una plataforma de streaming de películas, movies y credits, se ha desarrollado una API en la web para consumo de estos datos, con 7 endpoints implementados, 6 de los cuales son funciones simples de consulta de datos agrupados y un endpoint principal que implementa un sistema de recomendación de películas desarrollado en base al modelo de similaridad del coseno.

-Descripción del proceso y archivos del proyecto-

. Preprocesamiento de Datos (ETL): Incluye la carga y desanidación de los datos crudos, tratamiento preliminar de la base de datos: depuración de columnas, formateo, creacion de columna "return", imputacion de valores nulos de revenue y budget.

ARCHIVOS: . MS_Transformaciones.ipynb (al final de esta notebook se exportan los archivos desanidados de movie y credits, sin embargo estos no se encuentran en el repositorio por cuestión de limitación de espacio)

. EDA y desarrollo de sistema de recomendación: incluye la verificación de tipos de datos, porcentaje de nulos, eliminación de datos duplicados, graficas estadisticos para distribucion de valores y analisis de relaciones entre las variables versus el dato de popularidad de la pelicula (dato principal en el que se basa el sistema de recomendación). En este paso la base se recortó de manera significativa atendiendo los requerimientos de las funciones a desarrollar y la limitacion de espacio, con los criterios de decisión explicados. Tambien en este paso se encuentran las pruebas realizadas para el sistema de recomendación, la creación de los datasets resumidos que seran consumidas por la API.

ARCHIVOS: . EDA y Sistema de recomendacion.ipynb . cant_pelis_x_dia.parquet . cant_pelis_x_mes.parquet . peliculas_datos.parquet . actores.parquet . directores.parquet . matriz_normalizada_popularity.parquet

. Puesta en Marcha de la API con FastApi: se prueban las funciones desde el dataset resumido y luego se llevan los mismos al archivo main junto con el punto de acceso local para pruebas de los diferentes endpointss.

ARCHIVOS: . MS_funciones.ipynb . main.py

. Deploy en Render: Creacion de cuenta en Render y deploy del repositorio

ARCHIVOS: . requirements.txt

Link a la API desarrollada: https://moviestreaming-xxc4.onrender.com/docs
