/* Acceso a base de datos:  sudo mariadb -u root -p */
                   Salida:  exit

/* Creación de base de datos */
CREATE DATABASE Test

/* Visualización y elección de base de datos */
SHOW DATABASES;
USE Test;

/* Creación de tablas */
CREATE TABLE Persona (
    id INT(11) NOT NULL AUTO_INCREMENT UNIQUE,
    nombre VARCHAR(20) NOT NULL,
    estatura INT,
    peso INT,
    pais VARCHAR(20),
    PRIMARY KEY (id));

/* Modificación de tablas */
RENAME TABLE Personas TO Animales; /* Renombrar una tabla */
ALTER TABLE Personas ADD Sexo BIT(1); /* Añadir nuevo campo a tabla */
ALTER TABLE Personas CHANGE annoNacimiento nacimiento INT; /* Cambiar el nombre */
ALTER TABLE Personas CHANGE nombre nombre VARCHAR(50); /* Cambiar el tipo de dato */
DROP TABLE Personas; /* Borrar tabla seleccionada */
DELETE FROM Personas WHERE edad =1; /* Elimina registros de las tablas */
UPDATE Personas SET edad, estatura WHERE id = 1; /* Actualizar registros de las tablas */

/* Visualización de estructura */
show tables;
describe Personas;

/* Insertar un registro en una tabla */
INSERT INTO Personas(nombre, apellido1, nacimiento, estatura, peso, nacionalidad, color)
values("Alfredo", "García", 1990, 1.8, 74, "España", "Azul");

/* Insertar múltiples registros en una tabla en un solo comando */
INSERT INTO Personas
    (nombre, apellido1, nacimiento)
VALUES
    ("Juan", "Salgado", 1998),
    ("Elena", "López", 1994),
    ("Estefanía", "Díaz", 1991);
    
/* Consultas */
SELECT * FROM Personas; /* Consultar todo el contenido de Personas */
SELECT nombre,nacimiento FROM Personas; /* Consultar el contenido por columnas */
SELECT nombre,nacimiento FROM Personas WHERE sexo = 1; /* Consultar el contenido por columnas con condiciones */
SELECT nombre,nacimiento FROM Personas WHERE sexo = 1 AND nacimiento < 2000; /* Conultar el contenido por columnas con mas de una condicion */
SELECT * FROM Personas WHERE estatura IS NOT NULL / IS NULL; /* Comprobar si hay registros vacios */
SELECT * FROM Personas ORDER BY estatura; /* Consultar el contenido ordenado por parametros */
SELECT * FROM Personas ORDER BY estatura DESC; /* Consultar el contenido ordenado descendente por parametros */
SELECT * FROM Personas ORDER BY estatura ASC, peso DESC; /* "" */
SELECT TOP 4 * FROM Personas; /* Devuelve un numero determinado de registros */
SELECT MAX(Españolas) FROM Personas WHERE id = 1; /* Devuelve el valor máximo de una columna */
SELECT MIN(Españolas) FROM Personas WHERE id = 1; /* Devuelve el valor mínimo de una columna */
SELECT COUNT(Españolas) FROM Personas WHERE id = 1; /* Devuelve el numero de filas que coinciden con las condiciones */
SELECT AVG(Españolas) FROM Personas WHERE id = 1; /* Devuelve el valor promedio de una columna */
SELECT SUM(Españolas) FROM Personas WHERE id = 1; /* Devuelve la suma de una columna numerica */
SELECT * FROM Personas WHERE nombre LIKE 'a%'; /* Muestra las personas cuyo nombre empieza por a */
SELECT * FROM Personas WHERE nombre LIKE '%a'; /* Muestra las personas cuyo nombre acaba por a */
SELECT * FROM Personas WHERE nombre LIKE '%a%'; /* Muestra las personas cuyo nombre contenga una a */
SELECT * FROM Personas WHERE nombre LIKE '_a%'; /* Muestra las personas cuyo nombre contenga una a en segunda posicion*/
SELECT * FROM Personas WHERE nombre LIKE 'a__%'; /* Muestra las personas cuyo nombre empieza por a y tiene al menos 3 caracteres*/
SELECT * FROM Personas WHERE nombre LIKE '[abc]%'; /* Muestra las personas cuyo nombre empieza por a, b o c */
SELECT * FROM Personas WHERE nombre LIKE '[!abc]%'; /* Muestra las personas cuyo nombre no empieza por a, b o c */
SELECT * FROM Personas WHERE nombre NOT LIKE '[abc]%'; /* Muestra las personas cuyo nombre no empieza por a, b o c */
SELECT * FROM Personas WHERE pais IN ('España', 'Cuba', 'Argentina'); /* Muestra las personas que estan en España, Cuba o Argentina */
SELECT * FROM Personas WHERE pais NOT IN ('España', 'Cuba', 'Argentina'); /* Muestra las personas que no estan en España, Cuba o Argentina */
SELECT * FROM Personas WHERE pais IN (SELECT pais FROM Ciudades); /* Muestra las personas que estan en los mismos paises que las ciudades */
SELECT * FROM Personas WHERE estatura BETWEEN 100 AND 200; /* Muestras las personas cuya estatura esta entre 100 y 200 */
SELECT * FROM Personas WHERE estatura NOT BETWEEN 100 AND 200; /* Muestras las personas cuya estatura no esta entre 100 y 200 */
SELECT * FROM Personas WHERE estatura BETWEEN 100 AND 200 AND id NOT IN (1, 2, 3); /* Muestras las personas cuya estatura esta entre 100 y 200 Y no muestre las personas cuyo id es..*/
SELECT * FROM Personas WHERE nombre BETWEEN "Alberto" AND "Manuel" ORDER BY nombre; /* Muestra las personas entre Alberto y Manuel ordenado por nombre */
SELECT * FROM Personas WHERE nombre NOT BETWEEN "Alberto" AND "Manuel" ORDER BY nombre; /* Muestra las personas que no estan entre Alberto y Manuel ordenado por nombre */
SELECT * FROM Personas WHERE fechanac BETWEEN #01/07/2020# AND #31/07/2020#; /* Muestra las personas cuya fecha de nacimiento esta entre... */
SELECT idpersona AS Id, edad AS Ed FROM Personas; /* Crear alias para las columnas idpersona y edad */

/* Relaciones 0:N / 1:N (uno a muchos) */
ALTER TABLE
  Personas
ADD
  (
    Ordenador int(5),
    FOREIGN KEY(Ordenador) REFERENCES Ordenadores(idordenador)
  );
  
/* Relaciones N:M (muchos a muchos) */

/* PENDIENTE: create table nm */

SELECT * 
FROM Personas p, Persona_Telefono pt, Telefonos t 
WHERE p.idpersonal = pt.idpersonas AND t.idtelefono = pt.idtelefono;

SELECT * 
FROM Personas p 
JOIN Persona_Telefono pt ON p.idpersonal = pt.idpersonas 
JOIN Telefonos t ON pt.idtelefono = t.idtelefono;


/* PENDIENTE: Backup */
BACKUP DATABASE Prueba TO DISK = 'Ubicacion destino'; /* Backup de la base de datos */
BACKUP DATABASE Prueba TO DISK = 'Ubicacion destino' WITH DIFFERENTIAL; /* Backup de las partes que han cambiado desde el ultimo backup de la base de datos */

