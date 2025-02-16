# En este módulo se elabora una clase capaz de crear instancias de tipo Notebook

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, messagebox
from Ejercicio_Final_Módulos.Módulo_de_Tabulador_Normal import TabuladorNormal
from Ejercicio_Final_Módulos.Módulo_de_Scrolled_Text import TabuladorScrolledText
from Ejercicio_Final_Módulos.Módulo_de_Combo_Box import TabuladorComboBox
from Ejercicio_Final_Módulos.Módulo_de_Imagen import TabuladorImagen
from Ejercicio_Final_Módulos.Módulo_de_Progress_Bar import TabuladorProgressBar

# Clase de Tipo Notebook
class TabuladoresWidgets(ttk.Notebook):
    def __init__(self, cParamVentanaPadre):
        # Utilizamos el inicializador de la clase Notebook
        super().__init__(cParamVentanaPadre)
        # Agregamos los tabuladores del notebook
        self.add(TabuladorNormal(self), text = 'Tabulador Normal')
        self.add(TabuladorScrolledText(self), text = 'Scrolled Text')
        self.add(TabuladorComboBox(self), text = 'ComboBox')
        self.add(TabuladorImagen(self), text = 'Imagen')
        self.add(TabuladorProgressBar(self), text = 'Progress Bar')

if __name__ != '__main__':
    # Impresión con relación a la correcta exportación del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')

else:
    # Realización de Pruebas
    ventana = tkinter.Tk()
    ventana.geometry('600x500')
    ventana.title('Prueba')

    TabuladoresWidgets(ventana).pack(fill = 'both')
    ventana.mainloop()
