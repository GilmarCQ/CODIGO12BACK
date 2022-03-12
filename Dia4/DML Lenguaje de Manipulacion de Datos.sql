use prueba;

insert into clientes (nombre, documento, tipo_documento, estado) values
	('Gilmar', '72690553', 'DNI', true);
insert into clientes (nombre, documento, tipo_documento, estado) values
	('gilmar', '72690554', 'DNI', true);

insert into clientes (nombre, documento, tipo_documento, estado) values
	('Estefani', '15944587', 'DNI', true),
    ('Fabian', '45458777', 'RUC', false);
    
select * from clientes;

select * from clientes where tipo_documento = 'DNI' and estado = true;
select * from clientes where nombre like '%Gil%';

update clientes set nombre = 'Alfredo' where documento = '72690554';

--	modo seguro >	es el modo que nos impide hacer actualizaciones (UPDATE) y eliminaciones (DELETE)
--	sin usar una columna que sea indice o PK
--	Para descativar el modo seguro 
SET SQL_SAFE_UPDATES = false;
