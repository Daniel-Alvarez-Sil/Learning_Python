# El tipo de Dato None Constituye una Ausencia de Información

# El tipo de dato None se vuelve un FALSE cuando es pasado por el constructor de BOOL

listFalses = ['', [], (), {}, 0, 0.00, False, None]

print(f'Impresión de las 8 Formas de Expresar Falsedad'.center(len('Impresión de las 8 Formas de Expresar Falsedad') + 10, '-'))

print('\n')

for element in listFalses:
    print(f'Dato: {element} \nTipo de Dato: {type(element)} \nValor Bool del Dato: {bool(element)}\n\n')
