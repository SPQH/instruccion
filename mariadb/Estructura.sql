/* Acceso a base de datos:  sudo mariadb -u root -p */

/* Creación de base de datos */
CREATE DATABASE Test

/* Visualización y elección de base de datos */
SHOW DATABASES;
USE Test;

/* Creación de tablas */
CREATE TABLE Persona (
    id INT(11) NOT NULL AUTO_INCREMENT UNIQUE,
    nombre VARCHAR(20) NOT NULL,
    apellido1 VARCHAR(20) NOT NULL.
    annoNacimiento INT,
    estatura INT, 
    peso INT,
    nacionalidad VARCHAR(200),
    color VARCHAR(30),
    PRIMARY KEY (id));

/* Modificación de tablas */
ALTER TABLE Personas ADD Sexo BIT(1); /* Añadir nuevo campo a tabla */
ALTER TABLE Personas CHANGE annoNacimiento nacimiento INT; /* Cambiar el nombre de annoNacimiento a nacimiento */
ALTER TABLE Personas CHANGE nombre nombre VARCHAR(50); /* Cambiar el tipo de dato, en este caso aumentar longitud de VARCHAR */

/* Visualización de estructura */
SHOW TABLES;
DESCRIBE Personas;

/* Insertar un registro en una tabla */
INSERT INTO Personas(nombre, apellido1, nacimiento, estatura, peso, nacionalidad, color) 
values("Alfredo", "García", 1990, 1.8, 74, "España", "Azul");

/* Insertar múltiples registros en una tabla en un solo comando */
INSERT INTO Personas
    (nombre, apellido1, nacimiento)
VALUES
    ("Juan", "Salgado", 1998),
    ("Elena", "López", 1994),
    ("Estefanía", "Díaz", 1991),
    ("Carlos", "García", 1991),
    ("Alberto", "Murillo", 1991),
    ("Javier", "Delgado", 1991);
    

