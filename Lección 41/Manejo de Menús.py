# Dentro de esta rutina, revisaremos el manejo de Menús de una ventana

# Importamos los módulos necesarios para el manejo de ventanas y sus componentes
import sys
import tkinter
from tkinter import ttk, messagebox

# Importamos el módulo necesario para la creación de menús
from tkinter import Menu

# Creamos la función para el evento de "Salir"
def eventoSalir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

# Creamos la ventana y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('300x100')
ventana.title('Manejo de Menús')
ventana.iconbitmap('icono.ico')

# Elaboración del Menú Total de la Ventana
    # Creamos el menú principal
menuPrincipal = Menu(ventana)
        # Creamos un sub-menú, Archivo, dentro del menú principal
subMenuArchivo = Menu(menuPrincipal, tearoff = False) # <-- El argumento tearoff determina si queremos que el menú sea desplegable
            # Creamos las opciones del sub-menú
subMenuArchivo.add_command(label = 'Nuevo')
subMenuArchivo.add_separator()
subMenuArchivo.add_command(label = 'Salir', command = eventoSalir) # <-- Con el parámetro de command, le agregamos funcionalidad a la opción de Salir
        # Añadimos el sub-menú al menú principal
menuPrincipal.add_cascade(menu = subMenuArchivo, label = 'Archivo')

        # Creamos otro sub-menú, Ayuda, dentro del menú principal
subMenuAyuda = Menu(menuPrincipal, tearoff = False)
            # Creamos las opciones del sub-menú
subMenuAyuda.add_command(label = 'Acerca de')
subMenuAyuda.add_separator()
        #Añadimos el sub-menú al menú principal
menuPrincipal.add_cascade(menu = subMenuAyuda, label = 'Ayuda')

# Desplegamos la ventana y sus componentes
    # Desplegamos el menú dentro de la ventana
ventana.config(menu = menuPrincipal)

ventana.mainloop()