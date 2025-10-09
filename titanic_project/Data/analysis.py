#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# analysis.py
# Proyecto: Titanic Data Engineering
# Autor: Matías Kostiak
# Descripción:
# Este script conecta con PostgreSQL, inserta datos del CSV limpio,
# ejecuta consultas SQL y genera gráficos básicos.
# This script connects to PostgreSQL, inserts cleaned CSV data,
# runs SQL queries, and generates basic visualizations.

import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Cargar CSV limpio / Load cleaned CSV
df = pd.read_csv('test_clean.csv')
print("✅ CSV limpio cargado / Clean CSV loaded")

# 2️⃣ Conexión a PostgreSQL / PostgreSQL connection
# Cambia los parámetros según tu configuración local
conn = psycopg2.connect(
    host="localhost",
    database="titanic_db2",
    user="mati_user",
    password="prueba123"
)
cur = conn.cursor()
print("✅ Conexión a PostgreSQL establecida / PostgreSQL connection established")

# 3️⃣ Crear tabla Titanic si no existe / Create Titanic table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS titanic (
    PassengerId INT PRIMARY KEY,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age FLOAT,
    SibSp INT,
    Parch INT,
    Ticket TEXT,
    Fare FLOAT,
    Cabin TEXT,
    Embarked TEXT,
    Title TEXT
);
"""
cur.execute(create_table_query)
conn.commit()
print("✅ Tabla Titanic lista / Titanic table ready")

# 4️⃣ Insertar datos del CSV / Insert CSV data into PostgreSQL
for i, row in df.iterrows():
    cur.execute("""
        INSERT INTO titanic (PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Title)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (PassengerId) DO NOTHING;
    """, tuple(row))
conn.commit()
print("✅ Datos insertados / Data inserted into PostgreSQL")

# 5️⃣ Consultas SQL y resultados / SQL queries and results

# Pasajeros por clase / Passengers per class
cur.execute("SELECT Pclass, COUNT(*) AS num_passengers FROM titanic GROUP BY Pclass ORDER BY Pclass;")
print("\n📊 Pasajeros por clase / Passengers per class:")
for record in cur.fetchall():
    print(record)

# Edad promedio por sexo / Average age by gender
cur.execute("SELECT Sex, AVG(Age) AS avg_age FROM titanic GROUP BY Sex;")
print("\n📊 Edad promedio por sexo / Average age by gender:")
for record in cur.fetchall():
    print(record)

# Top 10 boletos más caros / Top 10 highest fares
cur.execute("SELECT Name, Ticket, Fare FROM titanic ORDER BY Fare DESC LIMIT 10;")
print("\n📊 Top 10 boletos más caros / Top 10 highest fares:")
for record in cur.fetchall():
    print(record)

# 6️⃣ Gráficos con Matplotlib y Seaborn / Visualizations

# Pasajeros por clase / Passengers per class
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', data=df)
plt.title('Pasajeros por clase / Passengers per class')
plt.savefig('passengers_per_class.png')
plt.close()

# Edad promedio por sexo / Average age by gender
plt.figure(figsize=(6,4))
sns.barplot(x='Sex', y='Age', data=df)
plt.title('Edad promedio por sexo / Average age by gender')
plt.savefig('avg_age_by_gender.png')
plt.close()

# Top 10 tarifas más altas / Top 10 highest fares
top10 = df.nlargest(10, 'Fare')
plt.figure(figsize=(10,5))
sns.barplot(x='Name', y='Fare', data=top10)
plt.title('Top 10 boletos más caros / Top 10 highest fares')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top10_fares.png')
plt.close()

print("✅ Gráficos generados y guardados como PNG / Graphs generated and saved as PNG")

# 7️⃣ Cerrar conexión / Close connection
cur.close()
conn.close()
print("✅ Conexión cerrada / Connection closed")

