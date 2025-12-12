# Conectarnos a la base de datos
import oracledb
import os
from dotenv import load_dotenv

# Implementar el hasheo de contraseñas
import bcrypt

# importar el tipo de dato opcional
from typing import Optional

# Implementar peticiones HTTP
import requests

# Implementar libreria de fecha
from datetime import datetime

# Cargar las variables desde el archivo .env
load_dotenv()

# Rescatar las credenciales de conexion con oracle
username = os.getenv("OACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

class Database:
    def __init__(self,username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
    @staticmethod
    def get_connection(self):
        return oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
    def create_all_tables(self):
        pass
    def query(self, sentence: str, parameters: Optional[dict]= None):
        print(f"ejecutando query...: \n", "\nsentences:\n{sentence}\nparametros:\n{parameters}")
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sentence, parameters)
                connection.commit()
        except oracledb.DatabaseError as error:
            print(f"No se pudo crear la tabla: {error}")        
        
# Generar autenticacion
class Auth:
    @staticmethod
    def register(db: Database, username: str, password: str):
        salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(password,salt)
        usuario= {
            "username": username,
            "password": hashed_password
        }
        db.query(
            "INSERT INTO USERS (id,username,password) VALUES (:id,username, password)",
            usuario
        )
    @staticmethod
    def login(db: Database, username: str, password: str):
        resultado = db.query(
        "SELECT * FROM USERS WHERE username = :username",
        {"username": username}
    )
        for usuario in resultado:
            password_user = usuario[2]
            return bcrypt.checkpw(password, password_user)
                

class finance:
    def __init__(self, base_url: str= "https://mindicador.cl/api"):
        self.base_url = base_url
    def get_uf(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/uf/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])

    def get_ipv(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/ipv/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])
    
    def get_ipc(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/ipc/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])
    
    def get_utm(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/utm/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])
    
    def get_usd(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/dolar/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])
    
    def get_eur(self,fecha: str = None):
        if not fecha:
            year = datetime.datetime.now().year
            mont = datetime.datetime.now().month
            day = datetime.datetime.now().day
            fecha = f"{day}-{mont}-{year}"
        url = f"{self.base_url}/euro/{fecha}"
        data = requests.get(url= url).json()
        print(data['serie'][0]['valor'])

if __name__ == "__main__":
    db = Database(username=username, password=password, dsn=dsn)
    db.query("SELECT sysdate FROM dual")
    