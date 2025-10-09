class Usuario:
    def __init__(self, nombre:str, rut:str, CorreoInstitucional:str):
     self._nombre:str = nombre
     self._rut:str = rut
     self._CorreoInstitucional:str = CorreoInstitucional

class Estudiante:
   def __init__(self, carrera: str, añoingreso: int):
      self._carrera: str = carrera
      self._añoIngreso:int = añoingreso

class Docente:
   def __init__(self, especialidad:str):
      self._especialidad:str = especialidad
def recomendarLibro(self)->str:
   return print(f"Docente:mira te dejo una recomendacion de este libro se llama {self._nombrelibro}")

class Investigador:
   def __init__(self, lineadeInvestigacion: str):
      self._lineadeInvestigacion:str = lineadeInvestigacion
class Libro:
   def __init__(self, nombrelibro:str, codlibro: str, disponible: bool):
      self._nombrelibro:str = nombrelibro
      self._codlibro:str = codlibro
      self._disponible:bool = disponible
        
recomendacionLibro: Libro = Libro("Vikingos","qyt7765","True")