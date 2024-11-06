HENRY - PROYECTO INDIVIDUAL: Plataforma de Streaming de Películas

-Intro- Este proyecto fue realizado con el propósito de demostrar las capacidades adquiridas en cuanto a manejo de datasets, python, ETL y machine learning entre otros.

-Descripcion básica del Proyecto- A partir de dos datasets crudos de una plataforma de streaming de películas, movies y credits, se ha desarrollado una API en la web para consumo de estos datos, con 7 endpoints implementados, 6 de los cuales son funciones simples de consulta de datos agrupados y un endpoint principal que implementa un sistema de recomendación de películas desarrollado en base al modelo de similaridad del coseno.

-Descripción del proceso y archivos del proyecto-

. Preprocesamiento de Datos (ETL): Incluye la carga y desanidación de los datos crudos, tratamiento preliminar de la base de datos: depuración de columnas, formateo, creacion de columna "return", imputacion de valores nulos de revenue y budget.

ARCHIVOS: . MS_Transformaciones.ipynb (al final de esta notebook se exportan los archivos desanidados de movie y credits, sin embargo estos no se encuentran en el repositorio por cuestión de limitación de espacio)

. EDA y desarrollo de sistema de recomendación: incluye la verificación de tipos de datos, porcentaje de nulos, eliminación de datos duplicados, graficas estadisticos para distribucion de valores y analisis de relaciones entre las variables versus el dato de popularidad de la pelicula (dato principal en el que se basa el sistema de recomendación). En este paso la base se recortó de manera significativa atendiendo los requerimientos de las funciones a desarrollar y la limitacion de espacio, con los criterios de decisión explicados. Tambien en este paso se encuentran las pruebas realizadas para el sistema de recomendación, las funciones y la creación de los datasets resumidos que seran consumidas por la API.

ARCHIVOS: . EDA y Sistema de recomendacion.ipynb . MS_funciones.ipynb . cant_pelis_x_dia.parquet . cant_pelis_x_mes.parquet . peliculas_datos.parquet . actores.parquet . directores.parquet . matriz_normalizada_popularity.parquet

. Modelado de Datos: creacion de la columna "sentiment_analysis" en el dataset "user_reviews" a través de NLP (librería TextBlob), manejo de datos faltantes. Creación de datasets auxiliares.

ARCHIVOS: . Sentiment Analysis.ipynb . datasets_auxiliares.ipynb . max_playtime_per_genre.parquet . user_total_playtime_general.parquet . top_3_games_per_year.parquet . bottom_3_games_per_year.parquet . sentiment_counts_sorted.parquet

. Generacion de modelo de machine learning: Se crea el modelo de aprendizaje a través de la similitud del coseno.

ARCHIVOS: . Modelo Item-item.ipynb . cosine_sim_df.parquet

. Puesta en Marcha de la API: se genera el archivo main junto con el punto de acceso local para pruebas de los diferentes endpoints o funciones.

ARCHIVOS: . Funciones.ipynb . main.py

. Deploy en Render: Creacion de cuenta en Render y deploy del repositorio

ARCHIVOS: . requirements.txt

-PRUEBAS REALIZADAS EN ENTORNO VIRTUAL-

Valores presentes en los datasets https://machinelearning-steam.onrender.com/PlayTimeGenre/Action https://machinelearning-steam.onrender.com/PlayTimeGenre/Adventure https://machinelearning-steam.onrender.com/PlayTimeGenre/Web%20Publishing

https://machinelearning-steam.onrender.com/UserForGenre/Indie https://machinelearning-steam.onrender.com/UserForGenre/Simulation https://machinelearning-steam.onrender.com/UserForGenre/Strategy

https://machinelearning-steam.onrender.com/UsersRecommend/2000 https://machinelearning-steam.onrender.com/UsersRecommend/2010 https://machinelearning-steam.onrender.com/UsersRecommend/2011

https://machinelearning-steam.onrender.com/UsersNotRecommend/2017 https://machinelearning-steam.onrender.com/UsersNotRecommend/2015 https://machinelearning-steam.onrender.com/UsersNotRecommend/2012

https://machinelearning-steam.onrender.com/sentiment_analysis/2002 https://machinelearning-steam.onrender.com/sentiment_analysis/2010 https://machinelearning-steam.onrender.com/sentiment_analysis/2008

https://machinelearning-steam.onrender.com/recomendacion_juego/Counter-Strike:%20Global%20Offensive https://machinelearning-steam.onrender.com/recomendacion_juego/Garry's%20Mod https://machinelearning-steam.onrender.com/recomendacion_juego/Lead%20and%20Gold:%20Gangs%20of%20the%20Wild%20West

Valores Ausentes en los datasets https://machinelearning-steam.onrender.com/PlayTimeGenre/Actin https://machinelearning-steam.onrender.com/PlayTimeGenre/Adenture https://machinelearning-steam.onrender.com/PlayTimeGenre/Wb%20Publishing

https://machinelearning-steam.onrender.com/UserForGenre/Idie https://machinelearning-steam.onrender.com/UserForGenre/Simulatio https://machinelearning-steam.onrender.com/UserForGenre/Strateg

https://machinelearning-steam.onrender.com/UsersRecommend/20010 https://machinelearning-steam.onrender.com/UsersRecommend/20102 https://machinelearning-steam.onrender.com/UsersRecommend/20112

https://machinelearning-steam.onrender.com/UsersNotRecommend/20117 https://machinelearning-steam.onrender.com/UsersNotRecommend/20115 https://machinelearning-steam.onrender.com/UsersNotRecommend/20142

https://machinelearning-steam.onrender.com/sentiment_analysis/20022 https://machinelearning-steam.onrender.com/sentiment_analysis/20102 https://machinelearning-steam.onrender.com/sentiment_analysis/20083

https://machinelearning-steam.onrender.com/recomendacion_juego/Ironbound https://machinelearning-steam.onrender.com/recomendacion_juego/Real%20Pool%203D%20-%20Poolians https://machinelearning-steam.onrender.com/recomendacion_juego/Log%20Challenge
