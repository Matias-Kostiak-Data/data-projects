-- -----------------------------------------------
-- Titanic Data Engineering Project
-- SQL Queries File
-- Author: Matías Kostiak – Ingeniero de Datos
-- -----------------------------------------------

-- 1️⃣ Contar pasajeros por clase / Count passengers per class
SELECT Pclass, COUNT(*) AS num_passengers
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;

-- 2️⃣ Edad promedio por género / Average age by gender
SELECT Sex, AVG(Age) AS avg_age
FROM titanic
GROUP BY Sex;

-- 3️⃣ Top 10 boletos más caros / Top 10 highest fares
SELECT Name, Ticket, Fare
FROM titanic
ORDER BY Fare DESC
LIMIT 10;

-- 4️⃣ Ejemplo extra: Número de hermanos/cónyuges a bordo / Number of siblings/spouses aboard
SELECT SibSp, COUNT(*) AS num_passengers
FROM titanic
GROUP BY SibSp
ORDER BY SibSp;

-- 5️⃣ Ejemplo extra: Número de padres/hijos a bordo / Number of parents/children aboard
SELECT Parch, COUNT(*) AS num_passengers
FROM titanic
GROUP BY Parch
ORDER BY Parch;

-- 6️⃣ Promedio de tarifa por clase / Average fare by class
SELECT Pclass, AVG(Fare) AS avg_fare
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;
