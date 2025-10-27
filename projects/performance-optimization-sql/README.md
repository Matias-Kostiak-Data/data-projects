# 🚀 SQL Performance Optimization Project (PostgreSQL)

## 🇪🇸 Resumen del Proyecto y Propuesta de Valor

Este proyecto demuestra la experiencia de un Ingeniero de Datos  en la **optimización crítica de bases de datos PostgreSQL** bajo condiciones de alto volumen.

**El Problema:** Un reporte de negocios esencial (filtrando 50,000 clientes y agregando 500,000 órdenes) estaba sufriendo un cuello de botella. La consulta se basaba en costosos **Sequential Scans** (Exploraciones Secuenciales) y un **Hash Join** ineficiente, resultando en latencias inaceptables.

**La Solución:** Se identificó la falta de indexación en la clave foránea (`ordenes.cliente_id`) y la columna de filtrado (`clientes.region`). Se aplicaron índices estratégicos y se actualizó el planificador de consultas (`ANALYZE`).

### Beneficios Cuantificables

| Métrica | ANTES de la Optimización | DESPUÉS de la Optimización | MEJORA |
| :--- | :--- | :--- | :--- |
| **Tiempo de Ejecución** | **759 ms** (0.76 segundos) | **230 ms** (0.23 segundos) | **~70% de Reducción** |
| **Recursos del Servidor** | Reducción del uso de CPU y memoria (menor dependencia del Hash Join). |

---

## 🇺🇸 Project Overview and Value Proposition

This project showcases a Senior Data Engineer’s expertise in **critical PostgreSQL database optimization** under high-volume conditions.

**The Problem:** An essential business report (filtering 50,000 clients and aggregating 500,000 orders) was suffering from a bottleneck. The query relied on costly **Sequential Scans** and an inefficient **Hash Join**, leading to unacceptable latency.

**The Solution:** Identified the lack of indexing on the foreign key (`ordenes.cliente_id`) and the filtering column (`clientes.region`). Applied strategic indexes and updated the query planner (`ANALYZE`).

### Quantifiable Benefits

| Metric | BEFORE Optimization | AFTER Optimization | IMPROVEMENT |
| :--- | :--- | :--- | :--- |
| **Execution Time** | **759 ms** (0.76 seconds) | **230 ms** (0.23 seconds) | **~70% Reduction** |
| **Server Resources** | Reduced CPU and memory usage (less reliance on Hash Join). |

---

## Estructura del Repositorio (Rutas Clave)

## Estructura del Repositorio (Rutas Clave) / Repository Structure

El proyecto está organizado profesionalmente siguiendo el flujo de trabajo de la Ingeniería de Datos.

* `performance-optimization-sql/`
    * `.gitignore`
    * `README.md`               <-- Este archivo. / This file.
    * `requirements.txt`        <-- Dependencias de Python. / Python dependencies.
    * `sql/`                    <-- Scripts SQL (La lógica de BD)
        * `setup_tablas.sql`    <-- ELT Load: Crea 500k filas y tablas. / Creates 500k rows and tables.
        * `consulta_lenta.sql`  <-- ELT Transform (Before): EXPLAIN ANALYZE lento. / Slow EXPLAIN ANALYZE.
        * `consulta_optimizada.sql` <-- ELT Transform (After): CREATE INDEX y EXPLAIN ANALYZE rápido. / CREATE INDEX and fast EXPLAIN ANALYZE.
    * `python/`                 <-- Script de Orquestación (El Pipeline)
        * `main_pipeline.py`    <-- Ejecuta scripts, mide el rendimiento y genera el gráfico final. / Executes scripts, measures performance, and generates the final graph.
    * `assets/`                 <-- Evidencia de la Optimización (Capturas/Gráficos)
        * `explain_analyze_antes.png`    <-- Captura del plan de ejecución lento. / Slow execution plan capture.
        * `explain_analyze_despues.png`  <-- Captura del plan de ejecución optimizado. / Optimized execution plan capture.
        * `performance_graph.png`        <-- Gráfico de barras que demuestra la mejora del ~70%. / Bar chart demonstrating ~70% improvement.
---

## Flujo de Trabajo (Para Pruebas)

Para replicar y validar la optimización, se deben ejecutar los scripts en este orden estricto (automatizado por `main_pipeline.py`):

1.  **Reiniciar Tablas:** Ejecutar `sql/setup_tablas.sql` (asegura que no haya índices).
2.  **Medir ANTES:** Ejecutar `sql/consulta_lenta.sql` para registrar el tiempo base (**759 ms**).
3.  **Aplicar Optimización:** Ejecutar la parte `CREATE INDEX` de `sql/consulta_optimizada.sql`.
4.  **Medir DESPUÉS:** Ejecutar la consulta `EXPLAIN ANALYZE` de `sql/consulta_optimizada.sql` para registrar el tiempo optimizado (**230 ms**).

El script de Python se encarga de estos cuatro pasos automáticamente.