# main_pipeline.py
# SQL Performance Optimization Pipeline - FINAL VERSION with Graph Generation
# Pipeline de Optimización de Rendimiento SQL - VERSIÓN FINAL con Generación de Gráfico

import psycopg2
import os
import re
import matplotlib.pyplot as plt # Importamos Matplotlib para el gráfico
from typing import Optional

# --- 1. CONFIGURATION / CONFIGURACIÓN ---

# Define the path to the 'sql' folder and the 'assets' folder
# Definimos la ruta de la carpeta 'sql' y la carpeta 'assets'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SQL_DIR = os.path.join(BASE_DIR, "sql")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Ensure the assets directory exists
# Aseguramos que el directorio 'assets' exista
os.makedirs(ASSETS_DIR, exist_ok=True)

DB_CONFIG = {
    "dbname": "performance_demo_db",
    "user": "mati_user",
    "password": "prueba123",
    "host": "localhost",
    "port": "5432"
}

# --- 2. CORE EXECUTION FUNCTIONS / FUNCIONES PRINCIPALES ---

def generate_performance_graph(time_before_ms: float, time_after_ms: float, reduction_percentage: float):
    """
    Generates and saves a performance comparison bar chart to the assets directory.
    Genera y guarda un gráfico de barras de comparación de rendimiento en el directorio 'assets'.
    """
    times = [time_before_ms / 1000, time_after_ms / 1000] # Convert to seconds / Convertir a segundos
    labels = ['ANTES (Before)', 'DESPUÉS (After)']
    
    # Calculate colors based on performance
    colors = ['#FF6347', '#3CB371'] # Tomato (Red) for slow, MediumSeaGreen (Green) for fast
    
    plt.figure(figsize=(7, 5))
    bars = plt.bar(labels, times, color=colors)
    
    plt.title(f"Performance Optimization: {reduction_percentage:.2f}% Latency Reduction", fontsize=14)
    plt.ylabel("Execution Time (Seconds)")
    plt.ylim(0, max(times) * 1.2) # Set Y limit
    
    # Add data labels on top of the bars / Agregar etiquetas de datos
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.3f} s', ha='center', va='bottom', fontweight='bold')
    
    # Save the graph
    graph_path = os.path.join(ASSETS_DIR, "performance_graph.png")
    plt.savefig(graph_path)
    plt.close()
    
    print(f"\n[INFO] 📈 Gráfico de rendimiento generado y guardado en: {graph_path}")


def execute_sql_file(file_path: str, conn) -> Optional[float]:
    """
    Executes an SQL script and extracts the final execution time from EXPLAIN ANALYZE output.
    Ejecuta un script SQL y extrae el tiempo de ejecución final de la salida de EXPLAIN ANALYZE.
    """
    print(f"\n[INFO] Running / Ejecutando: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
    except Exception as e:
        print(f"[ERROR] Could not read file / No se pudo leer el archivo {file_path}: {e}")
        return None

    try:
        with conn.cursor() as cur:
            cur.execute(sql_script)
            
            execution_time = None
            
            # --- EXPLAIN ANALYZE Time Extraction Logic / Lógica de Extracción de Tiempo ---
            try:
                results = cur.fetchall()
                
                for row in results:
                    if row and len(row) > 0:
                        # Regex pattern to find "Execution Time: XXX.XXX ms"
                        match = re.search(r'Execution Time: (\d+\.\d+) ms', row[0])
                        if match:
                            execution_time = float(match.group(1))
                            print(f"[SUCCESS] Extracted Execution Time / Tiempo Extraído: {execution_time} ms")
                            break
                            
            except psycopg2.ProgrammingError:
                pass # Continue if no results expected
                
        conn.commit()
        return execution_time
        
    except psycopg2.Error as e:
        print(f"[ERROR] Database error during execution of {file_path}: {e}")
        conn.rollback()
        return None


def main():
    """Main pipeline execution function."""
    
    time_before_ms = None
    time_after_ms = None
    conn = None

    try:
        # 1. ESTABLISH CONNECTION (WITH ENCODING FIX)
        print("--- 1. CONNECTING TO POSTGRESQL / CONECTANDO A POSTGRESQL ---")
        
        # CRITICAL FIX: Use 'latin1' for client_encoding and sslmode='disable'
        conn = psycopg2.connect(
            dbname=DB_CONFIG['dbname'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            client_encoding='latin1', 
            sslmode='disable'         
        )
        print("Connection successful! / Conexión exitosa!")
        
        # 2. STEP 1: LOAD (SETUP)
        execute_sql_file(os.path.join(SQL_DIR, "setup_tablas.sql"), conn)

        # 3. STEP 2: MEASURE BASELINE (SLOW QUERY)
        time_before_ms = execute_sql_file(os.path.join(SQL_DIR, "consulta_lenta.sql"), conn)

        # 4. STEP 3: APPLY OPTIMIZATION & MEASURE NEW PERFORMANCE
        time_after_ms = execute_sql_file(os.path.join(SQL_DIR, "consulta_optimizada.sql"), conn)

        # 5. FINAL PERFORMANCE ANALYSIS & GRAPH GENERATION
        print("\n" + "="*50)
        print("--- FINAL PERFORMANCE ANALYSIS / ANÁLISIS DE RENDIMIENTO FINAL ---")
        
        if time_before_ms and time_after_ms:
            time_before_s = time_before_ms / 1000.0
            time_after_s = time_after_ms / 1000.0
            
            improvement_ms = time_before_ms - time_after_ms
            reduction_percentage = (improvement_ms / time_before_ms) * 100
            
            print(f"| 🚀 BEFORE OPTIMIZATION (ANTES): {time_before_s:.3f} s ({time_before_ms:.0f} ms)")
            print(f"| ⚡ AFTER OPTIMIZATION (DESPUÉS): {time_after_s:.3f} s ({time_after_ms:.0f} ms)")
            print(f"|")
            print(f"| ✅ ABSOLUTE IMPROVEMENT (MEJORA ABSOLUTA): Reduction of {improvement_ms:.0f} ms")
            print(f"| ✅ PERCENTAGE IMPROVEMENT (MEJORA PORCENTUAL): {reduction_percentage:.2f}%")
            print("="*50)
            
            # --- GENERATE GRAPH / GENERAR GRÁFICO ---
            generate_performance_graph(time_before_ms, time_after_ms, reduction_percentage)

        else:
            print("Could not extract both execution times. Review logs.")

    except psycopg2.Error as e:
        print(f"\n[FATAL ERROR] Could not connect to the database: {e}")
    
    finally:
        if conn:
            conn.close()
            print("\nConnection closed. / Conexión cerrada.")


if __name__ == "__main__":
    main()