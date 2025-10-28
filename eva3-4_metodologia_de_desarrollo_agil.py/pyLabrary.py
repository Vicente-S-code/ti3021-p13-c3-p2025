# 
from datetime import date, timedelta

DIAS_PRESTAMO = 7
PENALIZACION_POR_DIA = 2

class Libro:
    def __init__(self, id_libro, titulo, autor, ejemplares):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.disponibles = ejemplares

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.penalizado_hasta = None

class Prestamo:
    def __init__(self, id_prestamo, libro, usuario):
        self.id = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=DIAS_PRESTAMO)
        self.devuelto = False

# Datos en memoria
libros = []
usuarios = []
prestamos = []
id_libro = id_usuario = id_prestamo = 0
print(" Bienvenido a la biblioteca, ¿que desea hacer hoy?")
def menu():
    print("\n--| SISTEMA BIBLIOTECA ---- PYLABRARY |--")
    print("|1| - Agregar libro")
    print("|2| - Registrar usuario")
    print("|3| - Prestar / Devolver libro")
    print("|4| - Ver información")
    print("|5| - Salir")

def agregar_libro():
    global id_libro
    titulo = input("Título Libro: ")
    autor = input("Autor Libro: ")
    ejemplares = int(input("Cantidad Libro: "))
    id_libro += 1
    libros.append(Libro(id_libro, titulo, autor, ejemplares))
    print(" Libro agregado.")

def registrar_usuario():
    global id_usuario
    nombre = input("Nombre: ")
    id_usuario += 1
    usuarios.append(Usuario(id_usuario, nombre))
    print(" Usuario registrado.")

def prestar_libro():
    global id_prestamo
    listar_libros()
    id_l = int(input("ID libro: "))
    listar_usuarios()
    id_u = int(input("ID usuario: "))
    libro = next((l for l in libros if l.id == id_l), None)
    usuario = next((u for u in usuarios if u.id == id_u), None)
    if libro and usuario and libro.disponibles > 0:
        id_prestamo += 1
        libro.disponibles -= 1
        prestamos.append(Prestamo(id_prestamo, libro, usuario))
        print(f" Préstamo registrado. Devuelve antes de {date.today() + timedelta(days=DIAS_PRESTAMO)}")
    else:
        print(" Error: libro no disponible o usuario no existe.")

def devolver_libro():
    listar_prestamos()
    id_p = int(input("ID préstamo: "))
    prestamo = next((p for p in prestamos if p.id == id_p), None)
    if prestamo and not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.libro.disponibles += 1
        atraso = (date.today() - prestamo.fecha_devolucion).days
        if atraso > 0:
            penalizacion = atraso * PENALIZACION_POR_DIA
            prestamo.usuario.penalizado_hasta = date.today() + timedelta(days=penalizacion)
            print(f" Devuelto con atraso, recuerda que hay una penalizacion por no devolver a tiempo el libro"  
                  "\nPenalización: {penalizacion} días.")
        else:
            print(" El libro fue Devuelto a tiempo.")
    else:
        print(" Préstamo no encontrado o ya devuelto.")

def listar_libros():
    print("\n| LIBROS DISPONIBLES |")
    for l in libros:
        print(f"[{l.id}] {l.titulo} ({l.disponibles}/{l.ejemplares})")

def listar_usuarios():
    print("\n| USUARIOS REGISTRADOS |")
    for u in usuarios:
        estado = f"Penalizado hasta {u.penalizado_hasta}" if u.penalizado_hasta else "Activo"
        print(f"[{u.id}] {u.nombre} - {estado}")

def listar_prestamos():
    print("\n| PRÉSTAMOS |")
    for p in prestamos:
        estado = "Devuelto" if p.devuelto else "Activo"
        print(f"[{p.id}] Libro: {p.libro.titulo} | Usuario: {p.usuario.nombre} | {estado}")

def ver_info():
    listar_libros()
    listar_usuarios()
    listar_prestamos()

# Programa principal
while True:
    menu()
    op = input("Ingrese una Opción (1-5): ")
    if op == "1": agregar_libro()
    elif op == "2": registrar_usuario()
    elif op == "3":
        accion = input("¿Prestar (P) o Devolver (D)? ").upper()
        if accion == "P": prestar_libro()
        elif accion == "D": devolver_libro()
    elif op == "4": ver_info()
    elif op == "5":
        print("Hasta pronto, vuelve cuando gustes")
        break
    else:
        print("Opción inválida.")
