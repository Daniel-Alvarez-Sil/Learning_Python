# Este procedimiento crea una clase de tipo Calculadora

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import messagebox

# Clase de Tipo Botón para Escribir
class WritingButton(tkinter.Button):
    def __init__(self, cParamPadreFrame, cParamElemento, iParamRow, iParamCol, cParamEntrySearch):
        # Utilizamos el inicializador de la clase Button
        super().__init__(cParamPadreFrame, text=str(cParamElemento), bd=0,
                   bg='#fff' if isinstance(cParamElemento, int) else '#eee', cursor='hand2',
                   width=13, height=5,
                    command=lambda: self._eventoClick(cParamElemento, cParamEntrySearch))
        self.grid(row=iParamRow, column=iParamCol, padx=1, pady=1, sticky='NSWE')

    # Evento para escribir caracteres en la barra de búsqueda
    def _eventoClick(self, cParamElemento, cParamEntrySearch):
        # print(cParamElemento)
        if cParamElemento != ' ':
            cParamEntrySearch.insert(tkinter.END, f'{cParamElemento}')

# Clase de Tipo Calculadora:
class Calculadora(tkinter.Tk):
    def __init__(self):

        # Utilizamos el inicializador de la clase de Ventana
        super().__init__()

        # Creamos la ventana y sus atributos
        self.geometry('400x450+600+100')
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        self.resizable(0, 0)
            # Proporción de filas y columnas
                # Filas
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 8)
                # Columnas
        self.columnconfigure(0, weight = 1)

        self._crearWidgets()

    def _crearWidgets(self):

        # Creamos los 2 Frames (y sus atributos) que constituyen la ventana, la botonera y la barra de búsqueda
        frameBusqueda = tkinter.Frame(self, background = 'yellow', width = 400, height = 50)
        frameBusqueda.pack(side = tkinter.TOP)
            # Proporción de filas y columnas
                # Filas
        frameBusqueda.rowconfigure(0, weight = 1)
                # Columnas
        frameBusqueda.columnconfigure(0, weight = 1)

        frameBotonera = tkinter.Frame(self, width = 400, height = 400, bg= 'grey')
        frameBotonera.pack()
            # Proporcion de filas y columnas
                # Filas
        frameBotonera.rowconfigure(0, weight = 1)
        frameBotonera.rowconfigure(1, weight = 1)
        frameBotonera.rowconfigure(2, weight = 1)
        frameBotonera.rowconfigure(3, weight = 1)
        frameBotonera.rowconfigure(4, weight = 1)
                # Columnas
        frameBotonera.columnconfigure(0, weight = 1)
        frameBotonera.columnconfigure(1, weight = 1)
        frameBotonera.columnconfigure(2, weight = 1)
        frameBotonera.columnconfigure(3, weight = 1)

        # Creamos los widgets de los frames de la ventana
            # Entrada
        self._entrySearch = tkinter.Entry(frameBusqueda, justify=tkinter.RIGHT,
                        width=30, font=('arial', 18, 'bold'))
        self._entrySearch.grid(row = 0, column = 0, padx = 1, pady = 1, ipadx = 5, ipady = 5)
            # Botones
                # Botón para Limpiar
        tkinter.Button(frameBotonera, text='C', bd = 0, bg='#eee', cursor = 'hand2', width = 30, height = 5,
                       command = self._limpiar).grid(row=0, column=0, columnspan=3, padx = 1, pady = 1, sticky = 'NSWE')
                # Botón para Evaluar
        tkinter.Button(frameBotonera, text = '=', bd = 0, bg = '#eee', cursor = 'hand2', command = self._evaluar)\
            .grid(row = 4, column = 3, padx = 1, pady = 1, sticky = 'NSWE')
                # Botones para Escribir
        self._botonesParaEscribir(frameBotonera)

    # Método para accesar el atributo protegido, "_entrySearch"
    @property
    def entrySearch(self):
        return self._entrySearch

    # Método para crear de manera dinámica los botones para escribir
    def _botonesParaEscribir(self, cParamPadreFrame):
        botones = [['', '', '', '/'], [7, 8, 9, '*'], [4, 5, 6, '-'], [1, 2, 3, '+'], [' ', 0, '.', '']]
        iRow = 0
        for fila in botones:
            iCol = 0
            for elemento in fila:
                if not elemento == '':
                    WritingButton(cParamPadreFrame, elemento, iRow, iCol, self.entrySearch)
                iCol = iCol + 1
            iRow = iRow + 1

    # Evento para borrar la operación en la barra de búsqueda
    def _limpiar(self):
        self._entrySearch.delete(0, tkinter.END)

    # Evento para evaluar la operación en la barra de búsqueda
    def _evaluar(self):
        cOperacion = self._entrySearch.get()
        if cOperacion:
            try:
                self._entrySearch.delete(0, tkinter.END)
                iResultado = eval(cOperacion)
            except BaseException:
                messagebox.showinfo(title = 'Error en tu Operación', message = 'Por favor valida tu operación. ')
            else:
                self._entrySearch.insert(0, iResultado)


calculadora = Calculadora()
calculadora.mainloop()