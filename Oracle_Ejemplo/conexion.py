import oracledb
import os
from dotenv import load_dotenv
from typing import Optional
from datetime import datetime
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

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
           
def create_all_tables():
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
    for query in tables:
        create_schema(query)

def create_usuario(
        id: int,
        nombre: str,
        rut: str,
        correoinstitucional : str
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
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} /n {sql} /n {parametros} " )

def create_estudiante(
        id_estudiante: int,
        carrera: str,
        anioingreso : str
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

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} /n {sql} /n {parametros} " )

def create_docente(
        id_docente  : int,
        especialidad    : str
):
    sql = (
        "INSER INTO DOCENTE(id_docente, especialidad)"
        "VALUES (:id_docente, :especialidad)"
        ) 

    parametros = {
        "id_docente": id_docente,
        "especialidad": especialidad
    }  

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} /n {sql} /n {parametros} " )  

def create_investigador(
        id_investigador : int,
        lineadeinvestigacion    : str
):
    sql = (
        "INSER INTO INVESTIGADOR(id_investigador, lineadeinvestigacion)"
        "VALUES (:id_investigador, :lineadeinvestigacion)"
    )

    parametros = {
        "id_investigador": id_investigador,
        "lineadeinestigacion": lineadeinvestigacion
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} /n {sql} /n {parametros} " )

def create_libro(
        id_libro    : int,
        nombre    : str,
        codlibro    : str,
        disponible  : bool,
        id_estudiantefk,
        id_docentefk
):
    sql = (
        "INSER INTO LIBRO(id_libro, nombre, codlibro, disponible, id_estudiantefk, id_docentefk)"
        "VALUES(:id_libro, :nombre, :codlibro, :disponible, :id_estudiantefk, :id_docentefk)"
    )

    parametros = {
        "id_libro": id_libro,
        "nombre": nombre,
        "codlibro": codlibro,
        "disponible": disponible,
        "id_estudiantefk": id_estudiantefk,
        "id_docentefk": id_docentefk
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} /n {sql} /n {parametros} " )

# READ - LECTURA DE DATOS

def read_usuarios():
            sql = (
                "SELECT * FROM USUARIOS WHERE id = :id"
            )
            parametros = {"id" : id}
def read_usuario_by_id(id : int):
            sql = (
                "SELECT * FROM USUARIOS WHERE id = :id"
            )
            parametros = {"id" : id}

            try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql, parametros)
                        resultado = cursor.execute(sql, parametros)
                        if len(resultado) == 0:
                            return print(f"No se encontraron usuarios con ese ID{id}")
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} /n {parametros} " )

def read_estudiantes():
            sql = (
                "SELECT * FROM ESTUDIANTE"
            )
            
            try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_estudiante_by_id(id_estudiante: int):
            sql = (
                "SELECT * FROM ESTUDIANTE WHERE id_estudiante = :id_estudiante"
            )
            try: 
                 with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_docentes():
            sql = (
                "SELECT * FROM DOCENTE"
            )
            try:
                  with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_docente_by_id(id_docente: int):
            sql = (
                "SELECT * FROM DOCENTE WHERE id_docente = :id_docente"
            )
            try:
                   with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_investigadores():
            sql = (
                "SELECT * FROM INVESTIGADOR"
            )
            try:
                   with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_investigador_by_id(id_investigador : int):
    sql = (
    "SELECT * FROM INVESTIGADOR WHERE id_investigador = :id_investigador"
    )
    try:
        with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
    except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )
            
def read_libro():
    sql = (
    "SELECT * FROM LIBRO"
    )
    try:
            with get_connection() as connection:
                with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo leer el dato {error} /n {sql} " )

def read_libro_by_id(id_libro : int):  
    sql = (
    "SELECT * FROM LIBRO WHERE id_libro = :id_libro"
    )
    try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        resultado = cursor.execute(sql)
                        for fila in resultado:
                            print(fila)
    except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} /n {sql} " )

# UPDATE - ACTUALIZACION DE DATOS
def update_usuario(
    id: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correoinstitucional: Optional[str] = None
):
    modificaciones = []
    parametros = {"id": id}

    if rut is not None:
        modificaciones.append("rut = :rut")
        parametros["rut"] = rut
    if nombre is not None:
        modificaciones.append("nombre = :nombre")
        parametros["nombre"] = nombre
    if correoinstitucional is not None:
        modificaciones.append("correoinstitucional = :correoinstitucional")
        parametros["correoinstitucional"] = correoinstitucional
    if not modificaciones:
        print("No hay modificaciones para realizar.")
    
    sql = f"UPDATE USUARIO SET {', '.join(modificaciones)} WHERE id = :id"

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, parametros)
        connection.commit()
        print(f"Dato con ID {id} actualizado correctamente.")

#DELETE - ELIMINACION DE DATOS
def delete_usuario(id: int):
    sql = "DELETE FROM USUARIO WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id} eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
        error = e
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )

def delete_estudiante(id_estudiante: int):
    sql = "DELETE FROM ESTUDIANTE WHERE id_estudiante = :id_estudiante"
    parametros = {"id_estudiante": id_estudiante}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_estudiante} eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
        error = e
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )

def delete_docente(id_docente: int):
    sql = "DELETE FROM DOCENTE WHERE id_docente = :id_docente"
    parametros = {"id_docente": id_docente}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_docente} eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
        error = e
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )

def delete_investigador(id_investigador: int):
    sql = "DELETE FROM INVESTIGADOR WHERE id_investigador = :id_investigador"
    parametros = {"id_investigador": id_investigador}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_investigador} eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
        error = e
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )

def delete_libro(id_libro: int):
    sql = "DELETE FROM LIBRO WHERE id_libro = :id_libro"
    parametros = {"id_libro": id_libro}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_libro} eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
        error = e
        print(f"No se pudo eliminar el dato {error} /n {sql} /n {parametros} " )
    
def main():
    pass
        
if __name__ == "__main__":
    main()
         
