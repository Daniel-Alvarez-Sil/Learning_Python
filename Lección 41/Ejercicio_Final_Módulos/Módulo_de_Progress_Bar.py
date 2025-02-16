# Este módulo elabora una clase capaz de crear instancias de tipo Frame con un Widget de Progress Bar

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from time import sleep
from tkinter import messagebox, ttk

# Clase de Tipo Frame con Widget de Progress Bar
class TabuladorProgressBar(ttk.Frame):
    def __init__(self, cParamTabuladorPadre):
        # Utilizamos el inicializador de la clase Frame
        super().__init__(cParamTabuladorPadre)

        # Asignamos los atributos del Frame
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)

        # Asignamos los objetos del Frame
            # Progress Bar
        self._progressBar = ttk.Progressbar(self, orient = 'horizontal', length = 400)
        self._progressBar.grid(row = 0, column = 0, columnspan = 4)
            # Botones
        self._botonIniciar = ttk.Button(self, text = 'Iniciar', command = self.eventoIniciar)
        self._botonIniciar.grid(row = 1, column = 0)
        self._botonReiniciar = ttk.Button(self, text = 'Reiniciar', command = self.eventoReiniciar)
        self._botonReiniciar.grid(row = 1, column = 1)
        self._botonCiclo = ttk.Button(self, text = 'Ciclar', command = self.eventoCiclo)
        self._botonCiclo.grid(row = 1, column = 2)
        self._botonDetener = ttk.Button(self, text = 'Detener', command = self.eventoDetener)
        self._botonDetener.grid(row = 1, column = 3)

    # Funciones de los Botones
    def eventoIniciar(self):
        self._botonIniciar.config(state = 'disabled')
        self._botonReiniciar.config(state = 'disabled')
        self._botonCiclo.config(state = 'disabled')
        self._botonDetener.config(state = 'disabled')
        self._progressBar['maximum'] = 100
        for x in range(100):
            sleep(0.05)
            self._progressBar['value'] = x
            self._progressBar.update()
        self._progressBar.stop()
        self._botonIniciar.config(state = 'enabled')
        self._botonReiniciar.config(state = 'enabled')
        self._botonCiclo.config(state = 'enabled')
        self._botonDetener.config(state = 'enabled')

    def eventoReiniciar(self):
        self._progressBar['value'] = 0

    def eventoCiclo(self):
        self._progressBar.start()

    def eventoDetener(self):
        self._progressBar.stop()

if __name__ != '__main__':
    # Impresión con relación a la correcta exportación del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    # Realización de Prueba
    ventana = tkinter.Tk()
    ventana.geometry('800x800')
    ventana.title('Prueba')

    tabuladores = ttk.Notebook(ventana)
    tabuladores.add(TabuladorProgressBar(tabuladores), text = 'Progress Bar')

    tabuladores.pack(fill = 'both')
    ventana.mainloop()
