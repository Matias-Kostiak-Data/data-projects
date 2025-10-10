-- consulta_lenta.sql
-- ELT/ETL Step 2: Extraction and Transformation (The Bottleneck) - BEFORE OPTIMIZATION
-- Paso 2 de ELT/ETL: Extracción y Transformación (El Cuello de Botella) - ANTES DE LA OPTIMIZACIÓN

-- ACTION: Use EXPLAIN ANALYZE to run the query and measure its actual performance.
-- ACCIÓN: Utilizar EXPLAIN ANALYZE para ejecutar la consulta y medir su rendimiento real.
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
    ordenes o ON c.cliente_id = o.cliente_id -- THE CORE PROBLEM: Joining the 500k-row 'ordenes' table
                                              -- on a non-indexed column forces slow table scans (e.g., Hash Join).
                                              -- EL PROBLEMA CENTRAL: Unir la tabla 'ordenes' (500k filas)
                                              -- en una columna sin índice fuerza lentas exploraciones de tabla (ej., Hash Join).
WHERE
    c.region = 'Norte' -- FILTERING PROBLEM: This filter also lacks an index, slowing down client selection.
                        -- PROBLEMA DE FILTRADO: Este filtro también carece de un índice, ralentizando la selección de clientes.
GROUP BY
    c.cliente_id, c.nombre, c.email
HAVING
    COUNT(o.orden_id) >= 10 AND AVG(o.monto) > 100.00
ORDER BY
    promedio_monto DESC;

-- SIMULATED EXPLAIN ANALYZE RESULT (BEFORE OPTIMIZATION):
-- Execution Time: 3845.213 ms (3.8 seconds)
-- Tiempo de Ejecución: 3845.213 ms (3.8 segundos)