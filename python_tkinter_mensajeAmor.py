# OBLIGATORIO: importar la libreria TKINTER
from tkinter import *
from tkinter import ttk

# ===============================
#  Ventana principal (root)
# ===============================
root: Tk = Tk()

# Configuración general
root.title("💖 Mensaje Especial")
root.geometry("750x450")          # Tamaño de ventana
root.resizable(False, False)       # Fijar tamaño (opcional)
root.configure(bg="#0f1228")       # Color de fondo base

# (Opcional) Icono de la ventana (reemplaza 'icono.png' por tu archivo)
# try:
#     icono = PhotoImage(file="icono.png")
#     root.iconphoto(True, icono)
# except Exception:
#     pass

# Crear un lienzo (Canvas) para dibujar fondo y elementos
canvas = Canvas(root, width=720, height=450, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ===============================
#  Fondo con degradado simple
# ===============================
def dibujar_degradado_vertical(cnv, color1, color2, ancho, alto, pasos=120):
    """
    Dibuja un degradado vertical aproximado con rectángulos.
    color1: color superior, color2: inferior (en hex, ej. "#4455aa")
    """
    def hex_a_rgb(hx: str):
        hx = hx.lstrip("#")
        return tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))

    def rgb_a_hex(rgb):
        return "#%02x%02x%02x" % rgb

    r1, g1, b1 = hex_a_rgb(color1)
    r2, g2, b2 = hex_a_rgb(color2)

    for i in range(pasos):
        t = i / max(pasos - 1, 1)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        y0 = int((alto / pasos) * i)
        y1 = int((alto / pasos) * (i + 1))
        cnv.create_rectangle(0, y0, ancho, y1, outline="", fill=rgb_a_hex((r, g, b)))

# Dibuja el fondo (colores: violeta a rosado)
dibujar_degradado_vertical(
    canvas,
    color1="#1c1f4a",   # arriba (azul/violeta oscuro)
    color2="#8a2c6c",   # abajo (magenta/rosado)
    ancho=1000,
    alto=600,
    pasos=160
)

# ===============================
#  Corazones decorativos (Canvas)
# ===============================
def dibujar_corazon(cnv, cx, cy, tam=30, color="#ff5c93", contorno=""):
    """
    Dibuja un corazón aproximado usando curvas con create_polygon.
    (Forma compuesta & suavizada)
    cx, cy: centro; tam: tamaño
    """
    # Puntos base de un corazón estilizado (normalizados)
    pts = [
        (-1, -0.2), (-0.7, -0.8), (-0.2, -0.9), (0, -0.6),
        (0.2, -0.9), (0.7, -0.8), (1, -0.2),
        (0.0, 1.0)
    ]
    # Escalar y trasladar
    coords = []
    for (x, y) in pts:
        coords.extend([cx + x * tam, cy + y * tam])
    cnv.create_polygon(
        coords, smooth=True, splinesteps=20,
        fill=color, outline=contorno, width=2
    )

# Corazones en distintas posiciones (sutiles)
dibujar_corazon(canvas, 90,  90,  tam=26, color="#ff7aa8")
dibujar_corazon(canvas, 640, 120, tam=22, color="#ffa3c4")
dibujar_corazon(canvas, 120, 360, tam=20, color="#ff6d9c")
dibujar_corazon(canvas, 620, 340, tam=28, color="#ff89b4")
dibujar_corazon(canvas, 360, 70,  tam=18, color="#ffc1d6")
dibujar_corazon(canvas, 540, 220, tam=16, color="#ff94bd")

# ===============================
#  Marco (Frame) opcional con ttk
# ===============================
# Si quieres un marco para contenidos adicionales, lo agregamos.
frame1: Frame = ttk.Frame(root, padding=10)
frame1.place(relx=0.5, rely=0.85, anchor="center")  # posición inferior centrada (opcional)

# ===============================
#  Texto principal: "TE AMO"
# ===============================
# Sombra (para dar relieve)
canvas.create_text(
    360, 180, text="", fill="#000000",
    font=("Georgia", 64, "bold")
)
# Texto frontal
canvas.create_text(
    360, 176, text="VUELVE PORFAVOR", fill="#ffe8f2",
    font=("Georgia", 64, "bold")
)

# Subtítulo opcional
canvas.create_text(
    360, 235, text="ATTE: VIXO", fill="#ffe8f2",
    font=("Arial", 18, "italic")
)

# Botón para cerrar (sobre el lienzo)
def cerrar():
    root.destroy()

# Dibujar un botón simple en Canvas
btn_w, btn_h = 180, 44
bx, by = 360, 320
btn_rect = canvas.create_rectangle(
    bx - btn_w//2, by - btn_h//2, bx + btn_w//2, by + btn_h//2,
    fill="#2d2f55", outline="#e0e2ff", width=2
)
btn_text = canvas.create_text(bx, by, text="Cerrar", fill="#e0e2ff", font=("Arial", 16, "bold"))

# Interacción básica de botón (hover/click)
def on_click(event):
    x, y = event.x, event.y
    x0, y0, x1, y1 = canvas.coords(btn_rect)
    if x0 <= x <= x1 and y0 <= y <= y1:
        cerrar()

def on_motion(event):
    x, y = event.x, event.y
    x0, y0, x1, y1 = canvas.coords(btn_rect)
    if x0 <= x <= x1 and y0 <= y <= y1:
        canvas.itemconfig(btn_rect, fill="#3b3f7a")
    else:
        canvas.itemconfig(btn_rect, fill="#2d2f55")

canvas.bind("<Button-1>", on_click)
canvas.bind("<Motion>", on_motion)

# ===============================
#  OBLIGATORIO: Mantener el ciclo de vida
# ===============================
root.mainloop()