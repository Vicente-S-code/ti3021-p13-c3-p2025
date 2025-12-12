# Conectarnos a la base de datos
import oracledb
# Rescatar variables de entorno
import os
from dotenv import load_dotenv
# Implementar hasheo de contraeñas
import bcrypt
# Importar el tipo de dato Opcional
from typing import Optional
# Implementar peticiones HTTP
import requests
# Importar liberia de fechas
import datetime
# Cargar las variables desde el archivo .env
load_dotenv()
# Rescatar las credenciales de conexion con Oracle
username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

class Database:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
    def get_connection(self):
        return oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
    def create_all_tables(self):
        pass
    def query(self, sentence: str, parameters: Optional[dict] = None):
        print(f"Ejecutando query:\n{sentence}\nParametros:\n{parameters}")
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    resultado = cursor.execute(sentence, parameters)
                    return resultado
                connection.commit()
        except oracledb.DatabaseError as error:
            print(f"Hubo un error con al base de datos:\n{error}")


# Generar autenticacion
class Auth:
    @staticmethod
    def register(db: Database, username: str, password: str):
        salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(password,salt)
        usuario = {
            "id": 1,
            "username": username,
            "password": hashed_password
        }

        db.query(
            "INSERT INTO USERS(id,username,password) VALUES (:id,:username:password)",
            usuario
        )
    @staticmethod
    def login(db: Database, username: str, password: str) -> bool:
        resultado = db.query(
            "SELECT * FROM USERS WHERE username = :username",
            {"username" : username}
        )

        for usuario in resultado:
            password_user = usuario[2]
            return bcrypt.checkpw(password, password_user)

class Finance:
    def __init__(self, base_url: str = "https://mindicador.cl/api"):
        self.base_url = base_url

    def get_indicator(self, indicator: str = None):
        # queremos valores actuales
        if not indicator:
            return print("Indicador faltante")
        # obtener todos los indicadores actuales
        url = f"{self.base_url}"
        data = requests.get(url=url).json()
        
        # Obtenemos el valor directamente del objeto, no de la serie
        if indicator in data:
            
            indicador_info = data[indicator]
            nombre = indicador_info['nombre']
            valor = indicador_info['valor']
            unidad = indicador_info['unidad_medida']
            print(f"{nombre}: {valor} {unidad}")
            return valor
        else:
            print(f"No se encontró el indicador {indicator}")
            return None

    def get_uf(self):
        return self.get_indicator("uf")  
    def get_ivp(self):
        return self.get_indicator("ivp")  
    def get_ipc(self):
        return self.get_indicator("ipc")  
    def get_utm(self):
        return self.get_indicator("utm")  
    def get_usd(self):
        return self.get_indicator("dolar")  
    def get_eur(self):
        return self.get_indicator("euro")  

if __name__ == "__main__":
    indicadores = Finance()
    
    # Menu interactivo
    while True:
        print("""
        -----------------------------------------------
        |    MENÚ DE INDICADORES - VALORES CHILENOS   |
        -----------------------------------------------           
        | 1. Unidad de Fomento (UF)                   |                                                      
        | 2. Índice de Valor Promedio (IVP)           |           
        | 3. Índice de Precios al Consumidor % (IPC)  | 
        | 4. Unidad Tributaria Mensual(UTM)           |        
        | 5. Dólar a peso chileno (CLP)               |             
        | 6. Euro a peso chileno (CLP)                |            
        | 7. Salir del consultor                      |   
        -----------------------------------------------                 
        """)
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == "1":
            print("\n")
            indicadores.get_uf()
        elif opcion == "2":
            print("\n")
            indicadores.get_ivp()
            print("\n")
        elif opcion == "3":
            indicadores.get_ipc()
            print("\n")
        elif opcion == "4":
            indicadores.get_utm()
            print("\n")
        elif opcion == "5":
            indicadores.get_usd()
            print("\n"
                  "===============================")
        elif opcion == "6":
            indicadores.get_eur()
            print("\n")
        elif opcion == "7":
            print("\nHasta luego, gracias por usar el consultor de indicadores.")
            break
        else:
            print("\n Opción no válida. Por favor ingrese un número del 1 al 7....")
        
        



"""
# Conectarnos a la base de datos
import oracledb
# Rescatar variables de entorno
import os
from dotenv import load_dotenv
# Implementar hasheo de contraeñas
import bcrypt
# Importar el tipo de dato Opcional
from typing import Optional
# Implementar peticiones HTTP
import requests
# Importar liberia de fechas
import datetime
# Cargar las variables desde el archivo .env
load_dotenv()
# Rescatar las credenciales de conexion con Oracle
username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

class Database:
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
    def get_connection(self):
        return oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
    def create_all_tables(self):
        pass
    def query(self, sentence: str, parameters: Optional[dict] = None):
        print(f"Ejecutando query:\n{sentence}\nParametros:\n{parameters}")
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    resultado = cursor.execute(sentence, parameters)
                    return resultado
                connection.commit()
        except oracledb.DatabaseError as error:
            print(f"Hubo un error con al base de datos:\n{error}")


# Generar autenticacion
class Auth:
    @staticmethod
    def register(db: Database, username: str, password: str):
        salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(password,salt)
        usuario = {
            "id": 1,
            "username": username,
            "password": hashed_password
        }

        db.query(
            "INSERT INTO USERS(id,username,password) VALUES (:id,:username:password)",
            usuario
        )
    @staticmethod
    def login(db: Database, username: str, password: str) -> bool:
        resultado = db.query(
            "SELECT * FROM USERS WHERE username = :username",
            {"username" : username}
        )

        for usuario in resultado:
            password_user = usuario[2]
            return bcrypt.checkpw(password, password_user)

class Finance:
    def __init__(self, base_url: str = "https://mindicador.cl/api"):
        self.base_url = base_url

    def get_indicator(self, indicator: str = None, fecha:str=None):
        if not indicator:
            return print("Indicador faltante")
        if not fecha:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{month}-{year}"
        url = f"{self.base_url}/{indicator}/{fecha}"
        data = requests.get(url=url).json()
        print(data['serie'][0]['valor']) 

    def get_uf(self, fecha: str = None):
        self.get_indicator("uf", fecha)
    def get_ivp(self, fecha: str = None):
        self.get_indicator("ivp", fecha)
    def get_ipc(self, fecha: str = None):
        self.get_indicator("ipc", fecha)
    def get_utm(self, fecha: str = None):
        self.get_indicator("utm", fecha)
    def get_usd(self, fecha: str = None):
        self.get_indicator("dolar", fecha)
    def get_eur(self, fecha: str = None):
        self.get_indicator("euro", fecha)

if __name__ == "__main__":
    indicadores = Finance()
    indicadores.get_uf()
    indicadores.get_ivp()
    indicadores.get_ipc()
    indicadores.get_utm()
    indicadores.get_usd()
    indicadores.get_eur()
"""

    