HENRY - PROYECTO INDIVIDUAL: Plataforma de Streaming de Películas

-Intro- Este proyecto fue realizado con el propósito de demostrar las capacidades adquiridas en cuanto a manejo de datasets, python, ETL y machine learning entre otros.

-Descripcion básica del Proyecto- A partir de 2 datasets crudos de una plataforma de streaming de películas, movies y credits, se ha implementado una API en la web para consultas   5 de las 6 consultas requieren manejo básico de bases de datos y 1 requiere entrenar un modelo de machine learning para armar un sistema de recomendación de juegos.

-Pasos Dados para la concrecion del Proyecto y Descripción de Archivos Relevantes-

. Preprocesamiento de Datos (ETL): Incluye la extraccion y descompresion de los archivos base desde el drive del proyecto, tratamiento preliminar de la base de datos, extraccion de datos anidados, tratamiento de datos duplicados y nulos, estandarizacion de tipos de datos en columnas.

ARCHIVOS: . Preprocesamiento steam_games.ipynb . Preprocesamiento user_reviews.ipynb . Preprocesamiento users_items.ipynb . steam_games.parquet . user_reviews.parquet . users_items.parquet

. Analisis exploratorio de Datos: investigacion de relaciones entre las variables de los datasets, verificacion de outliers o anomalías.Generacion de un nuevo diccionario de datos que nos permita entender mejor la utilidad y relación de todos los datos.

ARCHIVOS: . EDA steam_games.ipynb . EDA user_reviews.ipynb . EDA users_items.ipynb . Diccionario de Datos.txt

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
