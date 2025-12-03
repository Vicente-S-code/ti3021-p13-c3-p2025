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
    return oracledb.connect(user=username, password=password, dsn=dsn)

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

    """
    CREATE TABLE USUARIO (
        id NUMBER PRIMARY KEY,
        nombre VARCHAR2(200),
        rut VARCHAR2(10),
        correoinstitucional VARCHAR2(200)
    )
    """,

    """
    CREATE TABLE ESTUDIANTE (
        id_estudiante NUMBER PRIMARY KEY,
        carrera VARCHAR2(100),
        anioingreso DATE
    )
    """,

    """
    CREATE TABLE DOCENTE (
        id_docente NUMBER PRIMARY KEY,
        especialidad VARCHAR2(100)
    )
    """,

    """
    CREATE TABLE INVESTIGADOR (
        id_investigador NUMBER PRIMARY KEY,
        lineadeinvestigacion VARCHAR2(100)
    )
    """,

    """
    
    CREATE TABLE LIBRO (
        id_libro NUMBER PRIMARY KEY,
        nombre VARCHAR2(100),
        codlibro VARCHAR2(20),
        disponible NUMBER(1), 
        id_estudiantefk NUMBER,
        id_docentefk NUMBER,
        FOREIGN KEY (id_estudiantefk) REFERENCES ESTUDIANTE(id_estudiante),
        FOREIGN KEY (id_docentefk) REFERENCES DOCENTE(id_docente)
    
    )
    """,
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
        "INSERT INTO USUARIO (id, nombre, rut, correoinstitucional)"
        "VALUES (:id, :nombre, :rut, :correoinstitucional)"
    )

    parametros = {
        "id": int(id),
        "nombre": nombre,
        "rut": rut,
        "correoinstitucional": correoinstitucional
    }
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                connection.commit()
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} \n {sql} \n {parametros} " )

def create_estudiante(
        id_estudiante: int,
        carrera: str,
        anioingreso : str
):
    sql = (
        "INSERT INTO ESTUDIANTE(id_estudiante, carrera, anioingreso)"
        "VALUES (:id_estudiante, :carrera, :anioingreso)"
    )

    try:
        anioingreso_date = datetime.strptime(anioingreso, '%d-%m-%Y')
    except ValueError:
        print("Error: El formato de fecha debe ser dd-mm-yyyy.")
        return

    parametros = {
        "id_estudiante": int(id_estudiante),
        "carrera": carrera,
        "anioingreso": anioingreso_date
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                connection.commit()
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} \n {sql} \n {parametros} " )

def create_docente(
        id_docente  : int,
        especialidad    : str
):
    sql = (
        "INSERT INTO DOCENTE(id_docente, especialidad)"
        "VALUES (:id_docente, :especialidad)"
        ) 

    parametros = {
        "id_docente": int(id_docente),
        "especialidad": especialidad
    }  

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                connection.commit()
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} \n {sql} \n {parametros} " )  

def create_investigador(
        id_investigador : int,
        lineadeinvestigacion    : str
):
    sql = (
        "INSERT INTO INVESTIGADOR(id_investigador, lineadeinvestigacion)"
        "VALUES (:id_investigador, :lineadeinvestigacion)"
    )

    parametros = {
        "id_investigador": int(id_investigador),
        "lineadeinvestigacion": lineadeinvestigacion 
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
                connection.commit()
                print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} \n {sql} \n {parametros} " )

def create_libro(
        id_libro    : int,
        nombre    : str,
        codlibro    : str,
        disponible  : bool,
        id_estudiantefk,
        id_docentefk
):
    sql = (
        "INSERT INTO LIBRO(id_libro, nombre, codlibro, disponible, id_estudiantefk, id_docentefk)"
        "VALUES(:id_libro, :nombre, :codlibro, :disponible, :id_estudiantefk, :id_docentefk)"
    )
    
    disponible_db = 1 if str(disponible).lower() in ('true', '1') else 0

    parametros = {
        "id_libro": int(id_libro),
        "nombre": nombre,
        "codlibro": codlibro,
        "disponible": disponible_db,
        "id_estudiantefk": int(id_estudiantefk) if id_estudiantefk else None,
        "id_docentefk": int(id_docentefk) if id_docentefk else None
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserccion de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato {error} \n {sql} \n {parametros} " )

def read_usuarios():
            sql = (
                "SELECT * FROM USUARIO"
            )
            
            try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        cursor.execute(sql)
                        resultado = cursor.fetchall()
                        for fila in resultado:
                            print(fila)
                        if not resultado:
                             print("No se encontraron usuarios.")
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} " )

def read_usuario_by_id(id : int):
            sql = (
                "SELECT * FROM USUARIO WHERE id = :id" 
            )
            parametros = {"id" : int(id)}

            try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql, parametros)
                        cursor.execute(sql, parametros) 
                        resultado = cursor.fetchall() 
                        if not resultado:
                            return print(f"No se encontraron usuarios con ese ID: {id}")
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} \n {parametros} " )

def read_estudiantes():
            sql = (
                "SELECT * FROM ESTUDIANTE"
            )
            
            try:
                with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        cursor.execute(sql)
                        resultado = cursor.fetchall()
                        for fila in resultado:
                            print(fila)
                        if not resultado:
                             print("No se encontraron estudiantes.")
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} " )

def read_estudiante_by_id(id_estudiante: int):
            sql = (
                "SELECT * FROM ESTUDIANTE WHERE id_estudiante = :id_estudiante"
            )
            parametros = {"id_estudiante" : int(id_estudiante)} 
            try: 
                 with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql, parametros)
                        cursor.execute(sql, parametros) 
                        resultado = cursor.fetchall()
                        if not resultado:
                            return print(f"No se encontraron estudiantes con ese ID: {id_estudiante}") 
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} \n {parametros} " )

def read_docentes():
            sql = (
                "SELECT * FROM DOCENTE"
            )
            try:
                 with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        cursor.execute(sql)
                        resultado = cursor.fetchall()
                        for fila in resultado:
                            print(fila)
                        if not resultado:
                             print("No se encontraron docentes.")
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} " )

def read_docente_by_id(id_docente: int):
            sql = (
                "SELECT * FROM DOCENTE WHERE id_docente = :id_docente"
            )
            parametros = {"id_docente" : int(id_docente)} 
            try:
                 with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql, parametros)
                        cursor.execute(sql, parametros) 
                        resultado = cursor.fetchall()
                        if not resultado:
                            return print(f"No se encontraron docentes con ese ID: {id_docente}") 
                        for fila in resultado:
                            print(fila)
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} \n {parametros} " )

def read_investigadores():
            sql = (
                "SELECT * FROM INVESTIGADOR"
            )
            try:
                 with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql)
                        cursor.execute(sql)
                        resultado = cursor.fetchall()
                        for fila in resultado:
                            print(fila)
                        if not resultado:
                             print("No se encontraron investigadores.")
            except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} " )

def read_investigador_by_id(id_investigador : int):
    sql = (
    "SELECT * FROM INVESTIGADOR WHERE id_investigador = :id_investigador"
    )
    parametros = {"id_investigador" : int(id_investigador)} 
    try:
        with get_connection() as connection:
                    with connection.cursor() as cursor:
                        print(sql, parametros)
                        cursor.execute(sql, parametros) 
                        resultado = cursor.fetchall() 
                        if not resultado:
                            return print(f"No se encontraron investigadores con ese ID: {id_investigador}")
                        for fila in resultado:
                            print(fila)
    except oracledb.DatabaseError as error:
                        print(f"No se pudo leer el dato {error} \n {sql} \n {parametros} " )
            
def read_libro():
    sql = (
    "SELECT * FROM LIBRO"
    )
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                cursor.execute(sql)
                resultado = cursor.fetchall()
                for fila in resultado:
                    print(fila)
                if not resultado:
                     print("No se encontraron libros.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo leer el dato {error} \n {sql} " )

def read_libro_by_id(id_libro : int):  
    sql = (
    "SELECT * FROM LIBRO WHERE id_libro = :id_libro"
    )
    parametros = {"id_libro" : int(id_libro)} 
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                cursor.execute(sql, parametros) 
                resultado = cursor.fetchall() 
                if not resultado:
                    return print(f"No se encontraron libros con ese ID: {id_libro}")
                for fila in resultado:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo leer el dato {error} \n {sql} \n {parametros} " )

def update_usuario(
    id: int,
    nombre: Optional[str] = None,
    rut: Optional[str] = None,
    correoinstitucional: Optional[str] = None
):
    modificaciones = []
    parametros = {"id": int(id)}

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
        return 
    
    sql = f"UPDATE USUARIO SET {', '.join(modificaciones)} WHERE id = :id"
    
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id} actualizado correctamente.")
    except oracledb.DatabaseError as error:
        print(f"No se pudo actualizar el dato {error} \n {sql} \n {parametros} " )


def delete_usuario(id: int):
    sql = "DELETE FROM USUARIO WHERE id = :id"
    parametros = {"id": int(id)}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id} eliminado correctamente.")
    except oracledb.DatabaseError as error: 
        print(f"No se pudo eliminar el dato {error} \n {sql} \n {parametros} " )

def delete_estudiante(id_estudiante: int):
    sql = "DELETE FROM ESTUDIANTE WHERE id_estudiante = :id_estudiante"
    parametros = {"id_estudiante": int(id_estudiante)}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_estudiante} eliminado correctamente.")
    except oracledb.DatabaseError as error: 
        print(f"No se pudo eliminar el dato {error} \n {sql} \n {parametros} " )

def delete_docente(id_docente: int):
    sql = "DELETE FROM DOCENTE WHERE id_docente = :id_docente"
    parametros = {"id_docente": int(id_docente)}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_docente} eliminado correctamente.")
    except oracledb.DatabaseError as error: 
        print(f"No se pudo eliminar el dato {error} \n {sql} \n {parametros} " )

def delete_investigador(id_investigador: int):
    sql = "DELETE FROM INVESTIGADOR WHERE id_investigador = :id_investigador"
    parametros = {"id_investigador": int(id_investigador)}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_investigador} eliminado correctamente.")
    except oracledb.DatabaseError as error: 
        print(f"No se pudo eliminar el dato {error} \n {sql} \n {parametros} " )

def delete_libro(id_libro: int):
    sql = "DELETE FROM LIBRO WHERE id_libro = :id_libro"
    parametros = {"id_libro": int(id_libro)}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print(f"Dato con ID {id_libro} eliminado correctamente.")
    except oracledb.DatabaseError as error: 
        print(f"No se pudo eliminar el dato {error} \n {sql} \n {parametros} " )

def menu_usuarios():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |      Menu: Usuarios            |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Modificar un dato             |
                | 5. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-5, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            try:
                id = int(input("Ingrese id del usuario: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            nombre = input("Ingrese nombre del usuario: ")
            rut = input("Ingrese rut del usuario: ")
            correoinstitucional = input("Ingrese correo institucional del usuario: ")
            create_usuario(id, nombre, rut, correoinstitucional)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_usuarios()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            try:
                id = int(input("Ingrese id del usuario: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            read_usuario_by_id(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Modificar un dato")
            try:
                id = int(input("Ingrese id del usuario a modificar: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            print("[Sólo ingrese los datos a modificar del usuario]")
            nombre = input("Ingrese nombre del usuario (opcional): ")
            rut = input("Ingrese rut del usuario (opcional): ")
            correoinstitucional = input("Ingrese correo institucional del usuario (opcional): ")
            if len(nombre.strip()) == 0: nombre = None
            if len(rut.strip()) == 0: rut = None
            if len(correoinstitucional.strip()) == 0: correoinstitucional = None
            update_usuario(id, nombre, rut, correoinstitucional)
            input("Ingrese ENTER para continuar...")
        elif opcion == "5":
            os.system("cls")
            print("5. Eliminar un dato")
            try:
                id = int(input("Ingrese id del usuario a eliminar: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            delete_usuario(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def menu_estudiantes():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |      Menu: Estudiantes          |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            try:
                id_estudiante = int(input("Ingrese id del estudiante: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            carrera = input("Ingrese carrera del estudiante: ")
            anioingreso = input("Ingrese año de ingreso del estudiante (dd-mm-yyyy): ")
            create_estudiante(id_estudiante, carrera, anioingreso)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_estudiantes()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            try:
                id_estudiante = int(input("Ingrese id del estudiante: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            read_estudiante_by_id(id_estudiante)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Eliminar un dato")
            try:
                id_estudiante = int(input("Ingrese id del estudiante a eliminar: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            delete_estudiante(id_estudiante)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def menu_docentes():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |      Menu: Docentes            |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            try:
                id_docente = int(input("Ingrese id del docente: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            especialidad = input("Ingrese especialidad del docente: ")
            create_docente(id_docente, especialidad)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_docentes()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            try:
                id_docente = int(input("Ingrese id del docente: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            read_docente_by_id(id_docente)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Eliminar un dato")
            try:
                id_docente = int(input("Ingrese id del docente a eliminar: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue 
            delete_docente(id_docente)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def menu_investigadores():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |      Menu: Investigadores      |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            try:
                id_investigador = int(input("Ingrese id del investigador: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            lineadeinvestigacion = input("Ingrese línea de investigación del investigador: ")
            create_investigador(id_investigador, lineadeinvestigacion)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_investigadores()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            try:
                id_investigador = int(input("Ingrese id del investigador: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            read_investigador_by_id(id_investigador)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Eliminar un dato")
            try:
                id_investigador = int(input("Ingrese id del investigador a eliminar: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue 
            delete_investigador(id_investigador)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def menu_libros():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |      Menu: Libros              |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            try:
                id_libro = int(input("Ingrese id del libro: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            nombre = input("Ingrese nombre del libro: ")
            codlibro = input("Ingrese código del libro: ")
            disponible = input("Ingrese disponibilidad del libro (true/false/1/0): ")
            
            id_estudiantefk_str = input("Ingrese id del estudiante (opcional, debe existir): ")
            id_docentefk_str = input("Ingrese id del docente (opcional, debe existir): ")
            
            id_estudiantefk = id_estudiantefk_str if len(id_estudiantefk_str.strip()) > 0 else None
            id_docentefk = id_docentefk_str if len(id_docentefk_str.strip()) > 0 else None
            
            create_libro(id_libro, nombre, codlibro, disponible, id_estudiantefk, id_docentefk)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_libro()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            try:
                id_libro = int(input("Ingrese id del libro: ")) 
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue
            read_libro_by_id(id_libro)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Eliminar un dato")
            try:
                id_libro = int(input("Ingrese id del libro a eliminar: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                input("Ingrese ENTER para continuar...")
                continue 
            delete_libro(id_libro)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")

def main():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |     CRUD: Oracle + Python        |
                |----------------------------------|
                | 1. Crear todas las tablas        |
                | 2. Gestionar tabla Usuarios      |
                | 3. Gestionar tabla Estudiantes   |
                | 4. Gestionar tabla Docentes      |
                | 5. Gestionar tabla Investigadores|
                | 6. Gestionar tabla Libros        |
                | 0. Salir del sistema             |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-6, 0]: ")

        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_estudiantes()
        elif opcion == "4":
            menu_docentes()
        elif opcion == "5":
            menu_investigadores()
        elif opcion == "6":
            menu_libros()
        elif opcion == "0":
            os.system("cls")
            print("Saliendo del programa...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")


if __name__ == "__main__":
    main()