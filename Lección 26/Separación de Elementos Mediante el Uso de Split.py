help(str.split)

cadenaDeElementos = 'Java Javascript Python CSS C'
listaResultadoDeSplit = cadenaDeElementos.split() # <-- Sintáxis: <cadena de elementos a separar>.split(<cadena para usar como separador>, <máximos elementos a separar>)
print(f'Resultado de separar los elementos de una cadena, usando " " como separador: ')
print(f'\t{listaResultadoDeSplit}\n')

cadenaDeElementos = 'Java, Javascript, Python, CSS, C'
listaResultadoDeSplit = cadenaDeElementos.split(', ')
print(f'Resultado de separar los elementos de una cadena, usando ", " como separador: ')
print(f'\t{listaResultadoDeSplit}\n')

cadenaDeElementos = 'Java,Javascript,Python,CSS,C'
listaResultadoDeSplit = cadenaDeElementos.split(',', 2)
print(f'Resultado de separar solamente 2 elementos de una cadena, usando "," como separador: ')
print(f'\t{listaResultadoDeSplit}\n')