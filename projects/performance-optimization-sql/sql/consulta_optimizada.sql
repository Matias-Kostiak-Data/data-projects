-- consulta_optimizada.sql
-- ELT/ETL Step 3: Transformation (Optimization) and Extraction - AFTER OPTIMIZATION
-- Paso 3 de ELT/ETL: Transformación (Optimización) y Extracción - DESPUÉS DE LA OPTIMIZACIÓN

-- GOAL: Drastically reduce query execution time from 3.8s to <0.5s using strategic indexing.
-- OBJETIVO: Reducir drásticamente el tiempo de ejecución de la consulta de 3.8s a <0.5s utilizando indexación estratégica.

-- PASO 1: IMPLEMENTING THE OPTIMIZATION / APLICANDO LA OPTIMIZACIÓN

-- IDEMPOTENCE: Drop index if it exists, preventing the "already exists" error on re-execution.
-- IDEMPOTENCIA: Eliminar índice si existe, previniendo el error "ya existe" al reejecutar.
DROP INDEX IF EXISTS idx_ordenes_cliente_id;
DROP INDEX IF EXISTS idx_clientes_region;

-- 1.1. CRUCIAL INDEX: Optimize the JOIN condition on the large 'ordenes' table (Foreign Key).
-- 1.1. ÍNDICE CRUCIAL: Optimizar la condición JOIN en la tabla grande 'ordenes' (Clave Foránea).
CREATE INDEX idx_ordenes_cliente_id ON ordenes (cliente_id);

-- 1.2. FILTER INDEX: Optimize the WHERE condition filter on the 'clientes' table.
-- 1.2. ÍNDICE DE FILTRO: Optimizar el filtro de condición WHERE en la tabla 'clientes'.
CREATE INDEX idx_clientes_region ON clientes (region);

-- 1.3. ANALYZE: Update PostgreSQL's statistics.
-- 1.3. ANALIZAR: Actualizar las estadísticas de PostgreSQL.
ANALYZE ordenes;
ANALYZE clientes;


-- PASO 2: THE OPTIMIZED QUERY / LA CONSULTA OPTIMIZADA
-- We use EXPLAIN ANALYZE again to measure the *new, fast* performance.
-- Usamos EXPLAIN ANALYZE de nuevo para medir el *nuevo y rápido* rendimiento.
EXPLAIN ANALYZE
SELECT
    c.cliente_id,
    c.nombre,
    c.email,
    COUNT(o.orden_id) AS total_ordenes,
    AVG(o.monto) AS promedio_monto
FROM
    clientes c
JOIN
    ordenes o ON c.cliente_id = o.cliente_id
WHERE
    c.region = 'Norte'
GROUP BY
    c.cliente_id, c.nombre, c.email
HAVING
    COUNT(o.orden_id) >= 10 AND AVG(o.monto) > 100.00
ORDER BY
    promedio_monto DESC;

-- SIMULATED EXPLAIN ANALYZE RESULT (AFTER OPTIMIZATION):
-- Execution Time: 485.671 ms (0.5 seconds)
-- Tiempo de Ejecución: 485.671 ms (0.5 segundos)