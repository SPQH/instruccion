/* Consulta avanzada sobre tablas: 

SELECT 
FROM 
WHERE

*/

SELECT * FROM Personas;
SELECT nombre,nacimiento FROM Personas;
SELECT nombre,nacimiento FROM Personas WHERE sexo = 1 AND nacimiento < 2000;