from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()


#################################### Endpoint 1: cantidad_filmaciones_mes ###########################################

#Traemos los datos de peliculas por mes
df_cant_pelis_x_mes = pd.read_parquet('Datasets/cant_pelis_x_mes.parquet')

def cantidad_filmaciones_mes(mes):
    # Diccionario para traducir los meses al español
    meses_espanol = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8, 
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Obtenemos el número de mes en base al nombre en español
    numero_mes = meses_espanol.get(mes.lower())
    if not numero_mes:
        return f"Mes '{mes}' no válido. Por favor, ingrese un mes válido en español."

    # Filtramos el DataFrame por el mes especificado y sumar las películas
    total_peliculas = df_cant_pelis_x_mes[df_cant_pelis_x_mes['release_month'] == numero_mes]['movie_count'].sum()
    
    return f"Un total de {total_peliculas} peliculas fueron estrenadas en {mes.lower()}"

# Definimos el endpoint
@app.get("/cantidad-filmaciones-mes")
def get_cantidad_filmaciones_mes(mes: str):
    resultado = cantidad_filmaciones_mes(mes)
    return {"resultado": resultado}


#################################### Endpoint 2: cantidad_filmaciones_dia ##########################################

#Traemos los datos de peliculas por dia
df_cant_pelis_x_dia = pd.read_parquet('Datasets/cant_pelis_x_dia.parquet')

def cantidad_filmaciones_dia(dia):

    # Diccionario para traducir los días de la semana al español
    dias_espanol_a_ingles = {
        'lunes': 'Monday', 'martes': 'Tuesday', 'miércoles': 'Wednesday', 
        'jueves': 'Thursday', 'viernes': 'Friday', 'sábado': 'Saturday', 'domingo': 'Sunday'
    }

    # Traducimos el día del español al inglés
    dia_ingles = dias_espanol_a_ingles.get(dia.lower())
    if dia_ingles is None:
        return f"Día '{dia}' no válido. Por favor, ingrese un día válido en español."
    
    # Filtramos el DataFrame por el día de la semana especificado y sumar las películas
    total_peliculas = df_cant_pelis_x_dia[df_cant_pelis_x_dia['release_day'] == dia_ingles]['movie_count'].sum()
    
    return f"Un total de {total_peliculas} películas fueron estrenadas en los días {dia.lower()}."

# Definimos el endpoint
@app.get("/cantidad_filmaciones_dia")
def get_cantidad_filmaciones_dia(dia: str):
    resultado = cantidad_filmaciones_dia(dia)
    return {"resultado": resultado}


#################################### Endpoint 3: score_titulo ##########################################

#Traemos los datos ampliados de peliculas
df_peliculas_datos = pd.read_parquet('Datasets/peliculas_datos.parquet')

def score_titulo(titulo):
    # Buscamos la fila donde el título coincide
    filmacion = df_peliculas_datos[df_peliculas_datos['title'].str.lower() == titulo.lower()]
    
    if filmacion.empty:
        return f"La película '{titulo}' no se encuentra en el dataset."
    
    # Obtenemos el título, año de estreno y score
    titulo = filmacion['title'].values[0]
    anho_estreno = filmacion['release_year'].values[0]
    score = filmacion['popularity'].values[0]
    
    return f"La película '{titulo}' fue estrenada en el año {anho_estreno} con un score/popularidad de {score:.2f}."

# Definimos el endpoint
@app.get("/score_titulo")
def get_score_titulo(titulo: str):
    resultado = score_titulo(titulo)
    return {"resultado": resultado}


#################################### Endpoint 4: votos_titulo ##########################################


def votos_titulo(titulo):
    # Buscamos la fila donde el título coincide
    filmacion = df_peliculas_datos[df_peliculas_datos['title'].str.lower() == titulo.lower()]
    
    if filmacion.empty:
        return f"La película '{titulo}' no se encuentra en el dataset."
    
    # Obtenemos los datos de votación
    titulo = filmacion['title'].values[0]
    anho_estreno = filmacion['release_year'].values[0]
    total_votos = filmacion['vote_count'].values[0]
    promedio_votos = filmacion['vote_average'].values[0]
    
    # Comprobamos si tiene al menos 2000 valoraciones
    if total_votos < 2000:
        return f"La película '{titulo}' no cumple con la cantidad mínima de 2000 valoraciones."
    
    return (f"La película '{titulo}' fue estrenada en el año {anho_estreno}. "
            f"La misma cuenta con un total de {total_votos} valoraciones, "
            f"con un promedio de votos de {promedio_votos:.1f}.")

# Definimos el endpoint
@app.get("/votos_titulo")
def get_votos_titulo(titulo: str):
    resultado = votos_titulo(titulo)
    return {"resultado": resultado}


#################################### Endpoint 5: get_actor ##########################################

#Traemos los datos de actores
df_actores = pd.read_parquet('Datasets/actores.parquet')

def consultar_actor(nombre_actor):
    # Filtramos el DataFrame de actores para obtener las películas en las que participó el actor
    registro_actor = df_actores[df_actores['actor_name'].str.lower() == nombre_actor.lower()]
    
    if registro_actor.empty:
        return f"El actor '{nombre_actor}' no se encuentra en el dataset de actores."
    
    # Obtenemos los movie_id de las películas en las que participó el actor
    peliculas_actor_ids = registro_actor['movie_id'].unique()
    
    # Filtramos las películas del dataset de películas usando los movie_id del actor
    peliculas_participacion = df_peliculas_datos[df_peliculas_datos['movie_id'].isin(peliculas_actor_ids)]
    
    # Calculamos la cantidad de películas y el retorno total y promedio
    cantidad_peliculas = len(peliculas_participacion)
    retorno_total = peliculas_participacion['return'].sum()
    retorno_promedio = peliculas_participacion['return'].mean() if cantidad_peliculas > 0 else 0
    
    return (f"El actor '{nombre_actor}' ha participado en {cantidad_peliculas} filmaciones,"
            f"el mismo ha conseguido un retorno de {retorno_total:.2f}% con un promedio de {retorno_promedio:.2f}% por filmación.")


# Definimos el endpoint
@app.get("/get_actor")
def get_actor(actor: str):
    resultado = consultar_actor(actor)
    return {"resultado": resultado}


#################################### Endpoint 6: get_director ##########################################

#Traemos los datos de directores
df_directores = pd.read_parquet('Datasets/directores.parquet')

def consultar_director(nombre_director):
    # Filtramos el DataFrame de directores para obtener las películas que dirigió el director
    registro_director = df_directores[df_directores['crew_name'].str.lower() == nombre_director.lower()]
    
    if registro_director.empty:
        return f"El director '{nombre_director}' no se encuentra en el dataset de directores."
    
    # Obtenemos los movie_id de las películas dirigidas por el director
    peliculas_director_ids = registro_director['movie_id'].unique()
    
    # Filtramos las películas en el dataset de películas usando los movie_id del director
    peliculas_dirigidas = df_peliculas_datos[df_peliculas_datos['movie_id'].isin(peliculas_director_ids)]
    
    # Calculamos el retorno total y crear la lista de detalles de cada película
    retorno_total = peliculas_dirigidas['return'].sum()
    detalles_peliculas = []
    
    for _, row in peliculas_dirigidas.iterrows():
        ganancia = row['revenue'] - row['budget']
        detalles_peliculas.append({
            'title': row['title'],
            'release_date': row['release_date'],
            'return': row['return'],
            'budget': row['budget'],
            'ganancia': ganancia
        })
    
    # Formateamos de salida
    salida_detalles = "\n".join(
        [f"- {det['title']} (Lanzamiento: {det['release_date']}, Retorno: {det['return']:.2f}, "
         f"Presupuesto: {det['budget']}, Ganancia: {det['ganancia']})"
         for det in detalles_peliculas]
    )
    
    return (f"El director '{nombre_director}' ha conseguido un retorno total de {retorno_total:.2f} en las películas que dirigió. "
            f"Detalles de cada película dirigida:\n{salida_detalles}")

# Definimos el endpoint
@app.get("/get_director")
def get_director(director: str):
    resultado = consultar_director(director)
    return {"resultado": resultado}

#################################### Endpoint 7: Sistema de Recomendacion ##########################################

#Traemos los datos de popularidad normalizada
df_popularidad = pd.read_parquet('Datasets/matriz_normalizada_popularity.parquet')

matriz_similaridad_popularidad = cosine_similarity(df_popularidad)

def define_recomendaciones(titulo):
    
    # Verificar si el título existe en el dataset
    if titulo not in df_peliculas_datos['title'].values:
        return f"La película '{titulo}' no se encuentra en el dataset."

    # Encontrar el índice de la película en el dataset
    movie_index = df_peliculas_datos[df_peliculas_datos['title'] == titulo].index[0]
    
    # Obtener los puntajes de similitud para esa película específica
    similarity_scores = list(enumerate(df_peliculas_datos[movie_index]))
    
    # Ordenar las películas por similitud en orden descendente
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Seleccionar los índices de las películas más similares (excluyendo la misma película)
    top_movies_indices = [i[0] for i in similarity_scores[1:6]]
    
    # Filtrar y ordenar las películas similares por popularidad
    top_movies = df_peliculas_datos.iloc[top_movies_indices]
    top_movies = top_movies.sort_values(by='popularity', ascending=False)
    
    # Obtener los títulos de las películas recomendadas
    recommended_titles = top_movies['title'].tolist()
    
    return recommended_titles

# Definimos el endpoint
@app.get("/recomendacion")
def recomendacion(titulo: str):
    resultado = define_recomendaciones(titulo)
    return {"resultado": resultado}