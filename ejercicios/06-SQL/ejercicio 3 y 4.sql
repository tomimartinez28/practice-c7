CREATE DATABASE productos;

USE productos;

-- 1)

CREATE TABLE producto(
	codigo_producto INT NOT NULL,
    codigo_fabricante INT NOT NULL,
    nombre VARCHAR(100),
    PRIMARY KEY (codigo_producto)
);

CREATE TABLE fabricante(
	codigo_fabricante INT NOT NULL,
    nombre VARCHAR(100),
    PRIMARY KEY (codigo_fabricante)
);


-- agregar columna precio en la tabla producto
ALTER TABLE producto 
ADD precio FLOAT;



-- 1) Lista el nombre de todos los productos que hay en la tabla producto

SELECT nombre FROM producto;

-- 2) Lista todas las columnas de la tabla producto.

SHOW COLUMNS FROM producto;
DESCRIBE producto;

-- 3) Lista el nombre de los productos y el precio en USD.

SELECT nombre AS Nombre_Producto, precio AS precio_dolares FROM producto;


-- 4) Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los nombres a mayúscula.

SELECT UPPER(nombre) AS nombre_mayuscula, precio FROM producto;

-- 5) Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el valor del precio.

SELECT nombre, ROUND(precio) FROM producto;

-- 6) Lista el código de los fabricantes que tienen productos en la tabla producto.

SELECT codigo_fabricante FROM producto;


-- 7) Lista el código de los fabricantes que tienen productos en la tabla producto, eliminando los códigos que aparecen repetidos.
SELECT DISTINCT codigo_fabricante FROM producto;

-- 8) Lista los nombres de los fabricantes ordenados de forma ascendente.
SELECT nombre 
FROM fabricante
ORDER BY nombre;

-- 9) Lista los nombres de los productos ordenados en primer lugar por el nombre de forma ascendente y en segundo lugar por el precio de forma descendente.


SELECT nombre, precio
FROM producto
ORDER BY nombre, precio DESC;



-- 10)Devuelve una lista con las 5 primeras filas de la tabla fabricante.

SELECT * FROM fabricante LIMIT 2;

-- 11) Lista el nombre de todos los productos del fabricante cuyo código de fabricante es igual a 2.

SELECT *
FROM producto
WHERE codigo_fabricante = 2;

-- 12) Lista el nombre de los productos que tienen un precio menor o igual a 120USD
SELECT nombre 
FROM producto
WHERE precio <= 120;


-- 13) Devuelve todos los productos del fabricante Lenovo. (Sin utilizar INNER JOIN).

SELECT *
FROM producto
WHERE codigo_fabricante = (SELECT codigo_fabricante FROM fabricante WHERE nombre='Lenovo');



-- CON INNER JOIN

SELECT *
FROM producto AS p
INNER JOIN fabricante AS f
ON p.codigo_fabricante = f.codigo_fabricante
WHERE f.nombre = 'Lenovo';




















