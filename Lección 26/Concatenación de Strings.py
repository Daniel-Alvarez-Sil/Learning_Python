
mensajeConcatenado = 'Hola' ' ' 'Mundo' # <--- Esta sintáxis es igual a = 'Hola' + ' ' + 'Mundo'
                                        # <--- Esta sintáxis solo funciona con literales de string
print(f'Este es un mensaje concatenado: {mensajeConcatenado}')

mensajeConcatenado2 = 'Soy Daniel, ' + mensajeConcatenado
print(f'Este es otro mensaje concatenado: {mensajeConcatenado2}')

mensajeConcatenado2 += ', Adios!'
print(f'Este es otro mensaje concatenado: {mensajeConcatenado2}')

