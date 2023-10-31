-- EJERCICIO 2


-- 1) Modificar la base de datos para registrar que `Luis Torres' se mudó a `Málaga'.

-- leyendo los datos
SELECT * FROM empleado;

-- actualiza un valor
UPDATE empleado 
SET ciudad = 'Malaga' 
WHERE nombre_empleado = 'Luis Torres';

UPDATE empleado 
SET direccion = 'Calle falsa 123' 
WHERE nombre_empleado = 'Luis Torres';



-- 2) Dar a todos los empleados de la empresa `Amazon' un 10 % de aumento.

SELECT * FROM trabaja;

UPDATE trabaja
SET sueldo = sueldo * 1.1
WHERE nombre_empresa = 'Amazon';

-- 3) Dar a todos los supervisores de la empresa `Google' un 10 % de aumento.

UPDATE trabaja
SET sueldo = sueldo * 1.1
WHERE nombre_empresa = 'Google'
AND (nombre_empleado IN (SELECT nombre_supervisor FROM supervisa));

-- subconsulta
SELECT nombre_supervisor FROM supervisa;



/* 4) Dar a todos los supervisores de la empresa `Google' un 10 % de aumento, a
menos que su salario supere los $1900, en ese caso, dar sólo un 3 % de
aumento.  */

UPDATE trabaja
SET sueldo = 
	CASE
		WHEN sueldo <= 1900 THEN sueldo * 1.1
		ELSE sueldo * 1.03
	END
WHERE (nombre_empresa = 'Google')
AND (nombre_empleado IN (SELECT nombre_supervisor FROM supervisa));


    

        










