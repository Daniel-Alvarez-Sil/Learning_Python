# Conversión de STRING a BYTES y Viceversa

stringDeEjemplo = 'Programación con Python'
print(f'String Original: {stringDeEjemplo}. ')
    # Codificación de STRING a BYTES
bytes = stringDeEjemplo.encode('utf-8')
print(f'String codificado en bytes: {bytes}. ')

        # Impresión del STRING codificado en BYTES
print(f'Impresión del STRING codificado en BYTES: ')
for letra in bytes:
    print(f'{chr(letra)} - {letra}')

    # Decodificación de BYTES a STRING
stringDecodificado = bytes.decode('utf-8')
print(f'Bytes decodificados: {stringDecodificado}. ')
if (stringDeEjemplo == stringDecodificado):
    print(f'El string original ha sido codificado y decodificado correctamente. ')