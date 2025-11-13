/*

-- Nombre
-- Atributos: TIPO DE DATO (sql) (CONSTRAINT)

USUARIO
id interger primary key,
nombre varchar(200),
rut varchar(10),
correoinstitucional varchar(200);

ESTUDIANTE
id_estudiate interger primary key,
carrera vachar(200),
anioingreso date;

DOCENTE
id_docente interger primary key,
especialidad varchar(200);

INVESTIGADOR
id_investigador interger primary key,
lineadeinvestigacion varchar(200);

LIBRO
id_libro interger primary key,
nombre varchar(200),
codlibro varchar(30),
disponible boolean; --libro disponible o libro no disponible