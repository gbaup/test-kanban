# Query #

```sql
SELECT
  fecha_renta,
  titulo,
  genero,
  cantidad_pagada,
  RANK() OVER(PARTITION BY genero ORDER BY cantidad_pagada DESC)
FROM pelicula
JOIN alquiler
  ON alquiler.pelicula_id = pelicula.id;
```

# Solución #

'SELECT' indica las columnas que se desean mostrar en el resultado de la consulta. En este caso, se desean mostrar las columnas 'fecha_renta', 'titulo', 'genero' y 'cantidad_pagada'.

'FROM' indica las tablas que se desean consultar. 

'JOIN' se utiliza para combinar las tablas 'pelicula' y 'alquiler' a través de la columna 'pelicula_id' de la tabla 'alquiler' y la columna 'id' de la tabla 'pelicula'.

En resumen, vamos a ver una lista de películas alquiladas, con su fecha de renta, título, género, cantidad pagada y un ranking que indica la posición de cada película dentro de su género según la cantidad pagada, ordenado de forma descendiente.


# Query tabla clientes #

```sql
CREATE TABLE Clientes (
cliente_id INT PRIMARY KEY,
nombre_cliente VARCHAR(255),
correo_cliente VARCHAR(255),
fecha_registro DATE
);
```

```sql
SELECT
pelicula.titulo,
pelicula.genero,
alquiler.fecha_renta,
alquiler.cantidad_pagada,
Clientes.nombre_cliente,
FROM pelicula
JOIN alquiler ON alquiler.pelicula_id = pelicula.id
JOIN Clientes ON alquiler.cliente_id = Clientes.cliente_id
ORDER BY pelicula.titulo, Clientes.nombre_cliente;
```
