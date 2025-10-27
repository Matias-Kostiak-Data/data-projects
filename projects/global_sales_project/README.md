# 🌎 Global Sales Dashboard - Superstore Dataset

**Author:** Matías Kostiak  
**Role:** Data Engineer | Automations & Data Solutions Builder  

---

## 🇺🇸 Description / 🇪🇸 Descripción

🇺🇸 Professional Streamlit dashboard to visualize global sales data from the Superstore dataset.  
🇪🇸 Dashboard profesional de Streamlit para visualizar datos de ventas globales del dataset Superstore.  

🇺🇸 Connects to PostgreSQL, with fallback to processed CSV. Includes:  
🇪🇸 Conexión a PostgreSQL con respaldo a CSV procesado. Incluye:  

- 🇺🇸 KPIs: Total sales, average ticket, profit margin, top product, top region, unique customers  
  🇪🇸 KPIs: Ventas totales, ticket promedio, margen de ganancia, producto top, región top, clientes únicos  
- 🇺🇸 Interactive charts: Sales by category, sales over time, top 10 products, sales by region  
  🇪🇸 Gráficos interactivos: Ventas por categoría, ventas a lo largo del tiempo, top 10 productos, ventas por región  
- 🇺🇸 Filters: Region, category, date range  
  🇪🇸 Filtros: Región, categoría, rango de fechas  
- 🇺🇸 Export: Download filtered CSV  
  🇪🇸 Exportación: Descargar CSV filtrado  
- 🇺🇸 Fully reproducible ETL pipeline  
  🇪🇸 Pipeline ETL completamente reproducible  

---

## 🛠 Installation / Instalación

```bash
# 1. Clone the repository / Clonar el repositorio
git clone <YOUR_REPO_URL>
cd global_sales_project

# 2. Install dependencies / Instalar dependencias
pip install -r requirements.txt

# 3. Run ETL / Ejecutar ETL
python scripts/etl.py

# 4. Launch dashboard / Ejecutar dashboard
streamlit run dashboards/dashboard.py


##⚡ Requirements / Requerimientos
pandas        # Data manipulation / Manipulación de datos
sqlalchemy    # Database connection / Conexión a base de datos
psycopg2-binary # PostgreSQL driver / Driver de PostgreSQL
streamlit     # Dashboard framework / Framework para dashboard

##📈 Features / Funcionalidades

🇺🇸 Interactive KPIs and charts / KPIs y gráficos interactivos

🇺🇸 Filters by region, category, and date range / Filtros por región, categoría y rango de fechas

🇺🇸 Export filtered dataset as CSV / Exportar dataset filtrado como CSV

🇺🇸 Fully reproducible ETL pipeline / Pipeline ETL completamente reproducible

📂 Project Structure / Estructura de Carpetas


global_sales_project/
├── data/
│   ├── raw/
│   │   └── superstore_sales.csv
│   └── processed/
├── scripts/
│   ├── etl.py
│   └── helpers.py
├── dashboards/
│   └── dashboard.py
├── visuals/ 
├── README.md
└── requirements.txt
