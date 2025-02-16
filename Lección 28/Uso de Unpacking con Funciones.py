def regresaTupla():
    return (1,2,3,4,5,6,7,8,9,10)

valor1, valor2, *tupla3 = regresaTupla()

print(f'Valores de las variables: {valor1, valor2, tupla3}\nTipos de Datos: {type(valor1), type(valor2), type(tupla3)}')