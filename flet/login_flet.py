import flet as ft

def main(page: ft.Page):
    page.title = "Login con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def login(e):
        if username.value == "admin" and password.value == "1234":
            message.value = "Login exitoso"
            message.color = "green"
        else:
            message.value = "Credenciales incorrectas"
            message.color = "red"
        page.update()

    username = ft.TextField(label="Usuario", width=300)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    login_button = ft.ElevatedButton("Iniciar sesión", on_click=login)
    message = ft.Text("")

    page.add(
        ft.Column(
            [
                ft.Text("Login", size=24, weight=ft.FontWeight.BOLD),
                username,
                password,
                login_button,
                message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)