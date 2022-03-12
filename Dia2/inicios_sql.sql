
CREATE DATABASE prueba;
use prueba;

create table clientes(
	id			    int				auto_increment primary key,
    nombre		    varchar(50),
    documento 	    varchar(10) 	unique,
    tipo_documento  enum('C.E.', 'DNI', 'RUC', 'PASAPORTE', 'C.M.', 'OTRO'),
    estado		    bool
);
