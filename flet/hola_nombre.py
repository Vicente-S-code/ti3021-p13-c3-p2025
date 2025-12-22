"""
ESTE EJEMPLO VA A ABARCAR EL USO DE INPUTS, LABELS Y BOTONES
PARA FAMILIARIZARSE, QUE COSAS BASICAS DE FUNCIONALIDAD PODEMOS 
LOGRAR CON FLET
"""

# paso 1. importar la biblioteca Flet
import flet as ft

# paso 2. Crear la clase principal de la aplicacion
class App:
    def __init__(self, page: ft.Page):
      self.page = page
      self.page.title = "Hola Nombre"

      self.input_nombre = ft.TextField(hint_text="Ingresa tu nombre")
      self.label_saludar = ft.Button(text="Saludar", on_click=self.handle_saludo)
      self.text_saludo = ft.Text(value="")

      self.build()

    def build(self):
       self.page.add(
            self.input_nombre,
            self.label_saludar,
            self.text_saludo
         )
       self.page.update()
    def handle_saludo(self, e):
        nombre = (self.input_nombre.value or "").strip()
        if nombre:
           self.text_saludo.value = f"Hola, {nombre}"
        else:
            self.text_saludo.value = "Ingrese un nombre"
        self.page.update()

# paso 3. Ejecutar la aplicacion
if __name__ == "__main__":
    ft.app(target=App)



