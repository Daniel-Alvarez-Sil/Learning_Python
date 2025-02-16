# Manejo de Barras de Progreso

# Importamos los módulos necesarios para el funcionamiento de la rutina
import tkinter
from tkinter import ttk, messagebox
from Creación_de_Tabuladores import Tabulador
from time import sleep

# Creamos la ventana y le asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('200x300+500+125')
ventana.title('Manejo de Barras de Progreso')
ventana.iconbitmap('icono.ico')
ventana.resizable(False, False)

# Creamos los widgets de la ventana
    # Notebook
tabuladores = ttk.Notebook(ventana)
        # Tabuladores del Notebook
tab1 = Tabulador(tabuladores, 'Barra de Progreso')
            # Proporciones de Filas y Columnas
                # Filas
tab1.rowconfigure(0, weight = 50)
tab1.rowconfigure(1, weight = 50)
tab1.rowconfigure(2, weight = 50)
tab1.rowconfigure(3, weight = 50)
                # Columnas
tab1.columnconfigure(0, weight = 50)
tab1.columnconfigure(1, weight = 50)
    # Barra de Progreso
progressBar = ttk.Progressbar(tab1, orient = 'vertical', length = 300)
    # Botones
def eventoCiclo():
    messagebox.showinfo(title = 'Ciclo de Progreso', message = 'Inicio del ciclo de progresiones. ')
    progressBar.start()
botonCiclo = ttk.Button(tab1, text = 'Ciclo de Progreso', command = eventoCiclo)
def eventoDetener():
    progressBar.stop()
botonDetener = ttk.Button(tab1, text = 'Detener Progreso', command = eventoDetener)
def eventoIniciar():
    botonCiclo.config(state = 'disabled')
    botonDetener.config(state = 'disabled')
    botonReiniciar.config(state = 'disabled')
    messagebox.showinfo(title = '1 Ciclo de Progreso', message = 'Inicio de 1 SOLO ciclo de progresiones. ')
    progressBar['maximum'] = 100
    for x in range(100):
        sleep(0.05) # <-- Con esta sintáxis, la rutina se pausa por 0.05 segundos
        progressBar['value'] = x
        progressBar.update()
    botonCiclo.config(state = 'enabled')
    botonDetener.config(state = 'enabled')
    botonReiniciar.config(state = 'enabled')
botonIniciar = ttk.Button(tab1, text = '1 Ciclo de Progreso', command = eventoIniciar)
def eventoReiniciar():
    messagebox.showinfo(title = 'Reinicio del Ciclo de Progreso', message = 'Se ha vuelto a establecer en ceros el estatus del progreso. ')
    progressBar['value'] = 0
botonReiniciar = ttk.Button(tab1, text = 'Reiniciar la Barra de Progreso', command = eventoReiniciar)

# Desplegamos la ventana y sus atributos
botonReiniciar.grid(row = 3, column = 1, ipady = 10)
botonIniciar.grid(row = 2, column = 1, ipady = 10, ipadx = 25)
botonDetener.grid(row = 1, column = 1, ipady = 10, ipadx = 30)
botonCiclo.grid(row = 0, column = 1, ipady = 10, ipadx = 30)
progressBar.grid(row = 0, column = 0, rowspan = 4)
tabuladores.pack(fill = 'both')
ventana.mainloop()