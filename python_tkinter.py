# OBLIGATORIO: importar la libreria TKINTER
from tkinter import*
from tkinter import ttk 

# OBLIGATORIO:Inicializar TKINTER
root: Tk = Tk()

# Configuracion general
root.title("")
root.iconphoto(
    PhotoImage
)

# Crear un lienzo. contexto, estilizacion
frame1: Frame = ttk.Frame(root, padding=10)


# OBLIGATORIO: Mantener el ciclo de vida
root.mainloop()
