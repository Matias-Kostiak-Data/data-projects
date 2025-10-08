# -*- coding: utf-8 -*-
# Streamlit Dashboard for MovieLens Dataset
# Dashboard de Streamlit para el dataset de MovieLens
# Hecho por / Made by Matías Kostiak

import pandas as pd
import streamlit as st
import plotly.express as px

# -------------------------
# Load CSVs / Cargar CSVs
# -------------------------
movies = pd.read_csv("data/movies_clean.csv")      # Movies CSV / CSV de películas
ratings = pd.read_csv("data/ratings_clean.csv")    # Ratings CSV / CSV de ratings
tags = pd.read_csv("data/tags_clean.csv")          # Tags CSV / CSV de etiquetas
top_movies = pd.read_csv("data/top_movies.csv")    # Top movies CSV / Películas top
movies_above_avg = pd.read_csv("data/movies_above_avg.csv")  # Movies above average / Películas sobre promedio
genre_avg = pd.read_csv("data/genre_avg.csv")      # Average rating per genre / Promedio por género
genre_popularity = pd.read_csv("data/genre_popularity.csv")  # Popularity per genre / Popularidad por género

# -------------------------
# Streamlit page config
# -------------------------
st.set_page_config(
    page_title="MovieLens Dashboard",
    layout="wide",
    page_icon="🎬"
)

# -------------------------
# Footer credit / Crédito
# -------------------------
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>Hecho por Matías Kostiak / Made by Matías Kostiak</p>",
    unsafe_allow_html=True
)

# -------------------------
# KPIs Section / Sección KPIs
# -------------------------
st.title("MovieLens Dashboard 🎬")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Movies / Total películas", movies.shape[0])
col2.metric("Total Ratings / Total ratings", ratings.shape[0])
col3.metric("Average Rating / Promedio global", round(ratings['rating'].mean(), 2))
most_popular_genre = genre_popularity.loc[genre_popularity['num_ratings'].idxmax(), 'genres']
col4.metric("Most Popular Genre / Género más popular", most_popular_genre)

st.markdown("---")

# -------------------------
# Sidebar Filters / Filtros
# -------------------------
st.sidebar.header("Filters / Filtros")

# Genre filter / Filtro de género
genre_options = genre_avg['genres'].unique()
selected_genre = st.sidebar.selectbox("Select Genre / Seleccionar género", options=genre_options)

# Minimum rating filter / Filtro de rating mínimo
min_rating = st.sidebar.slider("Minimum Rating / Rating mínimo", min_value=0.0, max_value=5.0, value=3.5, step=0.1)

# -------------------------
# Top Movies Chart / Gráfico Top Movies
# -------------------------
top_filtered = top_movies[top_movies['mean'] >= min_rating]
fig_top_movies = px.bar(
    top_filtered.sort_values('mean', ascending=True),
    x='mean',
    y='title',
    orientation='h',
    hover_data=['count', 'movieId'],
    labels={'mean': 'Average Rating / Promedio', 'title': 'Title / Título'},
    title="Top Movies by Rating / Películas Top por Rating"
)
st.plotly_chart(fig_top_movies, use_container_width=True)

# -------------------------
# Genre Average Rating / Promedio por Género
# -------------------------
genre_filtered = genre_avg[genre_avg['genres'] == selected_genre]
fig_genre_avg = px.bar(
    genre_filtered,
    x='genres',
    y='avg_rating',
    labels={'avg_rating': 'Average Rating / Promedio'},
    title=f"Average Rating for Genre: {selected_genre} / Promedio por género"
)
st.plotly_chart(fig_genre_avg, use_container_width=True)

# -------------------------
# Genre Popularity / Popularidad por Género
# -------------------------
fig_genre_pop = px.bar(
    genre_popularity.sort_values('num_ratings', ascending=False),
    x='genres',
    y='num_ratings',
    labels={'num_ratings': 'Number of Ratings / Cantidad de ratings', 'genres': 'Genre / Género'},
    title="Genre Popularity / Popularidad por Género"
)
st.plotly_chart(fig_genre_pop, use_container_width=True)

# -------------------------
# Export CSV / Exportar CSV
# -------------------------
st.markdown("---")
st.header("Export Filtered Top Movies / Exportar Top Movies filtradas")
st.download_button(
    label="Download CSV / Descargar CSV",
    data=top_filtered.to_csv(index=False).encode('utf-8'),
    file_name="top_movies_filtered.csv",
    mime="text/csv"
)
