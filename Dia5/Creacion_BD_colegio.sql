CREATE DATABASE colegio;

use colegio;

create table if not exists alumnos(
	id					int				primary key		auto_increment,
    nombres				varchar(45),
    apellido_paterno	varchar(45),
    apellido_materno	varchar(45),
    correo				varchar(45)		unique,
    numero_emergencia	varchar(45)
);

create table if not exists niveles(
	id					int			primary key		auto_increment,
    nombre				varchar(45)	not null,
    seccion				varchar(45)	not null,
    ubicacion			varchar(45)
);
create table if not exists alumnos_niveles(
	id					int 		primary key		auto_increment,
    alumnos_id			int			not null,
    niveles_id			int			not null,
    fecha_cursada		year,
    foreign key(alumnos_id) references alumnos(id),
    foreign key(niveles_id) references niveles(id)
);