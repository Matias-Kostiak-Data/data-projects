import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Create folder for visuals / Crear carpeta de visualizaciones
os.makedirs("../visuals", exist_ok=True)

# 🎨 Set a professional style / Estilo profesional
sns.set(style="whitegrid", palette="coolwarm", font_scale=1.1)

# --------------------------------------------------------------
# 1️⃣ TOP 10 MOVIES
# --------------------------------------------------------------
# Cargar datos de películas mejor calificadas
top_movies = pd.read_csv("../outputs/top_movies.csv")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_movies,
    y="title",
    x="avg_rating",
    hue="total_ratings",
    dodge=False
)
plt.title("Top 10 Highest-Rated Movies (100+ Ratings)\nTop 10 Películas Mejor Calificadas")
plt.xlabel("Average Rating / Promedio de Calificación")
plt.ylabel("Movie Title / Título de la Película")
plt.legend(title="Total Ratings / Total Calificaciones")
plt.tight_layout()
plt.savefig("../visuals/top_movies.png")
plt.close()
print("🎬 Saved: visuals/top_movies.png")

# --------------------------------------------------------------
# 2️⃣ AVERAGE RATING BY GENRE
# --------------------------------------------------------------
# Promedio de calificaciones por género
genre_avg = pd.read_csv("../outputs/genre_avg.csv")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=genre_avg.sort_values("avg_rating", ascending=False),
    x="avg_rating",
    y="genre",
    color="#4c72b0"
)
plt.title("Average Rating by Genre / Promedio por Género")
plt.xlabel("Average Rating / Promedio")
plt.ylabel("Genre / Género")
plt.tight_layout()
plt.savefig("../visuals/genre_avg.png")
plt.close()
print("🎭 Saved: visuals/genre_avg.png")

# --------------------------------------------------------------
# 3️⃣ GENRE POPULARITY (MOST RATED)
# --------------------------------------------------------------
# Popularidad de géneros por cantidad de ratings
genre_popularity = pd.read_csv("../outputs/genre_popularity.csv")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=genre_popularity,
    x="total_ratings",
    y="genre",
    color="#55a868"
)
plt.title("Most Rated Genres / Géneros con Más Calificaciones")
plt.xlabel("Total Ratings / Total de Calificaciones")
plt.ylabel("Genre / Género")
plt.tight_layout()
plt.savefig("../visuals/genre_popularity.png")
plt.close()
print("📊 Saved: visuals/genre_popularity.png")

# --------------------------------------------------------------
# 4️⃣ MOVIES ABOVE GLOBAL AVERAGE
# --------------------------------------------------------------
# Películas con ratings por encima del promedio global
above_avg = pd.read_csv("../outputs/movies_above_avg.csv")

plt.figure(figsize=(10, 6))
sns.barplot(
    data=above_avg.sort_values("movie_avg", ascending=True),
    x="movie_avg",
    y="title",
    color="#c44e52"
)
plt.title("Movies Above Global Average / Películas sobre el Promedio Global")
plt.xlabel("Average Rating / Promedio de Calificación")
plt.ylabel("Movie / Película")
plt.tight_layout()
plt.savefig("../visuals/movies_above_avg.png")
plt.close()
print("🏆 Saved: visuals/movies_above_avg.png")

# --------------------------------------------------------------
# 5️⃣ GENRE RANKING
# --------------------------------------------------------------
# Ranking de películas dentro de cada género
genre_ranking = pd.read_csv("../outputs/genre_ranking.csv")

# Tomar las 3 mejores de cada género
top_per_genre = genre_ranking[genre_ranking["rank_in_genre"] <= 3]

plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=top_per_genre,
    x="avg_rating",
    y="genre",
    size="total_ratings",
    hue="rank_in_genre",
    palette="viridis",
    sizes=(30, 200)
)
plt.title("Top Movies per Genre (Window Function)\nTop Películas por Género (Función Ventana)")
plt.xlabel("Average Rating / Promedio")
plt.ylabel("Genre / Género")
plt.legend(title="Rank in Genre / Posición en Género")
plt.tight_layout()
plt.savefig("../visuals/genre_ranking.png")
plt.close()
print("🥇 Saved: visuals/genre_ranking.png")

print("\n✅ All visuals generated successfully / Todas las visualizaciones generadas correctamente.")
