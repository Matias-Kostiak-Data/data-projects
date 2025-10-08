import pandas as pd
from sqlalchemy import create_engine
import os

# ✅ Connect to PostgreSQL / Conectar con PostgreSQL
engine = create_engine("postgresql+psycopg2://mati_user:prueba123@localhost:5432/movielens_db")
print("✅ Connection established with PostgreSQL / Conexión establecida con PostgreSQL")

# 📁 Create output directory if it doesn't exist / Crear carpeta de salida si no existe
os.makedirs("../outputs", exist_ok=True)

# ---------------------------------------------------------------
# 🧩 QUERY 1 — Top 10 highest-rated movies (more than 100 ratings)
# ---------------------------------------------------------------
# Consulta 1 — Top 10 películas mejor calificadas (más de 100 calificaciones)
query_top_movies = """
SELECT
    m.title,
    ROUND(AVG(r.rating)::numeric, 2) AS avg_rating,
    COUNT(r.rating) AS total_ratings
FROM ratings r
JOIN movies m ON m.movieid = r.movieid
GROUP BY m.title
HAVING COUNT(r.rating) > 100
ORDER BY avg_rating DESC
LIMIT 10;
"""

top_movies = pd.read_sql(query_top_movies, engine)
top_movies.to_csv("../outputs/top_movies.csv", index=False)
print("🎬 Top 10 movies saved to outputs/top_movies.csv / Guardado correctamente.\n")

# ----------------------------------------------------------------
# 🧩 QUERY 2 — Average rating by genre (filtering low-frequency)
# ----------------------------------------------------------------
# Consulta 2 — Promedio de calificaciones por género (filtrando géneros poco frecuentes)
query_genre_avg = """
SELECT
    UNNEST(STRING_TO_ARRAY(m.genres, '|')) AS genre,
    ROUND(AVG(r.rating)::numeric, 2) AS avg_rating,
    COUNT(r.rating) AS total_ratings
FROM ratings r
JOIN movies m ON m.movieid = r.movieid
GROUP BY genre
HAVING COUNT(r.rating) > 500
ORDER BY avg_rating DESC;
"""

genre_avg = pd.read_sql(query_genre_avg, engine)
genre_avg.to_csv("../outputs/genre_avg.csv", index=False)
print("🎭 Genre averages saved to outputs/genre_avg.csv / Promedios por género guardados.\n")

# -------------------------------------------------------------------
# 🧩 QUERY 3 — Most rated genres (popularity-based)
# -------------------------------------------------------------------
# Consulta 3 — Géneros más calificados (por cantidad de ratings)
query_genre_popularity = """
SELECT
    UNNEST(STRING_TO_ARRAY(m.genres, '|')) AS genre,
    COUNT(r.rating) AS total_ratings,
    ROUND(AVG(r.rating)::numeric, 2) AS avg_rating
FROM ratings r
JOIN movies m ON m.movieid = r.movieid
GROUP BY genre
ORDER BY total_ratings DESC
LIMIT 10;
"""

genre_popularity = pd.read_sql(query_genre_popularity, engine)
genre_popularity.to_csv("../outputs/genre_popularity.csv", index=False)
print("📊 Most rated genres saved / Géneros más calificados guardados.\n")

# -------------------------------------------------------------------
# 🧩 QUERY 4 — Advanced CTE: Movies with above-average ratings
# -------------------------------------------------------------------
# Consulta 4 — CTE avanzada: Películas con ratings por encima del promedio global
query_above_avg = """
WITH avg_all AS (
    SELECT AVG(rating) AS global_avg FROM ratings
)
SELECT
    m.title,
    ROUND(AVG(r.rating)::numeric, 2) AS movie_avg,
    COUNT(r.rating) AS total_ratings
FROM ratings r
JOIN movies m ON m.movieid = r.movieid
CROSS JOIN avg_all
GROUP BY m.title, avg_all.global_avg
HAVING AVG(r.rating) > avg_all.global_avg
ORDER BY movie_avg DESC
LIMIT 15;
"""

above_avg = pd.read_sql(query_above_avg, engine)
above_avg.to_csv("../outputs/movies_above_avg.csv", index=False)
print("🏆 Movies above global average saved / Películas sobre el promedio global guardadas.\n")

# -------------------------------------------------------------------
# 🧩 QUERY 5 — Window function: Ranking movies within each genre
# -------------------------------------------------------------------
# Consulta 5 — Función ventana: Ranking de películas dentro de cada género
query_genre_ranking = """
WITH expanded AS (
    SELECT
        m.movieid,
        m.title,
        UNNEST(STRING_TO_ARRAY(m.genres, '|')) AS genre,
        AVG(r.rating) AS avg_rating,
        COUNT(r.rating) AS total_ratings
    FROM ratings r
    JOIN movies m ON m.movieid = r.movieid
    GROUP BY m.movieid, m.title, m.genres
)
SELECT
    genre,
    title,
    ROUND(avg_rating::numeric, 2) AS avg_rating,
    total_ratings,
    RANK() OVER (PARTITION BY genre ORDER BY avg_rating DESC, total_ratings DESC) AS rank_in_genre
FROM expanded
WHERE total_ratings > 100
ORDER BY genre, rank_in_genre
LIMIT 50;
"""

genre_ranking = pd.read_sql(query_genre_ranking, engine)
genre_ranking.to_csv("../outputs/genre_ranking.csv", index=False)
print("🥇 Genre ranking saved / Ranking por género guardado.\n")

# ✅ Close connection / Cerrar conexión
engine.dispose()
print("🔒 Connection closed / Conexión cerrada")
