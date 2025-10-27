"""
bulk_load_movies.py
-------------------
⚙️ Purpose / Propósito:
Load the full MovieLens dataset (movies, ratings, tags) into PostgreSQL using COPY for maximum speed.

Carga el dataset completo de MovieLens (movies, ratings, tags) en PostgreSQL usando COPY para máxima velocidad.
"""

import psycopg2
from psycopg2 import sql
import os

# ========== DATABASE CONNECTION CONFIG ==========
DB_CONFIG = {
    "host": "localhost",
    "dbname": "movielens_db",
    "user": "mati_user",
    "password": "prueba123",
    "port": 5432
}

# ========== FILE PATHS ==========
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
MOVIES_CSV = os.path.join(DATA_DIR, "movies_clean.csv")
RATINGS_CSV = os.path.join(DATA_DIR, "ratings_clean.csv")
TAGS_CSV = os.path.join(DATA_DIR, "tags_clean.csv")

# ========== CONNECT TO POSTGRESQL ==========
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()
print("✅ Connected to PostgreSQL / Conectado a PostgreSQL")

# ========== DROP OLD TABLES (IF ANY) ==========
cur.execute("""
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS movies;
""")
conn.commit()
print("🧹 Old tables dropped / Tablas anteriores eliminadas")

# ========== CREATE TABLES ==========
cur.execute("""
CREATE TABLE movies (
    movieid INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT
);

CREATE TABLE ratings (
    userid INTEGER,
    movieid INTEGER REFERENCES movies(movieid),
    rating FLOAT,
    timestamp BIGINT
);

CREATE TABLE tags (
    userid INTEGER,
    movieid INTEGER REFERENCES movies(movieid),
    tag TEXT,
    timestamp BIGINT
);
""")
conn.commit()
print("✅ Tables created successfully / Tablas creadas exitosamente")

# ========== BULK LOAD FUNCTION ==========
def bulk_copy(table_name, file_path, columns):
    """
    English: Load CSV data into PostgreSQL using COPY (the fastest method).
    Español: Carga los datos CSV en PostgreSQL usando COPY (el método más rápido).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # Skip header / Saltamos encabezado
        cur.copy_expert(
            sql.SQL("COPY {} ({}) FROM STDIN WITH CSV").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(map(sql.Identifier, columns))
            ),
            f
        )
    conn.commit()
    print(f"✅ {table_name} loaded successfully / {table_name} cargada correctamente")

# ========== LOAD DATA INTO TABLES ==========
print("📦 Loading data... / Cargando datos...")

bulk_copy("movies", MOVIES_CSV, ["movieid", "title", "genres"])
bulk_copy("ratings", RATINGS_CSV, ["userid", "movieid", "rating", "timestamp"])
bulk_copy("tags", TAGS_CSV, ["userid", "movieid", "tag", "timestamp"])

print("🎉 All data loaded successfully into PostgreSQL! / ¡Todos los datos cargados exitosamente en PostgreSQL!")

# ========== CLOSE CONNECTION ==========
cur.close()
conn.close()
print("🔒 Connection closed / Conexión cerrada")
