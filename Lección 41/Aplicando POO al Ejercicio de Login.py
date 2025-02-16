# En este ejercicio, vamos a crear una clase de la cual se podrán generar instancias de tipo ventana (de Login)

# Importamos los módulos necesarios para la manipulación de objetos gráficos
import tkinter
from tkinter import ttk, messagebox

# Clase de Tipo VentanaLogin
class VentanaLogin(tkinter.Tk): # <-- Heredamos de la clase de tipo Ventana Original
    def __init__(self):
        super().__init__() # <-- Inicializamos nuestra instancia con el mismo proceso inicializador que el de una ventana
        # Asignamos los atributos de nuestra ventana
        self.geometry('300x100')
        self.title('Login')
        self.iconbitmap('icono.ico')
            # Evitamos que la ventana cambie de tamaño
        self.resizable(False, False)
            # Configuramos la proporción de filas y columnas
                # Filas
        self.rowconfigure(0, weight = 30)
        self.rowconfigure(1, weight = 30)
        self.rowconfigure(2, weight = 40)
                # Columnas
        self.columnconfigure(0, weight = 30)
        self.columnconfigure(1, weight = 80)
        # Creamos los widgets de la ventana
        self._crearComponentes()

    def _crearComponentes(self): # <-- Este método esta protegido, por lo que sólo debe ser accesado dentro de la clase
        # Etiquetas
        ttk.Label(self, text = 'Usuario:').grid(row = 0, column = 0, sticky = 'E')
        ttk.Label(self, text = 'Contraseña:').grid(row = 1, column = 0, sticky = 'E')

        # Entradas
        self.entryUser = ttk.Entry(self, width = 30, justify = 'center')
        self.entryUser.grid(row = 0, column = 1, sticky = 'W')
        self.entryPassword = ttk.Entry(self, width = 30, justify = 'center', show = '*')
        self.entryPassword.grid(row = 1, column = 1, sticky = 'W')

        # Botones
        ttk.Button(self, text = 'Login', command = self._eventoLogin).grid(row = 2, column = 0, columnspan = 2)

    def _eventoLogin(self):
        messagebox.showinfo(title = 'Información del Usuario', message = f'Usuario: {self.entryUser.get()}\nContraseña: {self.entryPassword.get()}')
        self.entryUser.delete(0, tkinter.END)
        self.entryPassword.delete(0, tkinter.END)

if __name__ != '__main__':
    # Imprimimos un mensaje de exportación correcta de los módulos de la rutina
    print(f'Los módulos de creación de ventanas con POO han sido exportados con éxito. ')
else:
    # Realización de pruebas de los módulos de la rutina
    ventana1 = VentanaLogin()
    ventana1.mainloop()