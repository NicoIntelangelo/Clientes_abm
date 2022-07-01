CREATE SCHEMA clientes_db ;
USE clientes_db;

CREATE TABLE 
`clientes`
(
  `id_c` int(10) NOT NULL AUTO_INCREMENT,
  `nombre_c` text (40) NOT NULL,
  `apellido_c` text (40) NOT NULL,
  `cuit_cuil_c` bigint(12) NOT NULL,
  `telefono_c` bigint (14)NOT NULL DEFAULT 0,
  primary key (id_c)
  );