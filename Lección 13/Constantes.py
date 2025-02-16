# En Python, no existe una sintaxis para establecer variables constantes (variables cuyo valor no puede ser cambiado)
# Debido a esto, solo podemos establecer una nomenclatura que funcione para que el desarrollador ubique las variables "constantes"
# Dicha nomenclatura consta de establecer el nombre de una variable en Mayusculas

from Modulo_de_Recurso_para_Tema_de_Constantes import CONSTANTE, Matematicas as Math

print("Impresion de Valores Constantes". center(50, '-'))
print(f'{CONSTANTE} \n {Math.PI}')