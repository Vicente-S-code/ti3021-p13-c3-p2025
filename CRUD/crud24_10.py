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

    def __str__(self): #nos permite ver los datos del usuario
       return f"""
        Rut: {self.rut}-{self.digito_verificador}
        Nombre completo: {self.nombres} {self.apellidos}
        Fecha de nacimiento: +{self.cod_area} {self.telefono}
       """
       

#creamos una lista para almacenar varios objetos intanciados de la clase |persona|
personas = []

def persona_existe(nueva_Persona: persona) -> bool:
   for persona in personas:
    if persona.rut == nueva_Persona.rut:
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

   if persona_existe(nueva_persona):
      return print("no se registro a la persona.")
   else:
      personas.append(nueva_persona)
   pass
def read_persona():
   for persona in personas:
      print("="*20)
      print(persona)
      print("="*20)
      
def update_persona(rut: int):
   rut_busqueda = int(input("ingresa el rut de la persona"))
   for persona in personas:
      if persona.rut == rut_busqueda:
         while True:
            print(
               f"""
              |-======================-|
              -|| Edicion de personas||-
              |-======================-|
               1. Rut: {persona.rut}
               2. Digito_verificador: {persona.digito_verificador}
               3. Nombres: {persona.nombres}
               4. Apellidos: {persona.apellidos} 
               5. Fecha de nacimiento: {persona.fecha_nacimiento} 
               6. Codigo de area: {persona.cod_area} 
               7. Telefono: {persona.telefono} 
               0. No seguir modificando
               """
            )
            opcion = input("ingrese una opcion)")
            if opcion == "1":
               rut: int = int(input("ingrese el rut de la persona: "))
               for persona in personas:
                  if persona.rut == rut:
                     print(f"La persona con el rut {persona.rut} ya existe. Intente con otro rut")
                  else:
                     persona.rut = rut
                     print("Rut modificado exitosamente")
            elif opcion == "2":
               digito_verificador: str = input("ingresa el digito verificador: ")   
               persona.digito_verificador = digito_verificador
               print("Digito verificador modificado exitosamente ")     
            elif opcion == "3":
               nombres: str = input("Ingresa los nombres de la persona: ")
               persona.nombres = nombres
               print("Nombres modificado exitosamente")
            elif opcion == "4":
               apellidos: str = input("Ingresa los apellidos de la persona: ")
               persona.apellidos = apellidos
               print("Apellidos modificados exitosamente")
            elif opcion == "5":
               dia_nacimiento = int(input("Ingresa el dia de nacimiento de la persona: "))
               mes_nacimiento = int(input("ingresa el mes de nacimiento de la persona: "))
               anio_nacimiento = int(input("Ingresa el año de nacimiento de la persona"))
               fecha_nacimiento: date = date(
                  year=anio_nacimiento,
                  month=mes_nacimiento,
                  day=dia_nacimiento
               )
               persona.fecha_nacimiento = fecha_nacimiento
               print("Fecha de nacimiento modificada exitosamente")
            elif opcion == "6":
               cod_area: int = int(input("Ingrese el codigo de area del telefono de la persona (ejemplo +56 9): "))
               persona.cod_area = cod_area
               print("Codigo de area modificado exitosamente")
            elif opcion == "7":
               telefono: int = int(input("Ingrese el numero de telefono de la persona: "))
               persona.telefono = telefono
               print("Telefono modificado exitosamente")
            elif opcion == "0":
               print("-----|Modificaciones completadas|-----")
            else:
               print("Opcion incorrecta")
               input("Presiona |ENTER| para continuar...")
def delete_persona():
   rut_busqueda = int(input("Ingresa el rut sin el digito verificador (ej:22283696): "))
   for persona in personas:
      print(f"ELIMINANDO A PERSONA CON DATOS....{persona}")
      personas.remove(persona)
      print(f"persona con rut {rut_busqueda}, no encontrada.")
   print(f"persona con rut {rut_busqueda}, no encontrada")
   input("Presiona |ENTER| para continuar")

while True:
   print(
      """
         1. |Crear persona|
         2. |Listar persona|
         3. |Editar persona|
         4. |Eliminar persona|
         0. |Salir|
      """
      )
   
   opcion = input("|||--|Ingrese una opcion|--|||\n"
   ">>> ")
 
   if opcion == "1":
      create_persona()
   elif opcion == "2":
      read_persona()
   elif opcion == "3":
      update_persona()
   elif opcion == "4":
      delete_persona()
   elif opcion == "0":
    break
   else:
      print("Opcion invalida")
      print("Presiona |ENTER| para continuar....")
    