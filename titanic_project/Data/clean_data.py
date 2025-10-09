#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# clean_data.py
# Proyecto: Titanic Data Engineering
# Autor: Matías Kostiak
# Fecha: 2025-10-07
# Descripción:
# Este script limpia el dataset del Titanic, realiza transformaciones básicas 
# y genera un CSV limpio listo para análisis o carga en base de datos.
# This script cleans the Titanic dataset, performs basic transformations, 
# and outputs a clean CSV ready for analysis or database insertion.

# 📘 Import libraries / Importar librerías
import pandas as pd
import numpy as np

# 📌 Load dataset / Cargar dataset
df = pd.read_csv('data/test.csv')  # CSV original sin limpiar

# 🔍 Preview first rows / Mostrar primeras filas
print(df.head())

# 🧹 Check null values / Verificar valores nulos
print(df.isnull().sum())

# 💡 Fill missing values / Llenar valores nulos
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Edad: media
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Puerto de embarque: moda
if 'Fare' in df.columns:
    df['Fare'] = df['Fare'].fillna(df['Fare'].mean())  # Tarifa: media

# ✂️ Clean column names and text / Limpiar nombres de columnas y texto
df.columns = df.columns.str.strip()
df['Name'] = df['Name'].str.strip()
df['Sex'] = df['Sex'].str.lower()

# 📝 Export cleaned dataset / Exportar CSV limpio
df.to_csv('data/test_clean.csv', index=False)

print("✅ Dataset limpio exportado a data/test_clean.csv / Clean dataset exported")
