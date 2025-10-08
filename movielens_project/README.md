# 🎬 MovieLens Dashboard Project / Proyecto Dashboard MovieLens

## 🔹 Download Raw Data / Descargar datos crudos
Los datasets originales son demasiado grandes para GitHub. Descárgalos desde Google Drive y colócalos en la carpeta **`movielens_project/data/Official data/`** antes de ejecutar el dashboard.

*The raw datasets are too large for GitHub, please download them from Google Drive and place them in the folder **`movielens_project/data/Official data/`** before running the dashboard.*

- [movies.csv](https://drive.google.com/file/d/1r96MN4fhuBXzDjhkdCwwZXU5CTIfZTLC/view?usp=drive_link)
- [ratings.csv](https://drive.google.com/file/d/1cOyA93dPn9S4AZX_rCfIogvRQHDGtpfU/view?usp=drive_link)
- [tags.csv](https://drive.google.com/file/d/1giG46q7Kpro7-cneuJOUUQbiKdurbhhE/view?usp=drive_link)

---

## 📖 Descripción / Description
Este proyecto es un dashboard interactivo desarrollado con **Streamlit** y **Plotly**, usando los datasets de **MovieLens**. Permite explorar películas, ratings y géneros de manera visual y dinámica.

*This project is an interactive dashboard built with **Streamlit** and **Plotly**, using **MovieLens** datasets. It allows you to explore movies, ratings, and genres visually and dynamically.*

---

## 🚀 Características / Features
- **KPIs generales / General KPIs:** total de películas, ratings, promedio global y género más popular
- **Gráficos interactivos / Interactive charts:**
  - Top películas según promedio de rating / Top movies by average rating
  - Promedio de rating por género / Average rating by genre
  - Popularidad de los géneros / Genre popularity by number of ratings
- **Filtros dinámicos / Dynamic filters:** selección de género y rating mínimo
- **Exportación a CSV / CSV export:** exportar resultados filtrados
- **Footer con crédito:** “Hecho por Matías Kostiak / Made by Matías Kostiak”

---

## 📂 Estructura de Carpetas / Folder Structure
movielens_project/
|-- data/                # CSVs procesados / Cleaned CSVs
|   |-- Official data/   # Datos crudos descargados / Raw datasets
|   `-- ...              # Archivos limpios generados
|-- scripts/             # Scripts de Python
|   `-- movielens_dashboard_final.py
|-- visuals/             # Capturas o GIFs del dashboard / Screenshots or GIFs
`-- README.md



### 🔑 Archivos importantes / Key files
- `data/movies_clean.csv` → Lista de películas limpias / Clean movie list
- `data/ratings_clean.csv` → Ratings limpios / Clean ratings
- `data/tags_clean.csv` → Tags limpios / Clean tags
- `data/top_movies.csv` → Top 10 de películas / Top 10 movies
- `data/movies_above_avg.csv` → Películas sobre promedio / Movies above average rating
- `data/genre_avg.csv` → Promedio de rating por género / Average rating per genre
- `data/genre_ranking.csv` → Ranking de géneros / Genre ranking
- `data/genre_popularity.csv` → Popularidad de géneros / Genre popularity
- `scripts/movielens_dashboard_final.py` → Dashboard final / Final dashboard script
- `visuals/` → Capturas o GIFs del dashboard / Dashboard screenshots or GIFs

---

## ⚙️ Requisitos / Dependencies
- **Python** >= 3.10
- **Pandas**
- **Streamlit**
- **Plotly**

### 📦 Instalar dependencias / Install dependencies:
bash
pip install pandas streamlit plotly

###🚀 Ejecución / Run the Dashboard
Abre una terminal en la raíz del proyecto
(Open terminal in project root)

Ejecuta el siguiente comando:
(Run the following command)

streamlit run scripts/movielens_dashboard_final.py

Abre el navegador en la URL indicada por Streamlit
(Usually http://localhost:8501)

Explora KPIs, gráficos y filtros
(Explore KPIs, charts, and filters)

Descarga CSV filtrado si lo deseas
(Download filtered CSV if needed)

Hecho por Matías Kostiak / Made by Matías Kostiak
