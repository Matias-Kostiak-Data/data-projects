"""
Author: Matías Kostiak
Role: Data Engineer | Automations & Data Solutions Builder
Project: Global Sales Dashboard - Superstore Dataset

🇺🇸 Description:
Professional Streamlit dashboard with separate KPI sections, interactive charts,
filters, and CSV export. Connected to PostgreSQL local with fallback to processed CSV.

🇪🇸 Descripción:
Dashboard profesional de Streamlit con secciones separadas de KPIs,
gráficos interactivos, filtros y exportación de CSV.
Conectado a PostgreSQL local con fallback a CSV procesado.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

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
PROCESSED_CSV_PATH = ROOT_DIR / "data" / "processed" / "superstore_sales_clean.csv"

# =======================
# Streamlit App
# =======================
st.set_page_config(page_title="🌎 Global Sales Dashboard", layout="wide")
st.title("🌎 Global Sales Dashboard - Superstore Dataset")
st.markdown("🇺🇸 Interactive KPIs & Charts | 🇪🇸 KPIs y gráficos interactivos")

# =======================
# Load data / Cargar datos
# =======================
@st.cache_data
def load_data():
    try:
        df = pd.read_sql("SELECT * FROM superstore_sales;", engine)
        st.success("✅ Data loaded from PostgreSQL / Datos cargados desde PostgreSQL")
    except Exception:
        df = pd.read_csv(PROCESSED_CSV_PATH)
        st.warning("⚠️ PostgreSQL failed, loaded CSV fallback / PostgreSQL falló, se cargó CSV")
    return df

df = load_data()

# =======================
# Filters / Filtros
# =======================
st.sidebar.header("Filters / Filtros")
regions = df['region'].unique().tolist()
categories = df['category'].unique().tolist()
min_date = df['order_date'].min()
max_date = df['order_date'].max()

selected_region = st.sidebar.multiselect("Select Region / Seleccionar Región", regions, default=regions)
selected_category = st.sidebar.multiselect("Select Category / Seleccionar Categoría", categories, default=categories)
date_range = st.sidebar.date_input("Select Date Range / Seleccionar Rango de Fechas", [min_date, max_date])

filtered_df = df[
    (df['region'].isin(selected_region)) &
    (df['category'].isin(selected_category)) &
    (df['order_date'] >= pd.to_datetime(date_range[0])) &
    (df['order_date'] <= pd.to_datetime(date_range[1]))
]

# =======================
# KPI Financials / KPIs Financieros
# =======================
with st.container():
    st.subheader("Financial Metrics / Métricas Financieras")
    col1, col2, col3 = st.columns(3, gap="large")
    total_sales = filtered_df['sales'].sum()
    avg_ticket = filtered_df['sales'].mean()
    profit_margin = filtered_df['profit_margin'].mean()
    col1.metric("💰 Total Sales (Filtered) / Ventas Totales (Filtradas)", f"${total_sales:,.2f}")
    col2.metric("🎟 Average Ticket / Ticket Promedio", f"${avg_ticket:,.2f}")
    col3.metric("📊 Average Profit Margin / Margen Promedio de Ganancia", f"{profit_margin:.2%}")

st.markdown("---")

# =======================
# KPI Product & Customer / Producto y Cliente
# =======================
with st.container():
    st.subheader("Product & Customer Insights / Insights de Producto y Cliente")
    col1, col2 = st.columns(2, gap="large")
    top_product = filtered_df.groupby('product_name')['sales'].sum().idxmax()
    top_region = filtered_df.groupby('region')['sales'].sum().idxmax()
    num_customers = filtered_df['customer_name'].nunique()
    col1.metric("🏆 Top Product / Producto Top", top_product)
    col2.metric("🌍 Top Region / Región Top", top_region)
    st.write(f"👥 Unique Customers / Clientes Únicos: {num_customers}")

st.markdown("---")

# =======================
# Charts / Gráficos
# =======================
st.subheader("Sales by Category / Ventas por Categoría")
sales_by_category = filtered_df.groupby('category')['sales'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_category)

st.subheader("Sales over Time / Ventas a lo largo del tiempo")
sales_over_time = filtered_df.groupby('order_date')['sales'].sum()
st.line_chart(sales_over_time)

st.subheader("Top 10 Products by Sales / Top 10 Productos por Ventas")
top10_products = filtered_df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top10_products)

st.subheader("Sales by Region / Ventas por Región")
sales_by_region = filtered_df.groupby('region')['sales'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_region)

st.markdown("---")

# =======================
# Export / Exportar CSV
# =======================
st.subheader("Export Filtered Data / Exportar datos filtrados")
st.download_button(
    label="📥 Download CSV / Descargar CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_superstore_sales.csv',
    mime='text/csv'
)
