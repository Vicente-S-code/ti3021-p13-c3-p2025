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

def create_schema():  
           
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
        )


        ]
        for query in tables:
        try:         
            with get_connection() as connection:             
             with connection.cursor() as cursor:                 
              cursor.execute(query)                 
              print("Tabla 'personas' creada.")     
        except oracledb.DatabaseError as error:                  
            print(f"No se pudo crear la tabla: {error}") 