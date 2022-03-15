select * from niveles;
insert into alumnos_niveles (alumnos_id, niveles_id, fecha_cursada) VALUES
					(1, 1, 2000),
					(1, 3, 2001),
					(1, 6, 2002),
					(1, 9, 2003),
					(1, 12, 2004),
					(1, 14, 2005),
					(2, 1, 2000),
					(2, 3, 2001),
					(2, 6, 2002),
					(2, 9, 2003),
					(2, 13, 2004),
					(2, 15, 2005),
					(3, 11, 2002),
					(3, 15, 2002);

select * from alumnos as al
inner join alumnos_niveles as al_niv
on al.id = al_niv.alumnos_id
inner join niveles as niv
on al_niv.niveles_id = niv.id
group by al.nombres;

select * from alumnos
where correo like '%gmail.com';

select al.nombres, al.apellido_paterno, al.apellido_materno, al_niv.fecha_cursada from alumnos as al
inner join alumnos_niveles as al_niv
on al.id = al_niv.alumnos_id
where al_niv.fecha_cursada = 2002;

select * from niveles
where ubicacion like '%Sotano%' or  ubicacion like '%Segundo Piso%';

select niv.nombre, niv.seccion from alumnos as al
inner join alumnos_niveles as al_niv
on al.id = al_niv.alumnos_id
inner join niveles as niv
on al_niv.niveles_id = niv.id
where al_niv.fecha_cursada = 2003
group by (niv.id);

--	5.	mostrar todos los alumnos del 5 A
--	6.	mostrar todos los correos de los alumnos del 1 B

select alumnos.nombres, alumnos.apellido_paterno, alumnos.apellido_materno from alumnos
inner join alumnos_niveles as al_niv
on alumnos.id = al_niv.alumnos_id
inner join niveles
on al_niv.niveles_id = niveles.id
where niveles.nombre = 'Quinto' and niveles.seccion = 'A';

select alumnos.correo, alumnos.nombres, alumnos.apellido_paterno, alumnos.apellido_materno from alumnos
inner join alumnos_niveles as al_niv
on alumnos.id = al_niv.alumnos_id
inner join niveles
on al_niv.niveles_id = niveles.id
where niveles.nombre = 'Primero' and niveles.seccion = 'A';



