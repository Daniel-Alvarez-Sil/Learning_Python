# Este módulo crea una clase que genera instancias de tipo Frame con un widget de imagen

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, messagebox

# Clase de tipo Frame con Widget de Imagen
class TabuladorImagen(ttk.Frame):
    def __init__(self, cParamTabuladorPadre):
        # Utilizamos el inicializador de la clase Frame
        super().__init__(cParamTabuladorPadre)
        # Asignamos los widgets del Frame
        self.imagen = tkinter.PhotoImage(file ='C:\Programación\Python\Lección 41\Ejercicio_Final_Módulos\python-logo.png')
        ttk.Button(self, image = self.imagen, command = self.eventoBoton).grid(row = 0, column = 0)

    def eventoBoton(self):
        messagebox.showinfo(title = 'Información', message = f'Has seleccionado la imagen: \n{self.imagen.cget("file")}')

if __name__ != '__main__':
    # Impresión con relación a la correcta exportación del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    # Realización de Pruebas
    ventana = tkinter.Tk()
    ventana.geometry('600x500')
    ventana.title('Prueba')

    tabuladores = ttk.Notebook(ventana)
    tabuladores.add(TabuladorImagen(tabuladores), text = 'Imagen')

    tabuladores.pack(fill = 'both')
    ventana.mainloop()