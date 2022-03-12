use prueba;

create table vacunas (
	id			int				primary key		auto_increment,
    nombre		varchar(50)		unique			not null,
    estado  	boolean			default true,
    fecha_vencimiento date,
    procedencia enum('USA', 'CHINA', 'RUSIA', 'UK'),
    lote		varchar(10)
);

create table vacunatorio(
	id			int				primary key		auto_increment,
    nombre		varchar(100)	not null,
    latitud		float,
    longitud		float,
    direccion	varchar(200),
    horario_atencion	varchar(100),
    vacuna_id	int,
    foreign key(vacuna_id) references vacunas(id)
);

--	DDL	Data Definition Language 	>	se usa para la definicion de donde se almacenaran los datos en mi base de datos
--	Para renombrar una tabla con un nuevo nombre
--	RENAME TABLE valor_antiguo TO nuevo_valor
--	CREATE TABLES | CREATE DATABASE
--	DROP elimina la tabla y su contenido a diferencia del DELETE que solo eliminar el contenido
--	DROP TABLE vacunatorio
--	DROP DATABASE prueba

--	Eliminacion de la columna de la tabla
--	ALTER TABLE vacunatorios drop column latitud;

rename table vacunatorio to vacunatorios;

--	Agregar una columna, (after agrega la columna despues de la columna horario_atencion)
ALTER TABLE vacunatorio ADD COLUMN imagen varchar(100) default 'imagen.png' AFTER horario_atencion;

--	RENAME COLUMN 	>	renombra la columna
ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;

--	MODIFY COLUMN	>	renombra la columna
--	NO SE PUEDE CAMBIAR EL TIPO DE DATO SI YA HAY INFORMACION EN ESA COLUMNA Y NO CORRESPONDE CON EL NUEVO TIPO DE DATO
--	ALTER TABLE vacunatorios MODIFY COLUMN imagen INT UNIQUE NOT NULL;

--	Muesta las definicion de la tabla
DESC CLIENTES;


