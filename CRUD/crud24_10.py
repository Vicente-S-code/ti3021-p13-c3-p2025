"""
Actividad practica y reflexion: 
Implementa un sistema CRUD para al menos 3 clases distintas

CRUD
----
Create: Crear un nuevo registro
Read: Leer registro/s
Update: Actualizar registro
Delete: Borrar registro
"""

"""
GLOSARIO
--------

-Pass: es la palabra reservada para que python no exija el codigo minimo,
para el funcionamiento
de la funcion/metodo.

-IDE: viene de la palabra integrated Development Enviroment que significa entorno
de desarrollo integrado, que son los editores de codigo que normalmente utilizamos
para programar en la informatica.

-lint o linter: es el encargado de vigilar que la sintaxis del codigo en el IDE sea correcta
y te sugiere el funcionamiento de este.
"""

#Importar DATETIME (fecha: date) (datetime: hora)
from datetime import date

#Primero, debemos de definir una clase
class persona:
    #Definir como se inicializa
    def __init__(
            self,
            rut: int,
            digito_verificador: str,
            nombres: str,
            apellidos: str,
            fecha_nacimiento: date,
            cod_area: int,
            telefono: int
): 
     self.rut: int = rut
     self.digito_verificador: str = digito_verificador
     self.nombres: str = nombres
     self.apellidos: str = apellidos
     self.fecha_nacimiento: date = fecha_nacimiento
     self.cod_area: int = cod_area
     self.telefono: int = telefono

#creamos una lista para almacenar varios objetos intanciados de la clase |persona|
personas = list[persona] = []

def persona_existe(nueva_Persona: persona) -> bool:
   for persona in personas:
      if persona.rut == nueva_persona.rut:
       print(f"persona ya existe con rut: {persona.rut}-{persona.digito_verificador}")

   print("persona no existente.")
   return True

def create_persona():
   rut: int = int(input("ingrese rut sin digito verificador:"))
   digito_verificador: str = input("ingrese digito verificador:")
   nombres: str = input ("ingrese nombres de la persona:")
   apellidos: str = input ("ingrese apellidos de la persona:")
   dia_nacimiento: int = int(input("ingrese el dia de nacimiento"))
   mes_nacimiento: int = int(input("ingrese el mes de nacimiento"))
   anio_nacimiento: int = int(input("ingrese el año de nacimiento"))
   fecha_nacimiento: date = date ("year=anio_nacimiento, month=mes_nacimiento, day=dia_nacimiento")
   cod_area: int = int(input("ingrese codigo de area del numero de telefono:"))
   telefono: int = int(input("ingrese numero de telefono sin codigo de area:")) 

   nueva_persona = persona(
     rut,
     digito_verificador,
     nombres,
     apellidos,
     fecha_nacimiento,
     cod_area,
     telefono    
   )

   if persona_existe(nueva_Persona):
      return print("no se registro a la persona.")
   else:
      personas.append(nueva_persona)
   pass
def read_persona():
   pass
def update_persona():
   pass
def delete_persona():
   pass
    