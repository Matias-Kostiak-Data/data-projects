"""
Author: Matías Kostiak
Role: Data Engineer | Automations & Data Solutions Builder
Project: Global Sales ETL - Superstore Dataset

🇺🇸 Description:
This script executes a complete ETL pipeline for the Superstore dataset.
It reads raw sales data from 'data/raw', cleans and enriches it,
and loads the final dataset into PostgreSQL local.
Optionally, it can save a processed CSV in 'data/processed'.

🇪🇸 Descripción:
Este script ejecuta un pipeline ETL completo para el dataset Superstore.
Lee los datos crudos desde 'data/raw', los limpia y enriquece,
y carga el dataset final en PostgreSQL local.
Opcionalmente, puede guardar un CSV procesado en 'data/processed'.
"""

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import sys

# =======================
# Database configuration / Configuración de la base de datos
# =======================
DB_USER = "mati_user"
DB_PASSWORD = "prueba123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "global_sales_db"

CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(CONNECTION_STRING)

# =======================
# Paths / Rutas
# =======================
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = ROOT_DIR / "data" / "raw" / "superstore_sales.csv"
PROCESSED_CSV_PATH = ROOT_DIR / "data" / "processed" / "superstore_sales_clean.csv"

# =======================
# ETL Process
# =======================

# Check if file exists / Verificar existencia del archivo
if not RAW_CSV_PATH.exists():
    print(f"❌ CSV file not found at: {RAW_CSV_PATH}")
    print("🇪🇸 Archivo CSV no encontrado. Verifica la ruta antes de continuar.")
    sys.exit(1)

# Extract / Extracción
print(f"📥 Extracting data from: {RAW_CSV_PATH} / Extrayendo datos de: {RAW_CSV_PATH}")
try:
    df = pd.read_csv(RAW_CSV_PATH, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(RAW_CSV_PATH, encoding="latin1")
    print("⚠️ UTF-8 failed, loaded CSV using latin1 / UTF-8 falló, se cargó con latin1")

# Transform / Transformación
df.columns = df.columns.str.lower().str.replace(" ", "_")
df.dropna(inplace=True)
if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
if "ship_date" in df.columns:
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")
if {"sales", "profit"}.issubset(df.columns):
    df["profit_margin"] = (df["profit"] / df["sales"]).round(2)

print("✅ Data extraction and transformation completed.")
print("🇪🇸 Extracción y transformación de datos completadas.")

# Optional: save processed CSV / Guardar CSV procesado
PROCESSED_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCESSED_CSV_PATH, index=False)
print(f"💾 Processed CSV saved at: {PROCESSED_CSV_PATH}")
print(f"🇪🇸 CSV procesado guardado en: {PROCESSED_CSV_PATH}")

# Load / Carga
table_name = "superstore_sales"
try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ ETL process completed successfully. Table '{table_name}' loaded to PostgreSQL local.")
    print("🇪🇸 Proceso ETL completado correctamente. Tabla cargada en PostgreSQL local.")
except Exception as e:
    print("❌ Error during load / 🇪🇸 Error durante la carga:")
    print(e)
