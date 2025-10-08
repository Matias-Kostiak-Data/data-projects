# 🎬 MovieLens Dashboard Project / Proyecto Dashboard MovieLens

## 📖 Descripción / Description
Este proyecto es un dashboard interactivo desarrollado con **Streamlit** y **Plotly**, usando los datasets de MovieLens. Permite explorar películas, ratings y géneros de manera visual y dinámica.  
This project is an interactive dashboard built with **Streamlit** and **Plotly**, using MovieLens datasets. It allows you to explore movies, ratings, and genres visually and dynamically.

**Características / Features:**
- KPIs generales / General KPIs: total de películas, ratings, promedio global y género más popular / total movies, ratings, global average, and most popular genre.
- Gráficos interactivos / Interactive charts:
  - Top películas según promedio de rating / Top movies by average rating
  - Promedio de rating por género / Average rating by genre
  - Popularidad de los géneros / Genre popularity by number of ratings
- Filtros dinámicos / Dynamic filters: selección de género y rating mínimo / genre selection and minimum rating
- Exportación de resultados filtrados a CSV / Export filtered results to CSV
- Footer con crédito: "Hecho por Matías Kostiak / Made by Matías Kostiak"

---

## 📂 Estructura de Carpetas / Folder Structure

movielens_project/
├─ data/ # CSVs procesados / Cleaned CSVs
├─ scripts/ # Scripts de Python
├─ visuals/ # Capturas o GIFs del dashboard / Screenshots or GIFs
└─ README.md


**Archivos importantes / Key files:**
- `data/movies_clean.csv` → Lista de películas limpias / Clean movie list
- `data/ratings_clean.csv` → Ratings limpios / Clean ratings
- `data/tags_clean.csv` → Tags limpios / Clean tags
- `data/top_movies.csv` → Top 10 de películas / Top 10 movies
- `data/movies_above_avg.csv` → Películas sobre promedio / Movies above average rating
- `data/genre_avg.csv` → Promedio de rating por género / Average rating per genre
- `data/genre_ranking.csv` → Ranking de géneros / Genre ranking
- `data/genre_popularity.csv` → Popularidad de géneros / Genre popularity
- `scripts/movielens_dashboard_final.py` → Dashboard interactivo final / Final interactive dashboard
- `visuals/` → Capturas o GIFs del dashboard / Dashboard screenshots or GIFs

---

## ⚙️ Requisitos / Dependencies

- Python >= 3.10
- Pandas
- Streamlit
- Plotly

Instalar dependencias / Install dependencies:

```bash
pip install pandas streamlit plotly
🚀 Ejecución / Run the Dashboard

Abrir terminal en la raíz del proyecto / Open terminal in project root.

Ejecutar / Run:

streamlit run scripts/movielens_dashboard_final.py


Abrir el navegador en la URL indicada (normalmente http://localhost:8501
) / Open the browser at the URL Streamlit provides (usually http://localhost:8501
)

Explorar KPIs, gráficos y filtros / Explore KPIs, charts, and filters

Descargar CSV filtrado si se desea / Download filtered CSV if needed

📊 Visualizaciones / Visualizations

Capturas de ejemplo / Example screenshots:

KPIs generales / General KPIs


Top 10 películas / Top 10 movies


Promedio de rating por género / Average rating by genre


Popularidad de géneros / Genre popularity


Tip de captura:
En Windows puedes usar Windows + G para abrir la Xbox Game Bar y capturar imágenes o grabar GIFs del dashboard en acción.

✍️ Créditos / Author

Hecho por Matías Kostiak / Made by Matías Kostiak