/*

-- Nombre
-- Atributos: TIPO DE DATO (sql) (CONSTRAINT)

CREATE TABLE        
USUARIO
id interger primary key,
nombre varchar(200),
rut varchar(10),
correoinstitucional varchar(200);

CREATE TABLE
ESTUDIANTE
id_estudiate interger primary key,
carrera vachar(200),
anioingreso date;

CREATE TABLE
DOCENTE
id_docente interger primary key,
especialidad varchar(200);

CREATE TABLE
INVESTIGADOR
id_investigador interger primary key,
lineadeinvestigacion varchar(200);

CREATE TABLE
LIBRO
id_libro interger primary key,
nombre varchar(200),
codlibro varchar(30),
disponible boolean; --libro disponible o libro no disponible