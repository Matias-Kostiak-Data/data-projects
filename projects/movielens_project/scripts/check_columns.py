import pandas as pd

# Lista de CSVs a chequear
csv_files = [
    "data/movies_clean.csv",
    "data/ratings_clean.csv",
    "data/tags_clean.csv",
    "data/top_movies.csv",
    "data/movies_above_avg.csv",
    "data/genre_avg.csv",
    "data/genre_ranking.csv",
    "data/genre_popularity.csv"
]

for file in csv_files:
    try:
        df = pd.read_csv(file)
        print(f"Columns in {file}:")
        print(df.columns.tolist(), "\n")
    except FileNotFoundError:
        print(f"⚠️ File not found: {file}\n")
