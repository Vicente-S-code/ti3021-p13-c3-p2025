import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

with oracledb.connect(user = username, 
                      password = password, 
                      dsn = dsn
                      ) as connection:
    with connection.cursor() as cursor:
        sql = "select sysdate from dual"
        for row in cursor.execute(sql):
         for column in row:
          print(column)

def get_connection():
   return oracledb.connect(iuser=username, password=password, dsn=dsn)

def create_schema(query):  
        try:
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    print(f"Tabla creada \n {query}")
        except oracledb.DatabaseError as error:
            print(f"No se pudo crear la tabla {error}")
           
        tables = [
        (  
            "CREATE TABLES"      
            "USUARIO ("
            "id integer primary key,"
            "nombre varchar(200),"
            "rut varchar(10),"
            "correoinstitucional varchar(200);"  
             ")"
        ),
        (
            "CREATE TABLES"
            "ESTUDIANTE ("
            "id_estudiante integer primary key,"
            "carrea varchar(100),"
            "anioingreso date"
            ");"
        ),
        (
            "CREATE TABLE"
            "DOCENTE("
            "id_docente interger primary key,"
            "especialidad varchar(100)"
            ");"
        ),
        (
            "CREATE TABLE"
            "INVESTIGADOR("
            "id_investigador interger primary key,"
            "lineadeinvestigacion varchar (100)"
            ");"
        ),
        (
            "CREATE TABLE"
            "LIBRO("
            "id_libro interger primary key"
            "nombre varchar(100),"
            "codlibro varchar(20),"
            "disponible boolean,"
            "id_estudiantefk interger,"
            "foreing key id_estudiantefk references ESTUDIANTE(id_estudiante),"
            "id_docentefk interger," 
            "foreing key id_docentefk references DOCENTE(id_docente)"
            ");"       
        ),
        
         ]
        
        def create_usuario(
                id,
                nombre,
                rut,
                correoinstitucional
        ):
            sql = (
                "INSER INTO USUARIO (id, nombre, rut, correoinstitucional)"
                "VALUES (:id, :nombre, :rut, :correoinstitucional)"
            )

            parametros = {
                "id": id,
                "nombre": nombre,
                "rut": rut,
                "correoinstitucional": correoinstitucional
            }
        from datetime import datetime
        def create_estudiante(
                id_estudiante,
                carrera,
                anioingreso
        ):
            sql = (
                "INSER INTO ESTUDIANTE(id_estudiante, carrea, anioingreso)"
                "VALUES (:id_estudiante, :carrera, :anioingreso)"
            )

            parametros = {
                "id_estudiante": id_estudiante,
                "carrera": carrera,
                "anioingreso": datetime.strptime(anioingreso, '%d-%m-%Y')
            }

        def create_docente(
                id_codente,
                especialidad
        ):
            pass

        def create_investigador(
                id_investigador,
                lineadeinvestigacion
        ):
            pass

        def create_libro(
                id_libro,
                nombre,
                codlibro,
                disponible,
                id_estudiantefk,
                id_docentefk
        ):
            pass