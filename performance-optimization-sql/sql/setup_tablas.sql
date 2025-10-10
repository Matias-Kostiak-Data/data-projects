-- setup_tablas.sql
-- ELT/ETL Step 1: Data Structuring and Loading (Setting the environment)
-- Paso 1 de ELT/ETL: Estructuración y Carga de Datos (Configurando el entorno)

-- GOAL: Create the necessary data structures and populate them with enough volume
-- to accurately demonstrate a performance bottleneck. (50,000 clients, 500,000 orders).
-- OBJETIVO: Crear las estructuras de datos necesarias y llenarlas con suficiente volumen
-- para demostrar con precisión un cuello de botella en el rendimiento. (50,000 clientes, 500,000 pedidos).

-- 1. CLEANUP (Ensuring Idempotency): Drop tables if they exist to start fresh.
-- 1. LIMPIEZA (Asegurando Idempotencia): Eliminar tablas si existen para comenzar de nuevo.
DROP TABLE IF EXISTS ordenes;
DROP TABLE IF EXISTS clientes;

-- 2. Create the 'clientes' (clients) table (The small dimension table).
-- 2. Crear la tabla de 'clientes' (La tabla de dimensión pequeña).
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,         -- Unique Identifier, critical for JOINs. / Identificador único, crítico para las uniones (JOINs).
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    region VARCHAR(50)                  -- This column will be used for filtering. / Esta columna se utilizará para el filtrado.
);

-- 3. Create the 'ordenes' (orders) table (The large fact/transaction table).
-- 3. Crear la tabla de 'ordenes' (La tabla grande de hechos/transacciones).
CREATE TABLE ordenes (
    orden_id BIGINT PRIMARY KEY,        -- Using BIGINT for scalability (500k+ rows). / Usando BIGINT por escalabilidad (500k+ filas).
    cliente_id INT NOT NULL,            -- Foreign Key: The essential column for joining to 'clientes'. (CURRENTLY UNINDEXED!) / Clave Foránea: La columna esencial para unir con 'clientes'. (¡ACTUALMENTE SIN ÍNDICE!)
    fecha_orden DATE NOT NULL,
    monto NUMERIC(10, 2) NOT NULL,
    estado VARCHAR(20)
);

-- 4. Insert 50,000 Client Records.
-- 4. Insertar 50,000 Registros de Clientes.
INSERT INTO clientes (cliente_id, nombre, email, region)
SELECT
    s.i AS cliente_id,
    'Cliente ' || s.i,
    'cliente' || s.i || '@ejemplo.com',
    CASE (s.i % 5)
        WHEN 0 THEN 'Norte'
        WHEN 1 THEN 'Sur'
        WHEN 2 THEN 'Este'
        WHEN 3 THEN 'Oeste'
        ELSE 'Centro'
    END
FROM generate_series(1, 50000) s(i);

-- 5. Insert 500,000 Order Records.
-- This large volume ensures our unoptimized query will be noticeably slow.
-- 5. Insertar 500,000 Registros de Pedidos.
-- Este gran volumen asegura que nuestra consulta no optimizada será notablemente lenta.
INSERT INTO ordenes (orden_id, cliente_id, fecha_orden, monto, estado)
SELECT
    s.i AS orden_id,
    (random() * 49999 + 1)::int, -- Links orders to a random client ID (1 to 50000). / Enlaza pedidos con un ID de cliente aleatorio.
    CURRENT_DATE - (random() * 365)::int * '1 day'::interval,
    (random() * 1000 + 10)::numeric(10, 2),
    CASE floor(random() * 3)
        WHEN 0 THEN 'Completada'
        WHEN 1 THEN 'Pendiente'
        ELSE 'Cancelada'
    END
FROM generate_series(1, 500000) s(i);

-- SETUP COMPLETADO / SETUP COMPLETE.