from typing import Optional, Dict, List


# =======================
#   MODELO DE DOMINIO
# =======================

class Usuario:
    def __init__(self, nombre: str, rut: str, CorreoInstitucional: str):
        self._nombre: str = nombre
        self._rut: str = rut
        self._CorreoInstitucional: str = CorreoInstitucional

    def solicitar_prestamo(self, biblioteca: "Biblioteca", cod_libro: str) -> str:
        libro = biblioteca.buscar_por_codigo(cod_libro)
        if not libro:
            return f"[{self._nombre}] No existe un libro con código {cod_libro}."
        return biblioteca.prestar(libro, self)

    def __str__(self) -> str:
        return f"{self._nombre} ({self._rut})"


class Estudiante(Usuario):
    def __init__(self, nombre: str, rut: str, CorreoInstitucional: str,
                 carrera: str, añoingreso: int):
        super().__init__(nombre, rut, CorreoInstitucional)
        self._carrera: str = carrera
        self._añoIngreso: int = añoingreso


class Docente(Usuario):
    def __init__(self, nombre: str, rut: str, CorreoInstitucional: str,
                 especialidad: str):
        super().__init__(nombre, rut, CorreoInstitucional)
        self._especialidad: str = especialidad

    def recomendar_libro(self, nombrelibro: str) -> str:
        return (f"Docente {self._nombre} recomienda: "
                f"'{nombrelibro}'. Ideal para profundizar en {self._especialidad}.")

    def publicar_libro(self, biblioteca: "Biblioteca", libro: "Libro") -> str:
        return biblioteca.publicar_libro(libro, autor=self)


class Investigador(Usuario):
    def __init__(self, nombre: str, rut: str, CorreoInstitucional: str,
                 lineadeInvestigacion: str):
        super().__init__(nombre, rut, CorreoInstitucional)
        self._lineadeInvestigacion: str = lineadeInvestigacion

    def publicar_libro(self, biblioteca: "Biblioteca", libro: "Libro") -> str:
        return biblioteca.publicar_libro(libro, autor=self)


class Libro:
    def __init__(self, nombrelibro: str, codlibro: str, disponible: bool = True,
                 autor_textual: Optional[str] = None):
        self._nombrelibro: str = nombrelibro
        self._codlibro: str = codlibro
        self._disponible: bool = disponible
        self._autor_textual: Optional[str] = autor_textual
        self._prestado_a: Optional[Usuario] = None

    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else f"Prestado a {self._prestado_a._nombre}"
        autor = f" | Autor: {self._autor_textual}" if self._autor_textual else ""
        return f"[{self._codlibro}] {self._nombrelibro}{autor} - {estado}"


class Biblioteca:
    def __init__(self, nombre: str):
        self._nombre: str = nombre
        self._catalogo: Dict[str, Libro] = {}
        self._historial: List[str] = []

    # --- Gestión de catálogo ---
    def publicar_libro(self, libro: Libro, autor: Optional[Usuario] = None) -> str:
        if libro._codlibro in self._catalogo:
            return (f"El libro con código {libro._codlibro} ya existe en el catálogo "
                    f"({self._catalogo[libro._codlibro]._nombrelibro}).")
        self._catalogo[libro._codlibro] = libro
        quien = f" por {autor._nombre}" if autor else ""
        msg = f"Libro '{libro._nombrelibro}' (código {libro._codlibro}) publicado{quien}."
        self._historial.append(msg)
        return msg

    def buscar_por_codigo(self, codlibro: str) -> Optional[Libro]:
        return self._catalogo.get(codlibro)

    def listar_libros(self) -> List[str]:
        if not self._catalogo:
            return ["(Catálogo vacío)"]
        return [str(libro) for libro in self._catalogo.values()]

    # --- Préstamos ---
    def prestar(self, libro: Libro, usuario: Usuario) -> str:
        if libro._codlibro not in self._catalogo:
            return f"El libro '{libro._nombrelibro}' no pertenece a esta biblioteca."
        if not libro._disponible:
            return (f"No disponible: '{libro._nombrelibro}' ya se encuentra prestado "
                    f"a {libro._prestado_a._nombre}.")
        libro._disponible = False
        libro._prestado_a = usuario
        msg = f"Préstamo exitoso: '{libro._nombrelibro}' a {usuario._nombre}."
        self._historial.append(msg)
        return msg

    def devolver(self, libro: Libro) -> str:
        if libro._codlibro not in self._catalogo:
            return f"El libro '{libro._nombrelibro}' no pertenece a esta biblioteca."
        if libro._disponible:
            return f"'{libro._nombrelibro}' ya estaba disponible. No había préstamo activo."
        quien = libro._prestado_a._nombre if libro._prestado_a else "desconocido"
        libro._disponible = True
        libro._prestado_a = None
        msg = f"Devolución registrada: '{libro._nombrelibro}' devuelto por {quien}."
        self._historial.append(msg)
        return msg

    def historial(self) -> List[str]:
        return list(self._historial)


# =======================
#   INTERFAZ POR CONSOLA
# =======================

def input_no_vacio(msg: str) -> str:
    while True:
        v = input(msg).strip()
        if v:
            return v
        print("⚠️  Este campo no puede estar vacío.")

def input_int(msg: str) -> int:
    while True:
        v = input(msg).strip()
        if v.isdigit():
            return int(v)
        print("⚠️  Debes ingresar un número entero.")

def pausa():
    input("\nPresiona ENTER para continuar...")

def imprimir_titulo(t: str):
    print("\n" + "=" * 60)
    print(t)
    print("=" * 60)

def registrar_estudiante(usuarios: Dict[str, Usuario]):
    imprimir_titulo("Registrar Estudiante")
    rut = input_no_vacio("RUT: ")
    if rut in usuarios:
        print("⚠️  Ya existe un usuario con ese RUT.")
        return
    nombre = input_no_vacio("Nombre: ")
    correo = input_no_vacio("Correo institucional: ")
    carrera = input_no_vacio("Carrera: ")
    año = input_int("Año de ingreso (ej: 2024): ")
    usuario = Estudiante(nombre, rut, correo, carrera, año)
    usuarios[rut] = usuario
    print(f"✅ Estudiante registrado: {usuario}")

def registrar_docente(usuarios: Dict[str, Usuario]):
    imprimir_titulo("Registrar Docente")
    rut = input_no_vacio("RUT: ")
    if rut in usuarios:
        print("⚠️  Ya existe un usuario con ese RUT.")
        return
    nombre = input_no_vacio("Nombre: ")
    correo = input_no_vacio("Correo institucional: ")
    esp = input_no_vacio("Especialidad: ")
    usuario = Docente(nombre, rut, correo, esp)
    usuarios[rut] = usuario
    print(f"✅ Docente registrado: {usuario}")

def registrar_investigador(usuarios: Dict[str, Usuario]):
    imprimir_titulo("Registrar Investigador")
    rut = input_no_vacio("RUT: ")
    if rut in usuarios:
        print("⚠️  Ya existe un usuario con ese RUT.")
        return
    nombre = input_no_vacio("Nombre: ")
    correo = input_no_vacio("Correo institucional: ")
    linea = input_no_vacio("Línea de investigación: ")
    usuario = Investigador(nombre, rut, correo, linea)
    usuarios[rut] = usuario
    print(f"✅ Investigador registrado: {usuario}")

def publicar_libro_cli(biblio: Biblioteca, usuarios: Dict[str, Usuario]):
    imprimir_titulo("Publicar Libro")
    nombre = input_no_vacio("Título del libro: ")
    codigo = input_no_vacio("Código del libro (único): ")
    autor_textual = input("Autor (texto libre, opcional): ").strip() or None

    libro = Libro(nombre, codigo, disponible=True, autor_textual=autor_textual)

    usar_autor = input("¿Asignar autor del sistema (Docente/Investigador) por RUT? (s/n): ").strip().lower()
    if usar_autor == "s":
        rut = input_no_vacio("RUT del autor: ")
        autor = usuarios.get(rut)
        if isinstance(autor, (Docente, Investigador)):
            print(biblio.publicar_libro(libro, autor=autor))
        else:
            print("⚠️  El RUT no corresponde a Docente/Investigador o no existe. Se publica sin autor sistema.")
            print(biblio.publicar_libro(libro, autor=None))
    else:
        print(biblio.publicar_libro(libro, autor=None))

def listar_libros_cli(biblio: Biblioteca):
    imprimir_titulo("Catálogo de Libros")
    for fila in biblio.listar_libros():
        print("•", fila)

def solicitar_prestamo_cli(biblio: Biblioteca, usuarios: Dict[str, Usuario]):
    imprimir_titulo("Solicitar Préstamo")
    rut = input_no_vacio("RUT del usuario: ")
    usuario = usuarios.get(rut)
    if not usuario:
        print("⚠️  No existe un usuario con ese RUT.")
        return
    codigo = input_no_vacio("Código del libro: ")
    print(usuario.solicitar_prestamo(biblio, codigo))

def devolver_libro_cli(biblio: Biblioteca):
    imprimir_titulo("Devolver Libro")
    codigo = input_no_vacio("Código del libro: ")
    libro = biblio.buscar_por_codigo(codigo)
    if not libro:
        print("⚠️  No existe un libro con ese código.")
        return
    print(biblio.devolver(libro))

def recomendar_libro_cli(usuarios: Dict[str, Usuario]):
    imprimir_titulo("Recomendar Libro (Docente)")
    rut = input_no_vacio("RUT del Docente: ")
    usuario = usuarios.get(rut)
    if not isinstance(usuario, Docente):
        print("⚠️  El RUT no corresponde a un Docente o no existe.")
        return
    titulo = input_no_vacio("Título del libro a recomendar: ")
    print(usuario.recomendar_libro(titulo))

def ver_historial_cli(biblio: Biblioteca):
    imprimir_titulo("Historial de Operaciones")
    hist = biblio.historial()
    if not hist:
        print("(Sin movimientos todavía)")
    else:
        for h in hist:
            print("•", h)

def menu():
    print("""
================= MENÚ BIBLIOTECA =================
1) Registrar Estudiante
2) Registrar Docente
3) Registrar Investigador
4) Publicar libro
5) Listar libros
6) Solicitar préstamo
7) Devolver libro
8) Recomendar libro (Docente)
9) Ver historial
0) Salir
===================================================
""")

def main():
    biblio = Biblioteca("Biblioteca Central")
    usuarios: Dict[str, Usuario] = {}

    while True:
        menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            registrar_estudiante(usuarios); pausa()
        elif opcion == "2":
            registrar_docente(usuarios); pausa()
        elif opcion == "3":
            registrar_investigador(usuarios); pausa()
        elif opcion == "4":
            publicar_libro_cli(biblio, usuarios); pausa()
        elif opcion == "5":
            listar_libros_cli(biblio); pausa()
        elif opcion == "6":
            solicitar_prestamo_cli(biblio, usuarios); pausa()
        elif opcion == "7":
            devolver_libro_cli(biblio); pausa()
        elif opcion == "8":
            recomendar_libro_cli(usuarios); pausa()
        elif opcion == "9":
            ver_historial_cli(biblio); pausa()
        elif opcion == "0":
            print("👋 ¡Hasta luego!"); break
        else:
            print("⚠️  Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
