/* 
Ejercicio 1:
Crear la BD con el siguiente esquema, respetando las claves requeridas:
EMPLEADO( NOMBRE-EMPLEADO, DIRECCION, CIUDAD)
TRABAJA (NOMBRE-EMPLEADO, NOMBRE-EMPRESA, SUELDO)
EMPRESA (NOMBRE-EMPRESA, CIUDAD)
SUPERVISA (NOMBRE-EMPLEADO, NOMBRE-SUPERVISOR)
*/


CREATE DATABASE ejercicio1;


USE ejercicio1;



-- CREANDO LA TABLA EMPLEADO

CREATE TABLE empleado(
	nombre_empleado VARCHAR(50) NOT NULL,
    direccion VARCHAR(255) DEFAULT NULL,
    ciudad VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (nombre_empleado)
);



CREATE TABLE empresa(
	nombre_empresa VARCHAR(50),
    ciudad VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY (nombre_empresa)
);


CREATE TABLE trabaja(
	nombre_empleado VARCHAR(50),
    nombre_empresa VARCHAR(50),
    sueldo FLOAT,
    FOREIGN KEY (nombre_empleado) REFERENCES empleado(nombre_empleado),
    FOREIGN KEY (nombre_empresa) REFERENCES empresa(nombre_empresa)
);


CREATE TABLE supervisa(
	id INT AUTO_INCREMENT,
	nombre_empleado VARCHAR(50),
    nombre_supervisor VARCHAR(50),
    FOREIGN KEY (nombre_empleado) REFERENCES empleado(nombre_empleado),
    FOREIGN KEY (nombre_supervisor) REFERENCES empleado(nombre_empleado),
    PRIMARY KEY (id)
);









































